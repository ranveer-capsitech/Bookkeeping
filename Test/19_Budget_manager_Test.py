import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.BankingPage import Banking
from Pages.Budget_manager_Page import Budget
from Pages.Dividend_Page import Dividend
from Pages.Journals_Page import Journals
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

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(3)

        cls.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def login(cls):
        driver = cls.driver
        config = ConfigReader(r"C:\Users\CT_USER\PycharmProjects\BOOKKEEPING\config.properties")


        loginpage = loginPage(driver)


        driver.get(config.get_value("DEFAULT", "URL"))


        loginpage.enter_username(config.get_value("DEFAULT", "USERNAME"))
        time.sleep(1)
        loginpage.enter_password(config.get_value("DEFAULT", "Password"))
        time.sleep(1)
        loginpage.click_sign_in_button()
        time.sleep(5)


        loginpage.Click_On_Menu()
        time.sleep(2)
        loginpage.Click_Bookkeeping()
        time.sleep(2)


        if __name__ == "__main__":
            unittest.main()

    @pytest.mark.navigation("Login >> Admin Dashboard >> Bookkeeping >> Client ")
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> Budget manager")


    def test_24_Budget_Manager(self):
        client_section = Budget(driver=self.driver)
        time.sleep(.2)

        client_section.Select_Search()
        time.sleep(5)
        client_section.Enter_Company()
        time.sleep(.2)
        client_section.Click_Company()
        time.sleep(.2)
        time.sleep(3)

        client_section.Click_Add_Budget()
        time.sleep(.2)

        client_section.Add_New_Budget()
        time.sleep(.2)

        client_section.Enter_Name()
        time.sleep(.3)
        client_section.Select_Date()
        time.sleep(.2)
        client_section.Click_Save()
        time.sleep(.2)

        # client_section.Click_On_Saved_Name()
        # time.sleep(.2)
        #
        client_section.Enter_Amount_First()
        time.sleep(.2)
        client_section. Enter_Amount_Second()
        time.sleep(.2)
        client_section.Enter_Amount_Third()
        time.sleep(.2)
        client_section.Click_On_Saved()
        time.sleep(.2)