import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.ExpenseclaimsPage import Expenseclaims
from Pages.PurchasePage import ClientPurchase
from VatPage import Vat
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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> Vat and HMRC Authentication")


    def test_15_Expense_claims(self):
        client_section = Vat(driver=self.driver)
        time.sleep(.2)
        client_section.Select_Search()
        time.sleep(5)
        client_section.Enter_Company()
        time.sleep(.2)
        client_section.Click_Company()
        time.sleep(.2)
        time.sleep(3)
        client_section.Click_Input()
        time.sleep(.2)
        client_section. Vat_Return_Section()
        time.sleep(.2)

        client_section.Handle_MTD_Or_Reauthorized()
        time.sleep(.2)



        client_section.Click_Continue()
        time.sleep(.2)
        client_section.Click_HMRC_Online()
        time.sleep(.2)
        client_section.Click_Test_User_Credentials()
        time.sleep(.2)
        client_section.Scroll_Down_Page()
        time.sleep(.2)
        client_section.Click_Radio_Organization()
        time.sleep(.2)
        client_section. Click_Create()
        time.sleep(.2)
        client_section.Get_User_ID()
        time.sleep(.2)
        client_section.Get_User_Pass()
        time.sleep(.2)
        client_section.Get_Vat_Registration_Date()
        time.sleep(.2)
        client_section.Get_Vat_Registration()
        time.sleep(.2)

        user_id = client_section.Get_User_ID()
        pass_id = client_section.Get_User_Pass()
        formatted_date = client_section.Get_Vat_Registration_Date()
        vat_number = client_section.Get_Vat_Registration()


        client_section.Switch_Back_And_Enter_User_ID(user_id)
        time.sleep(.2)

        client_section. Enter_Password(pass_id)
        time.sleep(.2)
        client_section.Click_SignIn_Button()
        time.sleep(.2)
        client_section.Give_Permission()
        time.sleep(.2)



        client_section.Store_Current_Vat_Page_URL()

        client_section.Verify_And_Return_To_Expected_Vat_Page()
        time.sleep(.2)

#------------------------------------------------------HMRC completed---------------------------------------------------

        client_section.Click_Edit()
        time.sleep(.2)
        client_section.Enter_Vat_Registration_Date(formatted_date)
        time.sleep(.2)
        client_section.Enter_Vat_Registration_Number(vat_number)
        time.sleep(.2)
        client_section.Click_Save()
        time.sleep(1)

#------------------------------edit vat details ----------------------------------------------------------------------------


        client_section.Click_VAT_return()
        time.sleep(.2)




        client_section.Select_Obligations()
        time.sleep(.2)
        client_section.Save_Vat()
        time.sleep(.2)

        client_section.Refresh_Page()
        time.sleep(2)

        client_section.Edit_Vat_Return()
        time.sleep(.2)


        client_section. Click_Import()
        time.sleep(1)
        client_section.Send_Button()
        time.sleep(.2)

        client_section.Enter_Reviewer()
        time.sleep(.2)

        remarks = "Please review and approve this VAT return."
        client_section.Enter_Remarks(remarks)
        time.sleep(.2)
        client_section.Add_Attachment()
        time.sleep(.2)
        client_section.Save_Request()
        time.sleep(.2)
        client_section.Click_Review()
        time.sleep(.2)
        client_section.Click_Next()
        time.sleep(.2)
        client_section.Click_Approve()
        time.sleep(.2)
        client_section.Click_Yes()
        time.sleep(.2)
        client_section.E_Sign()
        time.sleep(.2)



        client_section.Send_mail()
        time.sleep(.2)
        client_section.Mail_Form()
        time.sleep(.2)



        client_section.Click_Review_Mail_New_Tab()
        time.sleep(4)

        client_section.Click_Get_OTP()
        time.sleep(.2)
        client_section.Enter_OTP()
        time.sleep(.2)
        client_section.Proceed_Securely()
        time.sleep(.2)
        client_section.Click_Accept()
        time.sleep(.2)
        client_section.Enter_Name_Signature()
        time.sleep(.2)
        client_section.Click_Sing_Button()
        time.sleep(.2)
        client_section.Click_Okay_And_Return_To_Previous_Tab()
        time.sleep(1)
        client_section.Refresh_Page()
        time.sleep(2)
        client_section.Click_Submit()
        time.sleep(.2)
        client_section.Click_Submit()
        time.sleep(.2)
        client_section.Click_Yes()
        time.sleep(.2)
        client_section.Download_Response()
        time.sleep(.2)
        client_section. Click_Cancel_Vat_Submission_Pop_up()
        time.sleep(.2)
        client_section.Click_Back_Button()
        time.sleep(.2)




        #------------------------------------------------------------

        # client_section.Click_for_mail_Send()
        # time.sleep(1)
        # client_section.Send_Mail_Again_Button()
        # time.sleep(.2)
        # client_section.Mail_Form()
        # time.sleep(.2)
        # client_section.Click_for_mail_Send()
        # time.sleep(1)

        #-------------------------------------------------------




        client_section.Three_dot()
        time.sleep(.2)
        client_section.Click_Download_Report()
        time.sleep(.2)




