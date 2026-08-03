import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.Add_Customer import Add_Customer
from Pages.Add_Suppliers import Add_Supplier
from Pages.Add_User_Page import User
from Pages.Assets_Page import Asset
from Pages.Banking_Current_Account_Page import Banking
from Pages.Credit_NotesPage import Credit_Notes
from Pages.Dividend_Page import Dividend
from Pages.Estimates_page import Estimates
from Pages.ExpenseclaimsPage import Expenseclaims
from Pages.Item_Page import Items
from Pages.Journals_Page import Journals
from Pages.Mileage_Page import Mileage
from Pages.Purchase_Credit_Notes_Page import  Purchase_CN
from Pages.Purchase_PO_Page import Purchase_Order
from Pages.Purchase_Payment_Page import Purchase_Payment
from Pages.Receipts_Page import Receipts
from Pages.Refund_Page import Refund
from Pages.Reimbursements_Page import Reimbursement
from configReader import ConfigReader
from Pages.Client_SellPage import ClientSell
from Pages.LoginPage import loginPage
from Pages.PurchasePage import ClientPurchase
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
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> select banking section")


    def test_02_Go_Banking_Section(self):
        """
               Complete dependent workflow:
               1. Search company
               2. Select company
               3. Open banking section

               Automated by: Ranveer Singh Sankhala

               """
        client_section = Banking(driver=self.driver)
        time.sleep(.2)

        client_section.Select_Search()
        time.sleep(2)
        client_section.Enter_Company_For_Main()
        time.sleep(.2)
        client_section.Click_Company_For_Main()
        time.sleep(.3)

        # client_section.Click_Input()
        # time.sleep(.2)

        # client_section.Banking_Section()
        # time.sleep(.2)

        client_section.wait_for_loader_to_disappear()

#-----------------------------------------------------------------------------------------------------------------------


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Banking >> Add Current Account"
    )
    @pytest.mark.description(
        "Select a company, open the Banking section, add a current "
        "account with bank, account number and sort code details, "
        "set it as the primary account, and save it. "

    )
    # def test_03_complete_add_current_bank_account_workflow(self):
    #
    #     """
    #     Complete Add Current Bank Account workflow:
    #
    #     1. Search for a company
    #     2. Select the company
    #     3. Open the Client Input section
    #     4. Open the Banking section
    #     5. Wait for the Banking page to load
    #     6. Click Add Account
    #     7. Select the bank
    #     8. Enter the account number
    #     9. Enter the sort code
    #     10. Set the account as the primary account
    #     11. Save the bank account
    #     12. Wait for the save operation to complete
    #     13. Verify that the current account was created successfully
    #
    #     Automated by: Ranveer Singh Sankhala
    #     """
    #
    #     client_section = Banking(driver=self.driver)
    #     time.sleep(.2)
    #
    #
    #     client_section.Account()
    #     time.sleep(.2)
    #
    #     client_section.Select_Bank()
    #     time.sleep(.2)
    #
    #     client_section.Enter_Account_no()
    #     time.sleep(.2)
    #     client_section.Sort_Code()
    #     time.sleep(.2)
    #     client_section.Click_Primary_Account()
    #     time.sleep(.2)
    #
    #     client_section.Save_Banking()
    #     time.sleep(.2)


#-----------------------------------------------------------------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> input >>sell  "
        "Client >> Add Customer"
    )
    @pytest.mark.description(
        "Open the Client section, add a new customer with billing, "
        "contact, bank, VAT and project details, attach a document, "
        "and save the customer."
    )
#
    def test_04_complete_add_customer_workflow(self):
        """
        Complete Add Customer workflow:

        1. Open the Client section
        2. Click Add Customer
        3. Enter the customer name
        4. Perform the configured Cancel action
        5. Open the Billing Address section
        6. Enter the building information
        7. Enter the street
        8. Enter the city
        9. Enter the county
        10. Select the country
        11. Enter the postcode
        12. Open the Contact Person section
        13. Enter the contact person's name
        14. Enter the contact number
        15. Enter the email address
        16. Select the bank
        17. Enter the discount
        18. Select the VAT option
        19. Enter the VAT number
        20. Add project tags
        21. Add an attachment
        22. Save the customer
        Automated by: Ranveer Singh Sankhala
        """
        client_section = Add_Customer(driver=self.driver)


        client_section.Click_Input()

        client_section.Click_Sales()



        client_section.Select_Client_Section()

        client_section.Click_On_Add_Customer()

        client_section.Enter_Customer_Name()

        client_section.Click_Cancel()

        client_section.Click_Billing_Field()

        client_section.Enter_Building()

        client_section.Enter_Street()

        client_section.Enter_City()

        client_section.Enter_County()

        client_section.Select_Country()

        client_section.Enter_Postcode()

        client_section.Click_Contact_Person()

        # client_section.First_Name()

        client_section.Enter_Name()

        client_section.Enter_Contact_Number()

        client_section.Enter_Mail()

        client_section.Select_Bank()

        client_section.Discount()

        client_section.Select_Vat()

        client_section.Enter_Vat()

        # client_section.Enter_EORI()

        client_section.Project_tags()

        client_section.Add_Attachment()

        client_section.Save_customer()

        client_section.wait_for_loader_to_disappear()

        print(
            "Add Customer workflow completed successfully: "
            "customer details entered and saved."
        )


