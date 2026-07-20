import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Detail_Explain_Current_Account_Page import Detail_Explain_Current_Account
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
        time.sleep(0.5)
        loginpage.Click_Bookkeeping()
        time.sleep(0.5)


        if __name__ == "__main__":
            unittest.main()

    @pytest.mark.navigation("Login >> Admin Dashboard >> Bookkeeping >> Client ")
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> click on sell >> Current Account >> Money out")


    def test_25_Go_Client_Sell(self):
        client_section = Detail_Explain_Current_Account(driver=self.driver)
        time.sleep(.2)
        #
        client_section. Select_Search()
        time.sleep(5)
        client_section.Enter_Company()
        time.sleep(.2)
        client_section.Click_Company()
        time.sleep(.2)
        client_section.Click_Input()
        time.sleep(.2)

        client_section.Click_Sales()
        time.sleep(.2)

        client_section.Add_Invoice()
        time.sleep(.2)
        client_section.Select_Customer_Keyboard()
        time.sleep(.2)

        client_section.Add_Attachment()
        time.sleep(.2)

        client_section.Select_item_sale()
        time.sleep(.5)

        client_section.Enter_Discount()
        time.sleep(.3)

        client_section.Click_Save()
        time.sleep(2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(2)


#-----------------------------------------------------------------------------------------------------------------------
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
        time.sleep(2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(2)
#-------------------------------------------------------------------------------------------------------------------------

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

        client_section.Click_Import()
        time.sleep(.2)
        client_section.Click_Templet()
        time.sleep(.2)
        client_section.Click_Upload_File()
        time.sleep(.2)

        client_section.Upload_Import()
        time.sleep(.2)
        client_section.Click_Next()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

#-----------------------------------------------------------------------------------------------------------------------

        client_section.Click_Back_Button()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Add_Manual_Transaction()
        time.sleep(1)
        client_section.Enter_Date()
        time.sleep(1)
        client_section.Enter_Description()
        time.sleep(1)
        client_section.Enter_Money_Out()
        time.sleep(1)
        client_section.Click_Save_Manual_Transaction()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Add_Manual_Transaction()
        time.sleep(1)
        client_section.Enter_Date()
        time.sleep(1)
        client_section.Enter_Description()
        time.sleep(1)
        client_section.Enter_Money_Out()
        time.sleep(1)
        client_section.Click_Save_Manual_Transaction()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Add_Manual_Transaction()
        time.sleep(1)
        client_section.Enter_Date()
        time.sleep(1)
        client_section.Enter_Description()
        time.sleep(1)
        client_section.Enter_Money_Out()
        time.sleep(1)
        client_section.Click_Save_Manual_Transaction()
        time.sleep(.2)


        # ---------------------------------------------------------------------------------------------------------------

        client_section.Money_Out_Value()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_Out()
        time.sleep(1)
        # client_section.Click_Attachment_Icon()
#         # time.sleep(1)
        # client_section.Drag_Drop_File()
#         # time.sleep(1)
        client_section.wait_for_loader_to_disappear()
        time.sleep(1)
        client_section.Select_Claims()
        time.sleep(1)
        client_section.Enter_Allocated_Amount()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(1)
        client_section.Click_Match()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(1)

        # ------------------------------------------------
        #
        client_section.Click_Explain()
        time.sleep(.2)
        client_section.Contact_Name_Dropdown()
        time.sleep(.2)
        client_section.Select_Account_Head()
        time.sleep(.2)
        client_section.Explain_Submit_Button()
        time.sleep(2)

        # -------------------------------------------------

        client_section.Click_Transfer_Section()
        time.sleep(1)
        client_section.Select_Transfer_Account_Dropdown()
        time.sleep(1)
        client_section.Transfer_Submit_Button()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(1)
        client_section.Refresh_Page()
        time.sleep(1)

    # # -------------------------------------Money-In  ------------------------------------------------------------------------
    #
    # @pytest.mark.navigation("Login >> Admin Dashboard >> Bookkeeping >> Client ")
    # @pytest.mark.description(
    #     f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> click on sell >> Current Account >> Money In")
    # def test_26_Go_Client_Sell(self):
    #     client_section = Detail_Explain_Current_Account(driver=self.driver)
#     #     time.sleep(.2)
    #     #
    #     client_section.Select_Search()
#     #     time.sleep(5)
    #     client_section.Enter_Company()
#     #     time.sleep(.2)
    #     client_section.Click_Company()
#     #     time.sleep(.2)

        client_section.Click_Input()
        time.sleep(.2)

        client_section.Click_Sales()
        time.sleep(.2)

        client_section.Add_Invoice()
        time.sleep(.2)
        client_section.Select_Customer_Keyboard()
        time.sleep(.2)

        client_section.Add_Attachment()
        time.sleep(.2)

        client_section.Select_item_sale()
        time.sleep(.5)

        client_section.Enter_Discount()
        time.sleep(.3)

        client_section.Click_Save()
        time.sleep(2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(2)

        # ________________purchases---------------------------------------------

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
        time.sleep(2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(2)

        # ---------------------------------------------------------

        client_section.Banking_Section()
        time.sleep(.2)
        client_section.Click_Added_Bank()
        time.sleep(.2)

        # client_section.wait_for_loader_to_disappear()
#         # time.sleep(.2)
        #
        # client_section.Account()
#         # time.sleep(.2)
        #
        # client_section.Select_Bank()
#         # time.sleep(.2)
        #
        # client_section.Enter_Account_no()
#         # time.sleep(.2)
        # client_section.Sort_Code()
#         # time.sleep(.2)
        # client_section.Click_Primary_Account()
#         # time.sleep(.2)
        #
        # client_section.Save_Banking()
#         # time.sleep(1)
        #
        # client_section.Click_Added_Bank()
#         # time.sleep(.2)
        #


        # client_section.Click_Import()
#         # time.sleep(.2)
        # client_section.Click_Templet()
#         # time.sleep(.2)
        # client_section.Click_Upload_File()
#         # time.sleep(.2)
        #
        # client_section.Upload_Import()
#         # time.sleep(.2)
        # client_section.Click_Next()
#         # time.sleep(.2)
        #
        #
        # client_section.wait_for_loader_to_disappear()
#         # time.sleep(.2)
        #
        # client_section.Click_Back_Button()
#         # time.sleep(.2)
        #
        # client_section.wait_for_loader_to_disappear()
#         # time.sleep(.2)
        # -------------------------------------------------------------------------------------------------------------------

        client_section.Add_Manual_Transaction()
        time.sleep(1)
        client_section.Enter_Date()
        time.sleep(1)
        client_section.Enter_Description()
        time.sleep(1)
        client_section.Enter_Money_In()
        time.sleep(1)
        client_section.Click_Save_Manual_Transaction()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Add_Manual_Transaction()
        time.sleep(1)
        client_section.Enter_Date()
        time.sleep(1)
        client_section.Enter_Description()
        time.sleep(1)
        client_section.Enter_Money_In()
        time.sleep(1)
        client_section.Click_Save_Manual_Transaction()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Add_Manual_Transaction()
        time.sleep(1)
        client_section.Enter_Date()
        time.sleep(1)
        client_section.Enter_Description()
        time.sleep(1)
        client_section.Enter_Money_In()
        time.sleep(1)
        client_section.Click_Save_Manual_Transaction()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Money_Out_Value()
        time.sleep(.2)
        client_section.Click_Find_Match()
        time.sleep(.2)
        client_section.Click_Contact_Dropdown_For_Money_In()
        time.sleep(1)

        client_section.wait_for_loader_to_disappear()
        time.sleep(1)
        client_section.Select_Claims()
        time.sleep(1)
        client_section.Enter_Allocated_Amount()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(1)
        client_section.Click_Match()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(1)

        # ------------------------------------------------

        client_section.Click_Explain()
        time.sleep(.2)
        client_section.Contact_Name_Dropdown()
        time.sleep(.2)
        client_section.Select_Account_Head()
        time.sleep(.2)
        client_section.Explain_Submit_Button()
        time.sleep(2)

        # -------------------------------------------------

        client_section.Click_Transfer_Section()
        time.sleep(1)
        client_section.Select_Transfer_Account_Dropdown()
        time.sleep(1)
        client_section.Transfer_Submit_Button()
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


