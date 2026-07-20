import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Client_SellPage import ClientSell
from ExpenseclaimsPage import Expenseclaims
from PurchasePage import ClientPurchase
from Find_And_Match_Lock_Page import Find_And_Match_Lock
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


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >> Sale"
    )
    @pytest.mark.description(
        "Select company and create a new sales invoice"
    )


    def test_28_1_Add_New_Sale_Invoice_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Sales
        4. Create invoice
        5. Save invoice
        """

        company_page = Find_And_Match_Lock(
            driver=self.driver
        )

        company_page.Select_Search()
        time.sleep(0.5)

        company_page.Enter_Company()
        time.sleep(0.5)

        company_page.Click_Company()
        time.sleep(1)

        print("Company selected successfully.")


        # -------------------------------------------------------
        # Step 2: Open Sales section
        # -------------------------------------------------------


        client_sell_page = ClientSell(
            driver=self.driver
        )

        client_sell_page.Click_Input()
        time.sleep(0.5)

        client_sell_page.Click_Sales()
        time.sleep(0.5)

        client_sell_page.wait_for_loader_to_disappear()
        time.sleep(0.5)

        print("Sales section opened successfully.")

        # -------------------------------------------------------
        # Step 3: Add invoice
        # -------------------------------------------------------

        client_sell_page.Add_Invoice()
        time.sleep(0.5)

        client_sell_page.Select_Customer_Keyboard()
        time.sleep(0.5)

        client_sell_page.Add_Attachment()
        time.sleep(0.5)

        client_sell_page.Select_item_sale()
        time.sleep(0.5)



        # client_sell_page.Enter_Discount()
        # time.sleep(0.5)

        # client_sell_page.Click_Enter_Notes()
        # time.sleep(0.5)
        #
        # client_sell_page.Enter_Notes()
        # time.sleep(0.5)

        # -------------------------------------------------------
        # Step 4: Save invoice
        # -------------------------------------------------------

        client_sell_page.Click_Save()

        client_sell_page.wait_for_loader_to_disappear()
        time.sleep(1)

        print("Invoice created and saved successfully.")

        client_sell_page.Click_Pound_Icon()
        time.sleep(.2)
        client_sell_page.Click_Save()
        print("Receipt Created Successfully.....")

    #-------------------------------------------------------------------------------------------------------------------


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Purchase Order"
    )
    @pytest.mark.description(
        "Select company and create a new Purchase invoice"
    )



    def test_28_2_Add_New_Purchase_Invoice_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Purchase
        4. Create invoice
        5. Save invoice
        """

        purchase_sell_page = ClientPurchase(
            driver=self.driver
        )

        purchase_sell_page.Click_Purchases()
        time.sleep(.5)
        time.sleep(.2)

        purchase_sell_page.Add_Invoice()
        time.sleep(.2)
        purchase_sell_page.Select_Customer()
        time.sleep(.2)

        purchase_sell_page.Add_Attachment()
        time.sleep(.2)
        purchase_sell_page.Enter_Discount()
        time.sleep(.2)
        # client_section.Click_Enter_Notes()
        # time.sleep(.2)
        # client_section.Enter_Notes()
        # time.sleep(.2)

        purchase_sell_page.Select_item_purchase()
        time.sleep(.5)
        purchase_sell_page.Enter_amount()
        time.sleep(2)
        purchase_sell_page.Save_Services()
        time.sleep(.2)
        purchase_sell_page.wait_for_loader_to_disappear()
        time.sleep(0.5)
        purchase_sell_page.Click_Pound_Icon()
        time.sleep(.2)
        purchase_sell_page.Select_Account()
        time.sleep(.2)
        purchase_sell_page.Enter_Amount()
        time.sleep(.2)





    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Expense claims"
    )
    @pytest.mark.description(
        "Select company and create a new Expense claims"
    )
    def test_28_3_Add_New_Expense_Claims_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Expense claims
        4. Create claim
        5. Save claim-- By: - Ranveer
        """

        expense_claims_page = Expenseclaims(
            driver=self.driver
        )
        expense_claims_page.Click_Expense_Claims()
        time.sleep(.5)
        time.sleep(.2)

        expense_claims_page.Click_Expense_Claims_Button()
        time.sleep(.2)
        expense_claims_page.Select_Directors()
        time.sleep(.2)
        expense_claims_page.Enter_Remark()
        time.sleep(.2)
        expense_claims_page.Add_Attachment()
        time.sleep(.2)

        expense_claims_page.Enter_Bill_No()
        time.sleep(.2)
        expense_claims_page.Enter_Description()
        time.sleep(.2)
        expense_claims_page.Select_Account()
        time.sleep(.2)
        expense_claims_page.Base_Amount()
        time.sleep(.2)
        expense_claims_page.Select_Vat()
        time.sleep(10)
        expense_claims_page.Save_Expense()
        time.sleep(.2)

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Bank"
    )
    @pytest.mark.description(
        "Select company and create a new Expense claims"
    )
    def test_28_3_Add_New_Expense_Claims_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Expense claims
        4. Create claim
        5. Save claim-- By: - Ranveer
        """

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