# # #-----------------------------------------------------------------------------------------------------------------------
#
    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Items >> Add Item"
    )
    @pytest.mark.description(
        "Open the Items section, enter the item name, purchase and "
        "sales descriptions, set purchase and selling prices, and "
        "create the new item."
    )


    def test_05_add_new_item(self):
        """
        Complete Add Item workflow:

        1. Open the Items section
        2. Click Add Item
        3. Wait for the Add Item form to load
        4. Enter the item name
        5. Enter the purchase description
        6. Enter the sales description
        7. Enter the purchase unit price
        8. Enter the selling unit price
        9. Click Create
        10. Wait for item creation to complete
        11. Verify that the new item was created successfully
           Automated by: Ranveer Singh Sankhala
        """

        client_section = Items(driver=self.driver)


        client_section.Item()
        client_section.Add_Item()

        client_section.wait_for_loader_to_disappear(
            timeout=10
        )

        client_section.Enter_Name()
        client_section.Purchases_Description()
        client_section.Sales_Description()

        client_section.Enter_Unit_Price_Pur()
        client_section.Enter_Unit_Price_Sell()

        client_section.Create()

        client_section.wait_for_loader_to_disappear()

        print(
            "Add Item workflow completed successfully."
        )




# ----------------------------------------------- Estimates-----------------------------------------------------------------


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Sales >> Estimates"
    )
    @pytest.mark.description(
        "Select a company, create and save a new estimate, download "
        "the estimate, convert it into a direct invoice, and save "
        "the generated invoice."
    )

    def test_06_complete_estimate_workflow(self):
        """
        Complete Estimate workflow:

        1. Search for a company
        2. Select the company
        3. Open the Client Input section
        4. Open the Sales section
        5. Open the Estimates section
        6. Click Add Estimate
        7. Select a customer
        8. Select an item
        9. Add an attachment
        10. Enter the discount
        11. Open the notes field
        12. Enter estimate notes
        13. Save the estimate
        14. Wait for estimate creation to complete
        15. Download the estimate
        16. Wait for the download action to complete
        17. Convert the estimate into a direct invoice
        18. Save the generated invoice
        19. Wait for invoice creation to complete
        20. Verify that the direct invoice was created successfully
          Automated by: Ranveer Singh Sankhala
        """

        client_section = Estimates(driver=self.driver)
        time.sleep(.2)

        client_section.Select_Estimates()
        client_section.Add_Estimates()

        client_section.Select_Customer_for_Estimate()
        client_section.Select_item()

        client_section.Add_Attachment()
        client_section.Enter_Discount()

        client_section.Click_Enter_Notes()
        client_section.Enter_Notes()

        client_section.Click_Save_Estimation()
        client_section.wait_for_loader_to_disappear()

        client_section.Download_Invoice()
        client_section.wait_for_loader_to_disappear()

        client_section.Create_Direct_Invoice()
        client_section.Save_Direct_Invoice()
        client_section.wait_for_loader_to_disappear()


        client_section.Refresh_Page()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        print(
            "Estimate workflow completed successfully: "
            "estimate created, downloaded, and converted into an invoice."
        )




