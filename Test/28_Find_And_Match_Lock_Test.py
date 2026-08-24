import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from Pages.Client_SellPage import ClientSell
from Pages.Credit_NotesPage import Credit_Notes
from Pages.ExpenseclaimsPage import Expenseclaims
from Pages.PurchasePage import ClientPurchase
from Pages.Find_And_Match_Lock_Page import Find_And_Match_Lock

from configReader import ConfigReader
from Pages.LoginPage import loginPage


class Login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """
        This method runs only once before all test methods
        inside this class.

        preconditions -
        1. Add User
        2. Add item
        3. Supplier
        4. Customer
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
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Bank"
    )
    @pytest.mark.description(
        " Select company, create a bank account and add manual transactions"
    )


    def test_28_01_Add_New_Current_Bank_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Expense claims
        4. Create claim
        5. Save claim-- By: - Ranveer
        """

        client_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)


        client_section.Select_Search()
        time.sleep(0.5)

        client_section.Enter_Company()
        time.sleep(0.5)

        client_section.Click_Company()
        time.sleep(1)

        print("Company selected successfully.")


        # -------------------------------------------------------
        # Step 2: Open Sales section
        # -------------------------------------------------------



        client_section.Banking_Section()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Account()
        time.sleep(.2)

        client_section.Select_Bank()
        time.sleep(.2)

        client_section.Enter_Account_no()
        time.sleep(.2)
        client_section.Sort_Code()
        time.sleep(.2)
        client_section.Click_Primary_Account()
        time.sleep(.2)

        client_section.Save_Banking()
        time.sleep(1)

        client_section.Click_Added_Bank()
        time.sleep(.2)

        # client_section.Click_Manual()
        # time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Import()
        time.sleep(.2)
        # client_section.Click_Templet()
        # time.sleep(.2)
        client_section.Click_Upload()
        time.sleep(.2)

        client_section.Upload_Import()
        time.sleep(.2)
        client_section.Click_Next()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        # client_section.Add_Manual_Transaction()
        # time.sleep(1)
        # for i in range(3):
        #     print(f"Money Out Transaction {i + 1}")
        #
        #     client_section.Add_Manual_Transaction()
        #     time.sleep(1)
        #
        #     client_section.Enter_Date()
        #     time.sleep(1)
        #
        #     client_section.Enter_Description()
        #     time.sleep(1)
        #
        #     client_section.Enter_Money_Out()
        #     time.sleep(1)
        #
        #     client_section.Click_Save_Manual_Transaction()
        #
        #     client_section.wait_for_loader_to_disappear()
        #     time.sleep(0.2)
        #
        # # ---------------- Money In: 3 entries ----------------
        # for i in range(3):
        #     print(f"Money In Transaction {i + 1}")
        #
        #     client_section.Add_Manual_Transaction()
        #     time.sleep(1)
        #
        #     client_section.Enter_Date()
        #     time.sleep(1)
        #
        #     client_section.Enter_Description()
        #     time.sleep(1)
        #
        #     client_section.Enter_Money_In()
        #     time.sleep(1)
        #
        #     client_section.Click_Save_Manual_Transaction()
        #
        #     client_section.wait_for_loader_to_disappear()
        #     time.sleep(0.2)




    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >> Sale"
    )
    @pytest.mark.description(
        "Select company and create a new sales invoice"
    )



    def test_28_02_Add_New_Sale_Invoice_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Sales
        4. Create invoice
        5. Save invoice
        """

        client_sell_page = Find_And_Match_Lock(
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

        client_sell_page.Change_Quantity()
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
        client_sell_page.Select_Account_For_Sell()
        time.sleep(.2)
        client_sell_page.Click_Save()
        time.sleep(.2)
        print("Receipt Created Successfully.....")

    #-------------------------------------------------------------------------------------------------------------------

    @pytest.mark.navigation(
            "Login >> Admin Dashboard >> Bookkeeping >> Input >> CN"
        )
    @pytest.mark.description(
            "Create and save a new credit note"
        )

    def test_28_03_Add_New_Credit_Note_Find_And_match_with_lock(self):
        """
            Complete dependent workflow:
            1. Search company
            2. Select company
            3. Open Sales
            4. Create invoice
            5. Save invoice
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
        credit_notes_section.Change_CRN_Quantity()
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
        time.sleep(.5)

        credit_notes_section.Select_Account_CRN()
        time.sleep(.2)

        credit_notes_section.Click_Save_Button()
        time.sleep(.2)
        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        credit_notes_section.wait_for_page_ready()
        time.sleep(.2)


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Purchase Order"
    )
    @pytest.mark.description(
        "Select company and create a new Purchase invoice"
    )


    def test_28_04_Add_New_Purchase_Invoice_Find_And_match_with_lock(self):
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
        # purchase_sell_page.Enter_Discount()
        # time.sleep(.2)
        # client_section.Click_Enter_Notes()
        # time.sleep(.2)
        # client_section.Enter_Notes()
        # time.sleep(.2)

        purchase_sell_page.Select_item_purchase()
        time.sleep(.5)
        purchase_sell_page.Change_Quantity()
        time.sleep(.5)
        purchase_sell_page.Enter_amount()
        time.sleep(2)
        purchase_sell_page.Save_Services()
        time.sleep(.2)


        purchase_sell_page.wait_for_loader_to_disappear()
        time.sleep(0.5)
        purchase_sell_page.Click_Pound_Icon()
        time.sleep(.2)
        purchase_sell_page.Select_Account_Payment_lock()
        time.sleep(.2)
        purchase_sell_page.Enter_Amount()
        time.sleep(.2)
        purchase_sell_page.Click_Setting_Icon()
        time.sleep(.2)
        purchase_sell_page.Enter_Cash_Discount()
        time.sleep(.2)
        purchase_sell_page.Click_Green_Tick()
        time.sleep(.2)
        purchase_sell_page.Save_Services()
        time.sleep(.2)


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Expense claims"
    )
    @pytest.mark.description(
        "Select company and create a new Expense claims"
    )


    def test_28_05_Add_New_Expense_Claims_Find_And_match_with_lock(self):
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


        #---------------------------------------------------------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> go for Client >> expense-claims >> Reimbursements"
    )
    @pytest.mark.description(
        "Select company and create a new Reimbursements"
    )


    def test_28_06_Add_New_Reimbursement_Claims_Find_And_match_with_lock(self):
        """
        Complete dependent workflow:
        1. Search company
        2. Select company
        3. Open Expense claims
        4. CreateReimbursements
        5. Save Reimbursements- By: - Ranveer
        """
        client_section = Find_And_Match_Lock(
            driver=self.driver
        )
        time.sleep(.2)
        client_section.Reimbursed_Section()
        time.sleep(.2)
        client_section.Click_Reimbursed()
        time.sleep(.2)
        client_section.Reimbursed_to()
        time.sleep(.2)
        client_section.Reimbursed_Account()
        time.sleep(.2)
        client_section.Enter_Amount()
        time.sleep(.2)
        # client_section.Enter_Notes()
        # time.sleep(.2)
        client_section.Save_Reimbursement()
        time.sleep(.2)


        client_section.Refunds_Section()
        time.sleep(.2)
        client_section.Click_Refunds()
        time.sleep(.2)
        client_section.Refund_from()
        time.sleep(.2)
        client_section.Select_Account_Refund()
        time.sleep(.2)
        client_section.Save_Refund()
        time.sleep(.2)


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Bank >> find and match"
    )
    @pytest.mark.description(
        " Select company, select created bank account and find and match the transaction "
    )

    def test_28_07_Select_Current_Bank_Find_And_match_with_lock(self):

        client_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)
        client_section.Banking_Section()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Adde_Bank_Account()
        time.sleep(.2)

        # #----------1st des--------------------------------

        client_section.Click_Receipt_with_Bank_Charge()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_In()
        time.sleep(.2)
        client_section.Select_Receipts()
        time.sleep(.2)

        client_section.Select_Settle()
        time.sleep(.2)
        client_section.Click_Match()
        time.sleep(.2)

        # # ----------2nd des--------------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Click_Sales_Return()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_Out()
        time.sleep(.2)

        client_section.Select_Receipts()
        time.sleep(.2)
        client_section.Click_Match()
        time.sleep(.2)

      #--------------------------3rd Dec--------------------------------------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Click_Payment_Find_Match()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.3)
        client_section.Click_Match()
        time.sleep(.3)

        #----------------4th payment due --------------------------------------------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section. Click_Payment_Due()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_Out_2nd()
        time.sleep(.2)
        client_section.Select_Receipts()
        time.sleep(.2)
        client_section.Click_Match()
        time.sleep(.2)

    #---------------------------5th----------------------------------------------------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Reimbursement()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_Out_3nd()
        time.sleep(.2)
        client_section.Select_Receipts()
        time.sleep(.2)
        # client_section.Select_Settle_Reimbursement()
        # time.sleep(.2)
        client_section.Click_Match()
        time.sleep(.2)

    #---------------------------6th-----------------------------------------------------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Refund()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_Out_6th()
        time.sleep(.2)
        client_section.Select_Receipts()
        time.sleep(.2)
        client_section.Click_Match()
        time.sleep(.2)

    #-----------------------------------lock invoice-------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Invoice >> Verify the lock is showing or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in input module."
    )
    def test_28_08_lock_verification_invoice(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open Sales
                4. verify that lock is showing or not

                """

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

        client_sell_page.Click_On_Lock_Button()
        time.sleep(.2)
        client_sell_page.Click_On_Close_Icon()
        time.sleep(.2)


#--------------------------------------------------lock Credit Note---------------------------------------------------------------

    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Credit Note >> Verify the lock is showing or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in input module."
    )
    def test_28_09_lock_verification_credit_note(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open credit note
                4. verify that lock is showing or not

                """

        credit_notes_section = Credit_Notes(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)

        credit_notes_section.Click_Credit_Notes()
        time.sleep(.2)
        time.sleep(0.5)

        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(0.5)

        print("Sales section opened successfully.")

        credit_notes_section.Click_On_Lock_Button_Credit()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)






    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Receipts >> Verify the lock is showing or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in input module."
    )
    def test_28_10_lock_verification_receipts(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open Receipts
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)

        credit_notes_section.Click_Receipts()
        time.sleep(.2)
        time.sleep(0.5)

        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(0.5)

        print("Receipts section opened successfully for verify lock.")

        credit_notes_section.Click_On_Lock_Button_Receipts()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)

    # ------------------------------------------------------------------------------------------------------------------------


    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>purchases >> Verify the lock is showing or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in input module.")





    def test_28_11_lock_verification_purchases(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open Purchases
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)

        credit_notes_section.Click_Purchases()
        time.sleep(.2)
        time.sleep(0.5)

        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(0.5)

        print("Purchases section opened successfully for verify lock.")



        credit_notes_section.Click_On_Lock_Button_Purchases()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)





    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Purchases >>Payment >>>  Verify the lock is showing or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in input module."
    )


    def test_28_12_lock_verification_payment(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> payment
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)
        credit_notes_section.Click_Payments()
        time.sleep(.2)
        time.sleep(0.5)



        print("Payment section opened successfully for verify lock.")

        credit_notes_section.Click_First_Lock_Payment()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)
        print("Payment section opened successfully and  verify  lock for supplier.")
        # credit_notes_section.Click_Second_Lock_Payment()
        # time.sleep(.2)
        credit_notes_section.Click_Second_Lock_Payment()
        time.sleep(.2)
        print("Payment section opened successfully and  verify  lock.")


    def test_28_13_lock_verification_payment_Expense_claims(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> Expense_claims
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        credit_notes_section.Click_Expense_Claims()
        time.sleep(0.5)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)



        time.sleep(.2)
        time.sleep(0.5)


        print("Expense section opened successfully for verify lock.")

    def test_28_14_lock_verification_payment_Reimbursements(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> Reimbursements
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        credit_notes_section.Reimbursed_Section()
        time.sleep(0.5)

        credit_notes_section.Click_On_Lock_Button_Reimbursed()
        time.sleep(.2)

        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)



        time.sleep(.2)
        time.sleep(0.5)


        print("Expense section opened successfully for verify lock.")


    def test_28_15_lock_verification_payment_Refunds(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> Refunds
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        credit_notes_section.Refunds_Section()
        time.sleep(0.5)

        credit_notes_section.Click_On_Lock_Button_Refund()
        time.sleep(.5)


        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)


        time.sleep(.2)
        time.sleep(0.5)

        print("Refund section opened successfully for verify lock.")



    def test_28_16_Un_Explain_All(self):
        """
                        Complete dependent workflow:
                        1. Search company
                        2. Select company
                        3. Banking >> Add bank
                        4. Un_Explain_All

                        """

        un_explain = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)
        un_explain.Banking_Section()
        time.sleep(.2)

        un_explain.wait_for_loader_to_disappear()
        time.sleep(.2)
        un_explain.Click_Added_bank_for_Unexplain()
        time.sleep(.2)
        un_explain. Click_Explain()
        time.sleep(.2)
        un_explain.Select_All_Explain_Entries()
        time.sleep(.2)
        un_explain.Unexplain_all_checked_transactions()
        time.sleep(.2)
        un_explain.Click_Yes_For_Confirmation()
        time.sleep(.2)

    @pytest.mark.navigation(
            "Login >> Admin Dashboard >> Bookkeeping >> Input >>Invoice >> Verify the value un-lock  or not"
        )
    @pytest.mark.description(
            " Select company, Verify the lock in input module.")

    def test_28_17_Verify_Unlock_in_all_Section(self):
        """
                        Complete dependent workflow:
                        1. Search company
                        2. Select company
                        3. check all module
                        4. check uncheck


                        """
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

        client_sell_page.Click_On_Lock_Button()
        time.sleep(.2)
        client_sell_page.Click_On_Close_Icon()
        time.sleep(.2)



