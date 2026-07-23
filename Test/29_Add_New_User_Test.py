import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Add_User_Page import User


from configReader import ConfigReader
from Pages.LoginPage import loginPage


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        This method runs only once before all test methods
        inside this class.
        """

        chrome_options = Options()

        # 1 = Allow notifications
        # 2 = Block notifications
        prefs = {
            "profile.default_content_setting_values.notifications": 1
        }

        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")

        cls.driver = webdriver.Chrome(options=chrome_options)

        # Prefer explicit waits inside page methods.
        # Keep implicit wait small.
        cls.driver.implicitly_wait(3)

        cls.login()


    @classmethod
    def login(cls):
        """
        Login and open the Bookkeeping section once.
        """

        driver = cls.driver

        config = ConfigReader(
            r"C:\Users\CT_USER\PycharmProjects\BOOKKEEPING"
            r"\config.properties"
        )

        login_page = loginPage(driver)

        driver.get(
            config.get_value("DEFAULT", "URL")
        )

        login_page.enter_username(
            config.get_value("DEFAULT", "USERNAME")
        )

        time.sleep(1)

        login_page.enter_password(
            config.get_value("DEFAULT", "Password")
        )

        time.sleep(1)

        login_page.click_sign_in_button()

        time.sleep(5)

        login_page.Click_On_Menu()

        time.sleep(0.5)

        login_page.Click_Bookkeeping()

        time.sleep(0.5)



        print("Login and Bookkeeping navigation completed.")



#-----------------------------------------------------------------------------------------------------------------------
    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Expense claims>> Add new User"
    )
    @pytest.mark.description(
        "Select company and create a new User"
    )
    def test_29_Add_New_User(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Expense claims
        4. Create new user
        5. Save user-- By: - Ranveer
        """

        expense_claims_page = User(
            driver=self.driver
        )
        time.sleep(.2)
        expense_claims_page.Select_Search()
        time.sleep(5)
        expense_claims_page.Enter_Company()
        time.sleep(.5)
        expense_claims_page.Click_Company()
        time.sleep(.2)
        expense_claims_page.Click_Input()
        time.sleep(.2)
        expense_claims_page.Click_Expense_Claims()
        time.sleep(.5)


        expense_claims_page.User_Section()
        time.sleep(.2)
        expense_claims_page.Click_Add_User()
        time.sleep(.2)
        expense_claims_page.Click_Name_Field()
        time.sleep(.2)
        expense_claims_page.Select_Title()
        time.sleep(.2)
        expense_claims_page.Enter_name()
        time.sleep(.2)

        expense_claims_page.Enter_Ni_Number()
        time.sleep(.2)
        expense_claims_page.Save_User()
        time.sleep(.2)





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