##-----------------------------------------------Sales >> Invoices-----------------------------------------------------------------
    @pytest.mark.navigation(

        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Sales >> Invoices"
    )

    @pytest.mark.description(
        "Create and save a sales invoice, validate search, date filter, "
        "report visibility and pagination, clone the invoice, mark it "
        "as bad debt, and download the invoice."
    )

    def test_07_complete_sales_invoice_workflow(self):
        """
        Complete Sales Invoice workflow:

        1. Open the Add Invoice form
        2. Select a customer
        3. Add an attachment
        4. Select a sales item
        5. Enter the discount
        6. Enter invoice notes
        7. Save the invoice
        8. Wait for the invoice list to load
        9. Search for the saved invoice
        10. Clear the invoice search
        11. Validate the date calendar
        12. Apply the required filter
        13. Hide report information
        14. Change the pagination
        15. Open the invoice action menu
        16. Clone the invoice
        17. Save the cloned invoice
        18. Open the invoice action menu again
        19. Mark the invoice as bad debt
        20. Save the bad-debt changes
        21. Download the invoice
        22. Confirm completion of the workflow
           Automated by: Ranveer Singh Sankhala
        """



        client_section = ClientSell(driver=self.driver)

        client_section.Invoice_Section()
        time.sleep(.2)
        client_section.Add_Invoice()
        time.sleep(.1)

        client_section.Select_Customer_Keyboard()
        time.sleep(.2)

        client_section.Add_Attachment()
        time.sleep(.2)

        client_section.Select_item_sale()
        time.sleep(.5)

        client_section.Enter_Discount()
        time.sleep(.3)
        # client_section.Click_Enter_Notes()
        # time.sleep(.3)
        # client_section.Enter_Notes()
        # time.sleep(.3)

        client_section.Click_Save()
        time.sleep(2)
        client_section.wait_for_loader_to_disappear()

    #-------------------------------------------------------------------------------------------------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Enter_Search()
        time.sleep(.5)
        client_section. Remove_Search()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Change_Date_Calendar()
        time.sleep(1)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Select_Filter()
        time.sleep(.2)
        client_section.Hide_Reports()
        time.sleep(.2)
        client_section.Change_Pagination()

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Click_Three_Dot()
        time.sleep(.2)
        client_section.Click_Clone()
        time.sleep(.2)
        client_section.Clone_Save()
        time.sleep(.5)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Three_Dot()
        time.sleep(.2)
        client_section.Bad_Debts()
        time.sleep(.2)
        client_section.Bad_Debts_Save()
        time.sleep(2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Download_Invoice()
        time.sleep(.2)
        client_section.Refresh_Page()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()


        print(
            "Sell Invoice workflow completed successfully: "
            "All Test Cases of Sell Invoice Section Completed."
        )


        #---------------------------------------------------------------------------------------------------------------


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Sales >> Receipts"
    )
    @pytest.mark.description(
        "Select a company, open the Receipts section, create and save "
        "a new receipt with payment and attachment details, and "
        "download the saved receipt."
    )


    def test_08_complete_receipt_workflow(self):
        """
        Complete Receipt workflow:

        1. Search for a company
        2. Select the company
        3. Open the Client Input section
        4. Open the Sales section
        5. Open the Receipts section
        6. Click Add Receipt
        7. Select who the payment was received from
        8. Enter the receipt amount
        9. Select the payment method
        10. Add an attachment
        11. Open the notes field
        12. Enter receipt notes
        13. Save the receipt
        14. Wait for the receipt to be saved
        15. Download the saved receipt
        16. Wait for the download action to complete
        17. Verify that the receipt was created successfully
          Automated by: Ranveer Singh Sankhala
        """
        client_section = Receipts(driver=self.driver)
        time.sleep(.2)

        client_section.Receipts()
        time.sleep(.2)
        client_section.Add_Receipts()
        time.sleep(.2)
        client_section.Select_Receipts_from()
        time.sleep(.2)
        # client_section.Select_Amount()
        # time.sleep(.2)
        client_section.Enter_Amount()
        time.sleep(.2)
        client_section.Select_Method()
        time.sleep(.2)
        client_section.Add_Attachment()
        time.sleep(.2)
        client_section.Click_Enter_Notes()
        time.sleep(.2)
        client_section.Enter_Notes()
        time.sleep(.2)
        client_section.Save_Receipt()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Download_Invoice()
        time.sleep(.2)
        client_section.Refresh_Page()

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        print(
            "Receipt workflow completed successfully: "
            "receipt created, saved, and downloaded."
        )



# #----------------------------------------------------------------------------------------------------------------------



    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Sales >> Credit Notes"
    )
    @pytest.mark.description(
        "Open the Credit Notes section, create and save a credit note, "
        "validate search, calendar and filter functionality, and download "
        "the credit note."
    )
    def test_09_complete_credit_note_workflow(self):
        """
        Complete Credit Note workflow:

        1. Open the Credit Notes section
        2. Click Add Credit Note
        3. Select a customer
        4. Select or enter the invoice reference
        5. Add an attachment
        6. Enter the discount
        7. Click the notes field
        8. Enter credit note details
        9. Save the credit note information
        10. Click the final Save button
        11. Wait for the page to finish loading
        12. Search for the saved credit note
        13. Clear the search
        14. Wait for the results to reload
        15. Validate the date calendar
        16. Apply the required filter
        17. Download the credit note
           Automated by: Ranveer Singh Sankhala
        """

        credit_notes_section = Credit_Notes(driver=self.driver)
        time.sleep(.2)


        credit_notes_section.Click_Credit_Notes()
        time.sleep(.2)
        credit_notes_section.Add_Credit_Note()
        time.sleep(.2)
        credit_notes_section.Select_Customer_for_Credit_Note()
        time.sleep(.2)
        credit_notes_section.Invoice_ref()
        time.sleep(.2)
        credit_notes_section.Add_Attachment()
        time.sleep(.2)
        credit_notes_section.Enter_Discount()
        time.sleep(.2)
        credit_notes_section.Click_Enter_Notes()
        time.sleep(.3)
        credit_notes_section.Enter_Notes()
        time.sleep(.2)
        credit_notes_section.Save_Credit_Notes()
        time.sleep(.2)
        # credit_notes_section.Paid_From()
        # time.sleep(.2)
        # credit_notes_section.Save_Credit_Notes()
        # time.sleep(.2)
        # credit_notes_section.Paid_From()
        # time.sleep(.2)
        credit_notes_section.Click_Save_Button()
        time.sleep(.2)

        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        credit_notes_section.Enter_Search()
        time.sleep(.5)
        credit_notes_section.Remove_Search()
        time.sleep(.2)
        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        credit_notes_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        credit_notes_section.Change_Date_Calendar()
        time.sleep(1)
        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        credit_notes_section.Select_Filter()
        time.sleep(.2)
        # credit_notes_section.Hide_Reports()
        # time.sleep(.2)
        # credit_notes_section.Change_Pagination()
        # credit_notes_section.wait_for_loader_to_disappear()
        # time.sleep(.2)

        credit_notes_section.Download_Invoice()
        time.sleep(2)
        credit_notes_section.Refresh_Page()
        time.sleep(.2)
        credit_notes_section.wait_for_loader_to_disappear()

        print(
            "Credit Note workflow completed successfully: "
            "credit note created, searched, filtered, and downloaded."
        )



