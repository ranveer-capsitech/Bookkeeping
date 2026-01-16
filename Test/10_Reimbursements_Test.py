import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.ExpenseclaimsPage import Expenseclaims
from Pages.PurchasePage import ClientPurchase
from Pages.Reimbursements_Page import Reimbursement
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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> expense-claims >> reimbursement")


    def test_17_Reimbursement(self):
        client_section = Reimbursement(driver=self.driver)
        time.sleep(.2)

        client_section.Select_Business()
        time.sleep(3)
        client_section.Click_Input()
        time.sleep(.2)

        client_section.Click_Expense_Claims()
        time.sleep(.5)
        time.sleep(.2)

        client_section.Reimbursed_Section()
        time.sleep(.2)
        client_section.Click_Reimbursed()
        time.sleep(.2)
        client_section.Reimbursed_to()
        time.sleep(.2)
        client_section. Reimbursed_Account()
        time.sleep(.2)
        client_section. Enter_Amount()
        time.sleep(.2)
        # client_section.Enter_Notes()
        # time.sleep(.2)
        client_section.Save_Reimbursement()
        time.sleep(.2)