# --------------------------------------------------Check unlock Credit Note---------------------------------------------------------------



    @pytest.mark.navigation(
            "Login >> Admin Dashboard >> Bookkeeping >> Input >>Credit Note >> Verify the Unlock or not"
        )
    @pytest.mark.description(
            " Select company, Verify the lock in input module."
        )
    def test_28_18_Un_lock_verification_credit_note(self):
            """
                    Complete dependent workflow:
                    1. Search company
                    2. Select company
                    3. Open credit note
                    4. verify that un-lock is showing or not

                    """

            credit_notes_section = Credit_Notes(driver=self.driver)
            time.sleep(.2)

            # credit_notes_section.Click_Input()
            # time.sleep(0.5)

            credit_notes_section.Click_Credit_Notes()
            time.sleep(.2)
            time.sleep(0.5)

            credit_notes_section.wait_for_loader_to_disappear()
            time.sleep(0.5)

            print("Sales section opened successfully.")

            credit_notes_section.Click_On_Lock_Button_Credit()
            time.sleep(.2)
            credit_notes_section.Click_On_Close_Icon()
            time.sleep(.2)



    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Receipts >> Verify the Un lock  or not"
    )
    @pytest.mark.description(
        " Select company, Verify the un_lock in receipts module."
    )
    def test_28_19_Un_lock_verification_receipts(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open Receipts
                4. verify that Un-lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)

        credit_notes_section.Click_Receipts()
        time.sleep(.2)
        time.sleep(0.5)

        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(0.5)

        print("Receipts section opened successfully for verify  un-lock.")

        credit_notes_section.Click_On_Lock_Button_Receipts()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)



    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>purchases >> Verify the Un-lock is or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in purchases module.")
    def test_28_20_Un_lock_verification_purchases(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open Purchases
                4. verify that un lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)

        credit_notes_section.Click_Purchases()
        time.sleep(.2)
        time.sleep(0.5)

        credit_notes_section.wait_for_loader_to_disappear()
        time.sleep(0.5)

        print("Purchases section opened successfully for verify  un-lock.")

        credit_notes_section.Click_On_Lock_Button_Purchases()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)



    @pytest.mark.navigation(
        "Login >> Admin Dashboard >> Bookkeeping >> Input >>Purchases >>Payment >>>  Verify the un-lock  or not"
    )
    @pytest.mark.description(
        " Select company, Verify the lock in payment module."
    )
    def test_28_21_Un_lock_verification_payment(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> payment
                4. verify that lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        # credit_notes_section.Click_Input()
        # time.sleep(0.5)
        credit_notes_section.Click_Payments()
        time.sleep(.2)
        time.sleep(0.5)

        print("Payment section opened successfully for verify un-lock.")

        credit_notes_section.Click_First_Lock_Payment()
        time.sleep(.2)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)
        print("Payment section opened successfully and  verify  un-lock for supplier.")
        credit_notes_section.Click_Second_Lock_Payment()
        time.sleep(.2)
        credit_notes_section.Click_Second_Lock_Payment()
        time.sleep(.2)
        print("Payment section opened successfully and  verify   un-lock.")

    def test_28_22_Un_lock_verification_payment_Expense_claims(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> Expense_claims
                4. verify that  un-lock or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        credit_notes_section.Click_Expense_Claims()
        time.sleep(0.5)
        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)

        time.sleep(.2)
        time.sleep(0.5)

        print("Expense section opened successfully for verify  un-lock.")

    def test_28_23_Un_lock_verification_payment_Reimbursements(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> Reimbursements
                4. verify that Un_lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        credit_notes_section.Reimbursed_Section()
        time.sleep(0.5)

        credit_notes_section.Click_On_Lock_Button_Reimbursed()
        time.sleep(.2)

        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)

        time.sleep(.2)
        time.sleep(0.5)

        print("Expense section opened successfully for Un_lock .")

    def test_28_24_Un_lock_verification_payment_Refunds(self):
        """
                Complete dependent workflow:
                1. Search company
                2. Select company
                3. Open purchases >> Refunds
                4. verify that Un_lock is showing or not

                """

        credit_notes_section = Find_And_Match_Lock(driver=self.driver)
        time.sleep(.2)

        credit_notes_section.Refunds_Section()
        time.sleep(0.5)

        credit_notes_section.Click_On_Lock_Button_Refund()
        time.sleep(.5)

        credit_notes_section.Click_On_Close_Icon()
        time.sleep(.2)

        time.sleep(.2)
        time.sleep(0.5)

        print("Refund section opened successfully for verify Un_lock.")


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

