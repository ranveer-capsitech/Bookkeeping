import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from Pages.Purchase_PO_Page import Purchase_Order
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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> click on purchase")


    def test_12_Go_Purchase_PO(self):
        client_section = Purchase_Order(driver=self.driver)

        # Open company
        client_section.Select_Search()
        client_section.Enter_Company()
        client_section.Click_Company()

        # Open Purchase Order section
        client_section.Click_Input()
        client_section.Click_Purchases()
        client_section.Purchase_Order()
        client_section.Click_Purchase_Order()

        # Fill purchase order
        client_section.Select_Contact_Name()
        client_section.Add_Attachment()
        client_section.Click_Item_For_Invoice()
        client_section.Enter_Discount()
        client_section.Click_Enter_Notes()
        client_section.Enter_Notes()

        # Save purchase order
        client_section.Save_PO()
        client_section.wait_for_loader_to_disappear()

        print("Purchase Order workflow completed successfully.")


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