# ----------------------------------------Purchase Supplier-----------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Purchases >> Suppliers >> Add Supplier"
    )
    @pytest.mark.description(
        "Open the Suppliers section, enter supplier, billing, contact, "
        "VAT and bank details, add project tags and an attachment, "
        "and save the new supplier."
    )
    def test_10_complete_add_supplier_workflow(self):
        """
        Complete Add Supplier workflow:

        1. Open the Purchases section
        2. Open the Suppliers section
        3. Click Add Supplier
        4. Enter the supplier name

        Billing address:
        5. Open the Billing Address section
        6. Enter the building information
        7. Enter the street
        8. Enter the city
        9. Enter the county
        10. Select the country
        11. Enter the postcode

        Contact details:
        12. Open the Contact Person section
        13. Enter the first name
        14. Enter the remaining contact name
        15. Enter the contact number
        16. Enter the email address

        Tax and bank details:
        17. Enter the account name
        18. Select the VAT option
        19. Enter the VAT number
        20. Enter the EORI number
        21. Enter the sort code
        22. Enter the account number

        Additional details:
        23. Add project tags
        24. Add an attachment
        25. Save the supplier
        26. Verify that the supplier was created successfully.
          Automated by: Ranveer Singh Sankhala
        """
        client_section = Add_Supplier(driver=self.driver)
        time.sleep(.2)


        client_section.Click_Purchase()
        time.sleep(.2)
#
        client_section.Select_Suppliers_Section()
        time.sleep(.2)

        client_section.Click_On_Add_Suppliers()
        time.sleep(.2)

        client_section.Enter_Suppliers_Name()
        time.sleep(.2)
        client_section.Click_Billing_Field()
        time.sleep(.2)
        client_section.Enter_Building()
        time.sleep(.2)
        client_section.Enter_Street()
        time.sleep(.2)
        client_section.Enter_City()
        time.sleep(.2)
        client_section.Enter_County()
        time.sleep(.2)
        client_section.Select_Country()
        time.sleep(.2)
        client_section.Enter_Postcode()
        time.sleep(.2)
        client_section.Click_Contact_Person()
        time.sleep(.2)

        client_section.First_Name()
        time.sleep(.2)
        client_section.Enter_Name()
        time.sleep(.2)
        client_section.Enter_Contact_Number()
        time.sleep(.2)
        client_section.Enter_Mail()
        time.sleep(.2)
        client_section.Account_name()
        time.sleep(.2)
        client_section.Select_Vat()
        time.sleep(.2)
        client_section.Enter_Vat()
        time.sleep(.2)
        client_section.Enter_EORI()
        time.sleep(.2)
        client_section.Sort_Code()
        time.sleep(.2)
        client_section.Account_Number()
        time.sleep(.2)
        client_section.Project_tags()
        time.sleep(.2)
        client_section.Add_Attachment()
        time.sleep(.2)
        client_section.Save_Suppliers()
        time.sleep(.2)
        client_section.Refresh_Page()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()

        print(
            "Add Supplier workflow completed successfully: "
            "supplier details entered and saved."
        )




#---------------------------------------PO------------------------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Inputs >> Purchases >> Purchase Orders"
    )
    @pytest.mark.description(
        "Select a company, open the Purchase Orders section, create a "
        "purchase order with contact, attachment, item, discount and "
        "notes, and save the purchase order."
    )
    def test_11_complete_purchase_order_workflow(self):

        """
        Purchase Order creation workflow:

        1. Open the Purchase Orders section
        2. Click Add Purchase Order
        3. Select the supplier or contact name
        4. Add an attachment
        5. Select a purchase item
        6. Enter the discount
        7. Open the notes field
        8. Enter purchase order notes
        9. Save the purchase order
        10. Verify that the purchase order was created successfully.
           Automated by: Ranveer Singh Sankhala
        """
        client_section = Purchase_Order(driver=self.driver)
        time.sleep(.2)
        client_section.Purchase_Order()
        time.sleep(.5)
        client_section.Click_Purchase_Order()
        time.sleep(.2)
        client_section.Select_Contact_Name()
        time.sleep(.2)
        client_section.Add_Attachment()
        time.sleep(.2)
        client_section.Click_Item_For_Invoice()
        time.sleep(.2)
        client_section.Enter_Discount()
        time.sleep(.2)
        client_section.Click_Enter_Notes()
        time.sleep(.2)
        client_section.Enter_Notes()
        time.sleep(.2)
        client_section.Save_PO()
        time.sleep(.2)
        client_section.Refresh_Page()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()

        print(
            "Purchase Order workflow completed successfully: "
            "purchase order details entered and saved."
        )

