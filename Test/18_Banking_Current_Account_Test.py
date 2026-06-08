import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Banking_Current_Account_Page import Banking
from Pages.Dividend_Page import Dividend
from Pages.Journals_Page import Journals
from configReader import ConfigReader
from Pages.LoginPage import loginPage
import pytest


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()

        prefs = {
            "profile.default_content_setting_values.notifications": 1,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }

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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >>Banking >> Add current account")


    def test_23_Banking(self):
        client_section = Banking(driver=self.driver)
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
        client_section.Click_Upload()
        time.sleep(.2)

        client_section. Upload_Import()
        time.sleep(.2)
        client_section.Click_Next()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Click_Checkbox_Single_Element()
        time.sleep(.2)
        client_section.Click_Explain_1st()
        time.sleep(.2)
        client_section.Click_This_Transaction()
        time.sleep(.5)



        client_section.Click_Checkbox_Single_Element()
        time.sleep(.2)
        client_section.Click_Explain_1st()
        time.sleep(1)
        client_section.Click_With_All_Recommendation()
        time.sleep(1)



        client_section.Click_1st_Check_Box_Of_Similar_Transaction()
        time.sleep(1)
        client_section. wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Select_Account_Head()
        time.sleep(2)


        # -----------------------------------------


        client_section.Click_Similar_Section_Explain_Button()
        time.sleep(.2)
        client_section.Click_This_Transaction()
        time.sleep(.5)



        # client_section.Click_Similar_Section_Explain_Button()
        # time.sleep(.2)
        #
        client_section.Click_1st_Check_Box_Of_Similar_Transaction()
        time.sleep(1)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Select_Account_Head()
        time.sleep(2)

        client_section.Click_Similar_Section_Explain_Button()
        time.sleep(.2)
        client_section.Click_Similar_For_Explain()
        time.sleep(.2)



        client_section.Simple_Check_Box_Selection()
        time.sleep(5)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Last_Select()
        time.sleep(2)
        client_section. Click_Explain()
        time.sleep(2)
        # client_section.Click_This_Transaction()
        # time.sleep(.5)


        client_section.Click_Checkbox_Single_Element()
        time.sleep(.2)


        client_section.Click_Exclude_Button()
        time.sleep(.2)
        client_section.Click_Yes()
        time.sleep(.2)


        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Select_Excluded_Tab()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_First_Checkbox()
        time.sleep(.2)
        client_section.Click_Second_Checkbox()
        time.sleep(.2)


        client_section.Click_Delete_Button()
        time.sleep(.2)
        client_section.Click_Yes_Delete()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)


        client_section.Click_First_Checkbox()
        time.sleep(.2)
        client_section.Click_Revive_Button()
        time.sleep(.2)
        client_section.Click_Yes_Delete()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section. Select_Explained_Tab()
        time.sleep(.2)
        client_section.Click_First_Checkbox()
        time.sleep(.2)
        client_section.Click_Unexplain()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_First_Checkbox()
        time.sleep(.2)


        client_section.Click_Single_Explain_Translation()
        time.sleep(.2)
        client_section.Click_Single_Explain_And_Confirm()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)


        client_section.Select_Unexplained_Tab()
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Check_Search_Functionality()
        time.sleep(.2)

        #-------------------------------split----------------------------

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Simple_Check_Box_Selection()
        time.sleep(5)
        client_section.Click_three_dot()
        time.sleep(.2)
        client_section.Click_Split()
        time.sleep(.2)
        client_section.Money_in_or_Money_out()
        time.sleep(.2)
        client_section.Fill_Split_Amount()
        time.sleep(.2)
        client_section.Click_Description()
        time.sleep(.2)

        client_section.Select_Second_Account_Head_Option()
        time.sleep(.2)
        client_section.Fill_Split_Amount_Money_Out()
        time.sleep(.2)

        client_section.Select_Next_option_Second_Account_Head_Option()
        time.sleep(.2)
        client_section.Select_Vat()
        time.sleep(.2)
        client_section.Click_Split_Button()
        time.sleep(1)



        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Check_Search_Functionality()
        time.sleep(.2)
        client_section.Select_Explained_Tab()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Check_Search_Functionality()
        time.sleep(.2)
        client_section.Click_Checkbox_Single_Element()
        time.sleep(.2)
        client_section.Click_Unexplain()
        time.sleep(.2)
        client_section.Click_Yes_Confirm_To_Unexplain_Selected_Transaction()
        time.sleep(.2)

    # #-------------------------------------------setting-----------------------------------------------------------------
    #
    # @pytest.mark.navigation("Login >> Admin Dashboard >> Bookkeeping >> Client ")
    # @pytest.mark.description(f" Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> Banking >> setting")
    #
    #
    # def test_25_Setting(self):
    #     client_section = Banking(driver=self.driver)
    #     time.sleep(.2)
    #
    #
    #
    #     client_section.Select_Search()
    #     time.sleep(5)
    #     client_section.Enter_Company()
    #     time.sleep(.2)
    #     client_section.Click_Company()
    #     time.sleep(.2)
    #     time.sleep(3)
    #     client_section.Click_Input()
    #     time.sleep(.2)
    #
    #
    #     client_section.Select_Setting_Section()
    #     time.sleep(.2)
    #
    #     client_section.Chart_Of_Account()
    #     time.sleep(.2)
    #
    #     client_section.Click_Add_Account()
    #     time.sleep(.2)
    #
    #     client_section.Select_Account_Type_Setting()
    #     time.sleep(.2)
    #
    #     client_section.Enter_name()
    #     time.sleep(.2)
    #
    #     client_section.Select_vat_Rate()
    #     time.sleep(.2)
    #
    #     client_section.Click_Is_Credit_Card()
    #     time.sleep(.2)
    #
    #     client_section.Save_Account()
    #     time.sleep(.2)
    #
    #
    # #---------------------------------------------------------------------------------------------------------------
    #
    #     client_section.Banking_Section()
    #     time.sleep(.2)
    #
    #     client_section.Click_Active_Account()
    #     time.sleep(.2)
    #
    #     client_section.Click_Yes()
    #     time.sleep(.2)
    #
