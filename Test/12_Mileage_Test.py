import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from Pages.Mileage_Page import Mileage

from configReader import ConfigReader

from Pages.LoginPage import loginPage
import pytest


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # --- Chrome Options Setup ---
        chrome_options = Options()
        # 1 = Allow, 2 = Block
        prefs = {"profile.default_content_setting_values.notifications": 1}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")

        # Initialize WebDriver with options
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(3)

        # Call login once setup is done
        cls.login()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def login(cls):
        driver = cls.driver
        config = ConfigReader(r"C:\Users\CT_USER\PycharmProjects\BOOKKEEPING\config.properties")

        # Instance of login_page
        loginpage = loginPage(driver)

        # Open the site
        driver.get(config.get_value("DEFAULT", "URL"))

        # Login flow
        loginpage.enter_username(config.get_value("DEFAULT", "USERNAME"))
        time.sleep(1)
        loginpage.enter_password(config.get_value("DEFAULT", "Password"))
        time.sleep(1)
        loginpage.click_sign_in_button()
        time.sleep(5)

        # Menu navigation
        loginpage.Click_On_Menu()
        time.sleep(2)
        loginpage.Click_Bookkeeping()
        time.sleep(2)


        if __name__ == "__main__":
            unittest.main()

    @pytest.mark.navigation("Login >> Admin Dashboard >> Bookkeeping >> Client ")
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> mileage")


    def test_16_Mileage(self):
        client_section = Mileage(driver=self.driver)

        # Open company
        client_section.Select_Search()
        client_section.Enter_Company()
        client_section.Click_Company()

        # Open Expense Claims
        client_section.Click_Input()
        client_section.Click_Expense_Claims()

        # Open Mileage form
        client_section.Mileages_Section()
        client_section.Click_Mileages()

        # Fill mileage details
        client_section.Select_Directors()
        client_section.Enter_Remark_Mileages()
        client_section.Engine_Type()
        client_section.Enter_Description_Mileage()
        client_section.Mileage()
        client_section.Select_Rate()

        # Save mileage
        client_section.Save_Mileage()
        client_section.wait_for_loader_to_disappear()

        print("Mileage workflow completed successfully.")



    @classmethod
    def tearDownClass(cls):
        """
        This method runs once after all test methods finish.
        """

        if hasattr(cls, "driver"):
            cls.driver.quit()

        print("Browser closed successfully.")


if __name__ == "__main__":
    unittest.main()