#-----------------------------------------------------------------------------------------------------------------------


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Inputs >> Purchases >> Add Invoice"
    )
    @pytest.mark.description(
        "Select a company, open the Purchases section, create a purchase "
        "invoice with supplier, attachment, item, discount and amount "
        "details, and save the invoice."
    )
    def test_12_complete_purchase_invoice_workflow(self):
        """
        Complete Purchase Invoice workflow:

        1. Search for a company
        2. Select the company
        3. Open the Client Input section
        4. Open the Purchases section
        5. Click Add Invoice
        6. Select the supplier or customer
        7. Add an attachment
        8. Enter the discount
        9. Select a purchase item
        10. Enter the purchase amount
        11. Save the purchase invoice
        12. Wait for invoice creation to complete
        13. Verify that the purchase invoice was created successfully.
           Automated by: Ranveer Singh Sankhala
        """

        client_section = ClientPurchase(driver=self.driver)
        time.sleep(.2)


        client_section.Click_Purchases()
        time.sleep(.5)
        time.sleep(.2)

        client_section.Add_Invoice()
        time.sleep(.2)
        client_section.Select_Customer()
        time.sleep(.2)

        client_section.Add_Attachment()
        time.sleep(.2)
        client_section.Enter_Discount()
        time.sleep(.2)
        client_section.Select_item_purchase()
        time.sleep(.5)
        client_section.Enter_amount()
        time.sleep(2)
        client_section.Save_Services()
        time.sleep(.2)
        client_section.Refresh_Page()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()

        print(
            "Purchase Invoice workflow completed successfully: "
            "invoice details entered and saved."
        )

#----------------------------------------------Payments-------------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Inputs >> Purchases >> Payments"
    )
    @pytest.mark.description(
        "Select a company, open the Purchase Payments section, create "
        "a supplier payment by selecting the supplier and bank account, "
        "enter the payment amount, and save the payment."
    )
    def test_13_complete_purchase_payment_workflow(self):
        """
        Complete Purchase Payment workflow:

        1. Search for a company
        2. Select the company
        3. Open the Client Input section
        4. Open the Purchases section
        5. Open the Payments section
        6. Click Add Payment
        7. Select the supplier to be paid
        8. Select the payment account
        9. Enter the payment amount
        10. Save the payment
        11. Wait for the payment operation to complete
        12. Verify that the payment was created successfully.
           Automated by: Ranveer Singh Sankhala
        """

        client_section = Purchase_Payment(driver=self.driver)
        time.sleep(.2)

        client_section.Payment_Section()
        client_section.Click_Payment()

        client_section.Paid_To_Supplier_Main()
        client_section.Select_Account()
        client_section.Enter_Amount()
        client_section.Save_payment()

        client_section.wait_for_loader_to_disappear()


        client_section.Refresh_Page()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        print(
            "Purchase Payment workflow completed successfully: "
            "supplier payment details entered and saved."
        )


    #----------------------------------------purchase_credit_note-------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> "
        "Client >> Inputs >> Purchases >> Credit Notes"
    )
    @pytest.mark.description(
        "Select a company, open the Purchase Credit Notes section, "
        "create a credit note with supplier, invoice reference, "
        "attachment, discount and notes, and save the credit note."
    )

    def test_14_complete_purchase_credit_note_workflow(self):
        """
        Complete Purchase Credit Note workflow:

        1. Search for a company
        2. Select the company
        3. Open the Client Input section
        4. Open the Purchases section
        5. Open the Credit Notes section
        6. Click Add Credit Note
        7. Select the supplier
        8. Select or enter the invoice reference
        9. Add an attachment
        10. Enter the discount
        11. Open the notes field
        12. Enter the credit note details
        13. Save the credit note information
        14. Click the final Save button
        15. Wait for the save operation to complete
        16. Verify that the purchase credit note was created successfully.
          Automated by: Ranveer Singh Sankhala
        """

        credit_note_page = Purchase_CN(driver=self.driver)

        credit_note_page.Click_Credit_Notes()
        time.sleep(.2)
        credit_note_page.Add_Credit_Note()
        time.sleep(.2)
        credit_note_page.Select_Suppiler_for_Credit_Note()
        time.sleep(.2)
        credit_note_page.Invoice_ref()
        time.sleep(.2)
        credit_note_page.Add_Attachment()
        time.sleep(.2)
        credit_note_page.Enter_Discount()
        time.sleep(.2)
        credit_note_page.Click_Enter_Notes()
        time.sleep(.2)
        credit_note_page.Enter_Notes()
        time.sleep(.2)

        credit_note_page.Save_Credit_Notes()
        time.sleep(.2)
        credit_note_page.Click_Save_Button()
        time.sleep(.2)
        credit_note_page.Refresh_Page()

        time.sleep(.2)


        credit_note_page.wait_for_loader_to_disappear()

        print(
            "Purchase Credit Note workflow completed successfully: "
            "credit note details were entered and saved."
        )

