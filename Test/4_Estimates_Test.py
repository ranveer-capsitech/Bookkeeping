import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Estimates_page import Estimates
from configReader import ConfigReader
from Pages.Client_SellPage import ClientSell
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
        time.sleep(0.5)
        loginpage.Click_Bookkeeping()
        time.sleep(0.5)


        if __name__ == "__main__":
            unittest.main()

    @pytest.mark.navigation("Login >> Admin Dashboard >> Bookkeeping >> Client ")
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> click on sell >> Estimates ")

    def test_07_Add_New_Estimates(self):
        client_section = Estimates(driver=self.driver)
        time.sleep(.2)
        client_section.Select_Search()
        time.sleep(5)
        client_section.Enter_Company()
        time.sleep(.2)
        client_section.Click_Company()
        time.sleep(.2)
        client_section.Click_Input()
        time.sleep(.2)
        client_section.Click_Sales()
        time.sleep(.2)

        client_section.Select_Estimates()
        time.sleep(.2)
        client_section.Add_Estimates()
        time.sleep(.2)
        client_section.Select_Customer_for_Estimate()
        time.sleep(.2)
        client_section.Select_item()
        time.sleep(.2)
        client_section.Add_Attachment()
        time.sleep(.2)
        client_section.Enter_Discount()
        time.sleep(.2)
        client_section.Click_Enter_Notes()
        time.sleep(.2)
        client_section.Enter_Notes()
        time.sleep(.2)

        client_section.Click_Save_Estimation()
        time.sleep(.2)
