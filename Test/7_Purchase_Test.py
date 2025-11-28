import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.PurchasePage import ClientPurchase
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


    def test_10_Go_Client_Purchase(self):
        client_section = ClientPurchase(driver=self.driver)
        time.sleep(.2)
        client_section.Select_Business()
        time.sleep(3)
        client_section.Click_Input()
        time.sleep(.2)


        client_section.Click_Purchases()
        time.sleep(.5)
        time.sleep(.2)


        client_section.Add_Invoice()
        time.sleep(.2)
        client_section.Select_Customer()
        time.sleep(.2)
        client_section.Select_item_purchase()
        time.sleep(.5)
        client_section.Enter_amount()
        time.sleep(2)
        client_section.Save_Services()
        time.sleep(.2)


    def test_11_Go_Purchase_CreditNote(self):
        client_section = ClientPurchase(driver=self.driver)
        time.sleep(.2)


        # client_section.Select_Business()
        # time.sleep(3)
        # client_section.Click_Input()
        # time.sleep(.2)
        # client_section.Click_Purchases()


        time.sleep(.5)
        time.sleep(.2)
        client_section.Click_Credit_Notes()
        time.sleep(.5)
        client_section.Add_Credit_Note()
        time.sleep(.3)
        client_section.Select_Suppiler_for_Credit_Note()
        time.sleep(.3)
        client_section.Invoice_ref()
        time.sleep(.2)
        client_section.Save_Credit_Notes()
        time.sleep(.2)
        client_section.Click_Save_Button()
        time.sleep(.2)



    def test_12_Go_Purchase_PO(self):
        client_section = ClientPurchase(driver=self.driver)
        time.sleep(.2)



        # client_section.Select_Business()
        # time.sleep(3)
        # client_section.Click_Input()
        # time.sleep(.2)
        # client_section.Click_Purchases()



        time.sleep(.5)
        time.sleep(.2)
        client_section.Purchase_Order()
        time.sleep(.5)
        client_section.Click_Purchase_Order()
        time.sleep(.2)
        client_section.Select_Contact_Name()
        time.sleep(.2)
        client_section.Click_Item_For_Invoice()
        time.sleep(.2)
        client_section.Save_PO()
        time.sleep(.2)

    def test_13_Go_Payments(self):
        client_section = ClientPurchase(driver=self.driver)
        time.sleep(.2)


        # client_section.Select_Business()
        # time.sleep(3)
        # client_section.Click_Input()
        # time.sleep(.2)
        # client_section.Click_Purchases()


        time.sleep(.5)
        time.sleep(.2)

        client_section.Payment_Section()
        time.sleep(.5)
        client_section.Click_Payment()
        time.sleep(.2)
        client_section.Paid_To_Supplier()
        time.sleep(.2)
        client_section.Select_Account()
        time.sleep(.2)
        client_section.Enter_Amount()
        time.sleep(.2)
        client_section.Save_payment()
        time.sleep(.2)


    def test_14_Create_New_Item(self):
            client_section = ClientPurchase(driver=self.driver)
            time.sleep(.2)

            # client_section.Select_Business()
            # time.sleep(3)
            # client_section.Click_Input()
            # time.sleep(.2)
            # client_section.Click_Purchases()
            # time.sleep(.2)

            time.sleep(.5)
            time.sleep(.2)

            client_section.Item_Section()
            time.sleep(.5)
            client_section.Click_on_item()
            time.sleep(.2)
            client_section.Enter_Name()
            time.sleep(.2)
            client_section.Enter_Description_For_Purchases()
            time.sleep(.2)
            client_section.Enter_Description_For_Sell()
            time.sleep(.2)
            client_section.Enter_Unit_Price_Purchases()
            time.sleep(.2)
            client_section.Enter_Unit_Price_Sell()
            time.sleep(.2)
            client_section.Create_Item()
            time.sleep(.2)





