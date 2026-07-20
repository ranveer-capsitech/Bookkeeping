import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.Details_Explain_Filtering_Function_Page import Detail_Explain_Filter


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
    @pytest.mark.description(f"Go to Select Admin panel >> click Home >> click bookkeeping >> go for Client >> Banking >> Filter functionality")


    def test_27_Go_Banking(self):
        client_section = Detail_Explain_Filter(driver=self.driver)
        time.sleep(.2)
        #
        client_section. Select_Search()
        time.sleep(5)
        client_section.Enter_Company()
        time.sleep(.2)
        client_section.Click_Company()
        time.sleep(.2)
        client_section.Banking_Section()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        client_section.Account()
        time.sleep(.2)

        client_section.Select_Account_Type()
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
        time.sleep(.2)
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

        # -----------------------------------------------------------------------------------------------------------------------

        client_section.Click_Back_Button()
        time.sleep(.2)

        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Change_Date_Calendar()
        time.sleep(1)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)

        # --------------------------------------------------------------------------------------------------

        client_section.Click_Data_Filter_Icon()
        time.sleep(.2)
        client_section.Shorting_old_to_new()
        time.sleep(.2)

        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_Data_Filter_Icon()
        time.sleep(.2)
        client_section.Shorting_new_to_old()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_Data_Filter_Icon()
        time.sleep(.2)
        client_section.Click_Select_All_Date()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Select_First_Option()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Apply_Button()
        time.sleep(3)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)


        client_section.Click_cross_icon()
        time.sleep(2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        # #----------------------------------------------description--------------------------------------------------------------

        client_section.Click_Description_Filter_Icon()
        time.sleep(.2)
        client_section.Shorting_a_to_z()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_Description_Filter_Icon()
        time.sleep(.2)
        client_section.Shorting_z_to_a()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_Description_Filter_Icon()
        time.sleep(.2)

        client_section.Click_Select_All_Date()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)
        client_section.Select_First_Option()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Apply_Button()
        time.sleep(3)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        client_section.Click_cross_icon()
        time.sleep(2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        # -----------------------------------------Money- out ------------------------------------------------------------

        client_section.Click_MoneyOut_Filter_Icon()
        time.sleep(.2)
        client_section.Small_Lest_To_Largest()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_MoneyOut_Filter_Icon()
        time.sleep(.2)
        client_section.Largest_To_Small_Lest()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_MoneyOut_Filter_Icon()
        time.sleep(.2)
        client_section.Click_Select_All_Date()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)
        client_section.Select_First_Option()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Apply_Button()
        time.sleep(3)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        client_section.Click_cross_icon()
        time.sleep(2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        # -----------------------------------------Money- in ------------------------------------------------------------

        client_section.Click_MoneyIn_Filter_Icon()
        time.sleep(.2)
        client_section.Small_Lest_To_Largest()
        time.sleep(1)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(1)

        client_section.Click_MoneyIn_Filter_Icon()
        time.sleep(.2)
        client_section.Largest_To_Small_Lest()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)

        client_section.Click_MoneyIn_Filter_Icon()
        time.sleep(.2)
        client_section.Click_Select_All_Date()
        time.sleep(.2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(.2)
        client_section.Select_First_Option()
        time.sleep(.2)
        client_section.wait_for_loader_to_disappear()
        time.sleep(.2)
        client_section.Click_Apply_Button()
        time.sleep(5)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        client_section.Click_cross_icon()
        time.sleep(2)
        client_section.wait_for_spinner_to_disappear()
        time.sleep(2)

        client_section.Enter_Search()
        time.sleep(.2)
        client_section.Remove_Search()
        time.sleep(.2)

        # -----------------------------------------------------------------------------------------------------------------------

        client_section.click_magnifier_icon()
        time.sleep(2)


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