#
#
# #------------------------------------------Expense Claim Flow >> Add user-----------------------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Expense Claims >> Users >> Add User"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Expense Claims Users section, "
#         "create a new user with personal and NI details, and save "
#
#     )
#     def test_15_complete_add_expense_claim_user_workflow(self):
#         """
#         Complete Add Expense Claim User workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Expense Claims section
#         5. Open the Users section
#         6. Click Add User
#         7. Open the name field
#         8. Select the user's title
#         9. Enter the user's name
#         10. Enter the National Insurance number
#         11. Save the user
#         12. Wait for the save operation to complete
#         13. Verify that the user was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#         expense_claims_page = User(
#             driver=self.driver
#         )
#         time.sleep(.2)
#
#         expense_claims_page.Click_Expense_Claims()
#         time.sleep(.5)
#
#         expense_claims_page.User_Section()
#         time.sleep(.2)
#         expense_claims_page.Click_Add_User()
#         time.sleep(.2)
#         expense_claims_page.Click_Name_Field()
#         time.sleep(.2)
#         expense_claims_page.Select_Title()
#         time.sleep(.2)
#         expense_claims_page.Enter_name()
#         time.sleep(.2)
#
#         expense_claims_page.Enter_Ni_Number()
#         time.sleep(.2)
#         expense_claims_page.Save_User()
#         time.sleep(.2)
#         expense_claims_page.Refresh_Page()
#         time.sleep(.2)
#         expense_claims_page.wait_for_loader_to_disappear()
#
#
#         print(
#             "Expense Claim User workflow completed successfully: "
#             "the new user was created and saved. "
#
#         )
#
#
#
#     #------------------------------------------Add Expense Claim--------------------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Expense Claims >> Add Expense Claim"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Expense Claims section, create "
#         "a new expense claim with claimant, bill, account, amount, "
#         "VAT and attachment details, and save the claim. "
#
#     )
#     def test_16_complete_expense_claim_workflow(self):
#         """
#         Complete Expense Claim workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Expense Claims section
#         5. Click Add Expense Claim
#         6. Select the director or claimant
#         7. Enter the claim remarks
#         8. Add an attachment
#         9. Enter the bill number
#         10. Enter the expense description
#         11. Select the expense account
#         12. Enter the base amount
#         13. Select the VAT option
#         14. Save the expense claim
#         15. Wait for the save operation to complete
#         16. Verify that the expense claim was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         client_section = Expenseclaims(driver=self.driver)
#         time.sleep(.2)
#         client_section.Click_Expense_Claims_Tab()
#         time.sleep(.2)
#         client_section.Click_Expense_Claims_Button()
#         time.sleep(.2)
#         client_section.Select_Directors()
#         time.sleep(.2)
#         client_section.Enter_Remark()
#         time.sleep(.2)
#         client_section.Add_Attachment()
#         time.sleep(.2)
#
#         client_section.Enter_Bill_No()
#         time.sleep(.2)
#         client_section.Enter_Description()
#         time.sleep(.2)
#         client_section.Select_Account()
#         time.sleep(.2)
#         client_section.Base_Amount()
#         time.sleep(.2)
#         client_section.Select_Vat()
#         time.sleep(5)
#         client_section.Save_Expense()
#         time.sleep(.2)
#         client_section.Refresh_Page()
#         time.sleep(.1)
#         client_section.wait_for_loader_to_disappear()
#
#         print(
#             "Expense Claim workflow completed successfully: "
#             "the expense claim was created and saved. "
#
#         )
#
# #-----------------------------------------------------------------------------------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Expense Claims >> Mileage >> Add Mileage"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Mileage section, create a mileage "
#         "claim with claimant, journey, engine, distance and rate details, "
#         "and save the claim."
#     )
#     def test_17_complete_mileage_claim_workflow(self):
#         """
#         Complete Mileage Claim workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Expense Claims section
#         5. Open the Mileage section
#         6. Click Add Mileage
#         7. Select the director or claimant
#         8. Enter the mileage claim remarks
#         9. Select the engine type
#         10. Enter the journey description
#         11. Enter the mileage or distance
#         12. Select the mileage rate
#         13. Save the mileage claim
#         14. Wait for the save operation to complete
#         15. Verify that the mileage claim was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         client_section = Mileage(driver=self.driver)
#         time.sleep(.2)
#         client_section.Mileages_Section()
#         time.sleep(.2)
#         client_section.Click_Mileages()
#         time.sleep(.2)
#         client_section.Select_Directors()
#         time.sleep(.2)
#         client_section.Enter_Remark_Mileages()
#         time.sleep(.2)
#         client_section.Engine_Type()
#         time.sleep(.2)
#         client_section.Enter_Description_Mileage()
#         time.sleep(.2)
#         client_section.Mileage()
#         time.sleep(.2)
#         client_section.Select_Rate()
#         time.sleep(.2)
#         client_section.Save_Mileage()
#         time.sleep(.2)
#         client_section.Refresh_Page()
#         time.sleep(.2)
#         client_section.wait_for_loader_to_disappear()
#
#         print(
#             "Mileage Claim workflow completed successfully: "
#             "the mileage claim was created and saved. "
#
#         )
#
#
# #-----------------------------------------------------------------------------------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Expense Claims >> Reimbursements"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Reimbursements section, create a "
#         "reimbursement by selecting the recipient and payment account, "
#         "enter the amount, and save it. "
#
#     )
#     def test_18_complete_reimbursement_workflow(self):
#         """
#         Complete Reimbursement workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Expense Claims section
#         5. Open the Reimbursements section
#         6. Click Add Reimbursement
#         7. Select the person to reimburse
#         8. Select the reimbursement payment account
#         9. Enter the reimbursement amount
#         10. Save the reimbursement
#         11. Wait for the save operation to complete
#         12. Verify that the reimbursement was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         client_section = Reimbursement(driver=self.driver)
#         time.sleep(.2)
#
#
#
#         client_section.Reimbursed_Section()
#         time.sleep(.2)
#         client_section.Click_Reimbursed()
#         time.sleep(.2)
#         client_section.Reimbursed_to()
#         time.sleep(.2)
#         client_section.Reimbursed_Account()
#         time.sleep(.2)
#         client_section.Enter_Amount()
#         time.sleep(.2)
#         # client_section.Enter_Notes()
#         # time.sleep(.2)
#         client_section.Save_Reimbursement()
#         time.sleep(.2)
#         client_section.Refresh_Page()
#         time.sleep(.2)
#
#         client_section.wait_for_loader_to_disappear()
#
#         print(
#             "Reimbursement workflow completed successfully: "
#             "the reimbursement was created and saved. "
#
#         )
#
#
#
# #-----------------------------------------------Expense Claims >> Refunds-----------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Expense Claims >> Refunds"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Refunds section, create a refund "
#         "by selecting the refund source and account, and save it. "
#
#     )
#     def test_19_complete_refund_workflow(self):
#         """
#         Complete Refund workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Expense Claims section
#         5. Open the Refunds section
#         6. Click Add Refund
#         7. Select the person or source providing the refund
#         8. Select the account receiving the refund
#         9. Save the refund
#         10. Wait for the save operation to complete
#         11. Verify that the refund was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#         client_section = Refund(driver=self.driver)
#         time.sleep(.2)
#
#
#
#         client_section.Refunds_Section()
#         time.sleep(.2)
#         client_section.Click_Refunds()
#         time.sleep(.2)
#         client_section.Refund_from()
#         time.sleep(.2)
#         client_section.Select_Account()
#         time.sleep(.2)
#         client_section.Save_Refund()
#         time.sleep(.2)
#         client_section.Refresh_Page()
#         client_section.wait_for_loader_to_disappear()
#
#         print(
#             "Refund workflow completed successfully: "
#             "the refund was created and saved. "
#         )
#
# #     #-------------------------------------------------------------------------------------------------------------------
#
#
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Assets >> Add Asset"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Assets section, create a new asset "
#         "with purchase, account, supplier and rate details, and save it."
#     )
#     def test_19_complete_add_asset_workflow(self):
#         """
#         Complete Add Asset workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Assets section
#         5. Click Add Asset
#         6. Enter the asset name
#         7. Enter the purchase details
#         8. Select the asset account
#         9. Select the supplier
#         10. Enter the applicable rate
#         11. Save the asset
#         12. Wait for the save operation to complete
#         13. Verify that the asset was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         asset_page = Asset(driver=self.driver)
#
#
#
#         asset_page.Click_Asset()
#         time.sleep(0.2)
#
#         asset_page.Click_Add_Assets()
#         time.sleep(0.2)
#
#         asset_page.Asset_Name()
#         time.sleep(0.2)
#
#         asset_page.Purchase()
#         time.sleep(0.2)
#
#         asset_page.Select_Account()
#         time.sleep(0.2)
#
#         asset_page.Select_Supplier()
#         time.sleep(0.2)
#
#         asset_page.Enter_Rate()
#         time.sleep(0.2)
#
#         asset_page.Save_Asset()
#         time.sleep(.2)
#         asset_page.Refresh_Page()
#         asset_page.wait_for_loader_to_disappear()
#
#         print(
#             "Add Asset workflow completed successfully: "
#             "asset details were entered and saved."
#         )
#
#
#
#
#
# #    #--------------------------------------------------------------------------------------------------------------------
# #
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Assets >> Disposed Assets"
#     )
#     @pytest.mark.description(
#         "Open the Disposed Assets section, dispose of an existing asset "
#         "by entering the sales proceeds, payment method and customer "
#         "details, and save the disposal."
#     )
#     def test_20_complete_dispose_asset_workflow(self):
#         """
#         Complete Asset Disposal workflow:
#
#         1. Open the Disposed Assets section
#         2. Click Add Disposed Asset
#         3. Select the asset to be disposed
#         4. Enter the sales proceeds
#         5. Select the payment method
#         6. Select the customer
#         7. Save the asset disposal
#         8. Wait for the save operation to complete
#         9. Verify that the asset was disposed successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         asset_page = Asset(driver=self.driver)
#
#         asset_page.Disposed()
#         time.sleep(0.2)
#
#         asset_page.Add_Disposed()
#         time.sleep(0.2)
#
#         asset_page.Select_Asset()
#         time.sleep(0.2)
#
#         asset_page.Sales_proceeds()
#         time.sleep(0.2)
#
#         asset_page.Payment_Method()
#         time.sleep(0.2)
#
#         asset_page.Customer()
#         time.sleep(0.2)
#
#         asset_page.Save_Disposed()
#         time.sleep(.2)
#         asset_page.Refresh_Page()
#         time.sleep(.2)
#         asset_page.wait_for_loader_to_disappear()
#
#         print(
#             "Asset Disposal workflow completed successfully: "
#             "the selected asset was disposed and saved."
#         )
#
#
#
# #     #--------------------------------------------Journal--------------------------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Journals >> Add Journal"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Journals section, create a balanced "
#         "journal entry by selecting debit and credit accounts, enter the "
#         "journal reference and values, and save the journal."
#     )
#     def test_21_complete_add_journal_workflow(self):
#         """
#         Complete Add Journal workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Journals section
#         5. Click Add Journal
#         6. Enter the journal reference
#         7. Select the debit account
#         8. Enter the debit amount
#         9. Select the credit account
#         10. Enter the credit amount
#         11. Confirm that total debit equals total credit
#         12. Save the journal
#         13. Wait for the save operation to complete
#         14. Verify that the journal was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         journal_page = Journals(driver=self.driver)
#
#
#
#         journal_page.Click_Journals()
#         time.sleep(0.2)
#
#         journal_page.Click_Journals_Button()
#         time.sleep(0.2)
#
#         journal_page.Journal_Reference()
#         time.sleep(0.2)
#
#         # Debit entry
#         journal_page.Select_Account()
#         time.sleep(0.5)
#
#         journal_page.Enter_Value_IN_Debit()
#         time.sleep(0.5)
#
#         # Credit entry
#         journal_page.Select_Account()
#         time.sleep(0.2)
#
#         journal_page.Enter_Value_IN_Credit()
#         time.sleep(0.3)
#
#         journal_page.Save_Journal()
#         time.sleep(.2)
#         journal_page.Refresh_Page()
#
#         journal_page.wait_for_loader_to_disappear()
#
#         print(
#             "Journal workflow completed successfully: "
#             "balanced debit and credit entries were created and saved."
#         )
#
#
# # #-----------------------------------------------------------------------------------------------------------------------
#
#     @pytest.mark.navigation(
#         "Login >> Admin Dashboard >> Bookkeeping >> "
#         "Client >> Inputs >> Dividends >> Add Dividend"
#     )
#     @pytest.mark.description(
#         "Select a company, open the Dividends section, create a new "
#         "dividend by selecting the authorised director and dividend type, "
#         "enter the dividend per share and payment date, and save it."
#     )
#     def test_22_complete_add_dividend_workflow(self):
#         """
#         Complete Add Dividend workflow:
#
#         1. Search for a company
#         2. Select the company
#         3. Open the Client Input section
#         4. Open the Dividends section
#         5. Click Add Dividend
#         6. Select the authorised director
#         7. Select the dividend type
#         8. Select the share class, if applicable
#         9. Enter the dividend amount per share
#         10. Enter the dividend payment date
#         11. Save the dividend details
#         12. Confirm the final save operation
#         13. Wait for processing to complete
#         14. Verify that the dividend was created successfully
#
#         Automated by: Ranveer Singh Sankhala
#         """
#
#         dividend_page = Dividend(driver=self.driver)
#
#
#         dividend_page.Dividends_Section()
#         time.sleep(0.2)
#
#         dividend_page.Click_Dividends()
#         time.sleep(0.2)
#
#         dividend_page.Authorised_director()
#         time.sleep(0.2)
#
#         dividend_page.Select_Type()
#         time.sleep(0.2)
#
#         # Enable this step when a share class is required.
#         # dividend_page.Select_Class()
#         # time.sleep(0.2)
#
#         dividend_page.Dividend_Per_Share()
#         time.sleep(0.2)
#
#         dividend_page.Enter_Payment_Date()
#         time.sleep(0.2)
#
#         dividend_page.Save_Asset()
#         time.sleep(0.2)
#
#         dividend_page.Save()
#         dividend_page.wait_for_loader_to_disappear()
#
#         print(
#             "Dividend workflow completed successfully: "
#             "dividend details were entered and saved."
#         )
#
#
#
#
#
#
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#         This method runs once after all test methods finish.
#         """
#
#         if hasattr(cls, "driver"):
#             cls.driver.quit()
#
#         print("Browser closed successfully.")
#
#
# if __name__ == "__main__":
#     unittest.main()
#
#
