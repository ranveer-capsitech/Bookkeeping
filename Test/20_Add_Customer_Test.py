import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from configReader import ConfigReader
from Pages.Add_Customer import Add_Customer
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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> click on sell>> click on add customer section")




    def test_04_Go_Client_Sell(self):

            client_section = Add_Customer(
                driver=self.driver
            )

            client_section.Select_Search()
            client_section.Enter_Company()
            client_section.Click_Company()

            client_section.Click_Input()
            client_section.Click_Sales()

            client_section.Select_Client_Section()
            client_section.Click_On_Add_Customer()

            client_section.Enter_Customer_Name(
                "Anthony"
            )

            # Remove this if it closes the customer form
            client_section.Click_Cancel()

            client_section.Click_Billing_Field()
            client_section.Enter_Building()
            client_section.Enter_Street()
            client_section.Enter_City()
            client_section.Enter_County()
            client_section.Select_Country()
            client_section.Enter_Postcode()

            client_section.Click_Contact_Person()
            client_section.Enter_Name()
            client_section.Enter_Contact_Number()
            client_section.Enter_Mail()

            client_section.Select_Bank()
            client_section.Discount()
            client_section.Select_Vat()
            client_section.Enter_Vat()

            client_section.Project_tags()
            client_section.Add_Attachment()
            client_section.Save_customer()
            client_section.wait_for_loader_to_disappear()

            print(
                "Customer workflow completed successfully."
            )



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



