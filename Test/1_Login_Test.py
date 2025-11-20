import unittest
from selenium import webdriver
from Pages.LoginPage import loginPage
from configReader import ConfigReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_login(self):
        driver = self.driver

        # Create instance of ConfigReader
        config = ConfigReader(r"C:\Users\CT_USER\PycharmProjects\BOOKKEEPING\config.properties")
        # Instance of login_page
        loginpage = loginPage(driver)

        driver.get(config.get_value("DEFAULT", "URL"))

        # Login
        loginpage.enter_username(config.get_value("DEFAULT", "USERNAME"))
        time.sleep(1)
        loginpage.enter_password(config.get_value("DEFAULT", "Password"))
        time.sleep(1)
       #loginpage.eye_button()
        time.sleep(1)
        loginpage.click_sign_in_button()
        time.sleep(1)
        print("Test case - 1: Pass: Login successfully....!!")
        time.sleep(10)


        loginpage.Click_On_Menu()
        time.sleep(.2)
        loginpage.Click_Bookkeeping()
        time.sleep(.2)






if __name__ == "__main__":
    unittest.main()



