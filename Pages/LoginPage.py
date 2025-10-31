import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class loginPage:
    def __init__(self, driver):
        self.driver = driver



        # WebElements
        self.username_input = (By.ID, "Input_Email")
        self.password_input = (By.ID, "Input_Password")
        self.sign_in_button = (By.ID, "login-submit")

        self.click_on_menu = (By.XPATH, "(//button[@id='btn-menus-callout'])[1]")
        self.click_bookkeeping_section = (By.XPATH, "(//span[normalize-space()='Bookkeeping'])[1]")


         # Methods to use for login
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.username_input)
                ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.password_input)
                ).send_keys(password)

    def click_sign_in_button(self):
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.sign_in_button)
                ).click()


    def Click_On_Menu(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "ant-spin-spinning"))
            )

            click_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.click_on_menu)
            )
            click_menu.click()
            time.sleep(.2)
            print("Test_2 :: click an active employee section successfully.....!")
            time.sleep(.2)

        except Exception as e:
            print(f" Error on click: {e}")


    def Click_Bookkeeping(self):
        try:
            WebDriverWait(self.driver,10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME,"ant-spin-spinning"))
            )
            click_bookkeeping = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(self.click_bookkeeping_section)
            )
            click_bookkeeping.click()
            time.sleep(.2)
            print("Test_3 :: click on bookkeeping section successfully.....!")
            time.sleep(.2)

        except Exception as e:
            print(f" Error on click:: {e}")






