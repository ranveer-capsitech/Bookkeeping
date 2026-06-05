import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
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

        self.click_on_menu = (By.XPATH, "//button[contains(@class,'Header-button') and @title='Modules']//i[@data-icon-name='Waffle']")
        self.click_bookkeeping_section = (By.XPATH, "(//span[normalize-space()='Bookkeeping'])[1]")


         # Methods to use for login
    def enter_username(self, username):
        WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(self.username_input)
                ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(self.password_input)
                ).send_keys(password)

    def click_sign_in_button(self):
        WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(self.sign_in_button)
                ).click()


    def Click_On_Menu(self):

        wait = WebDriverWait(self.driver, 30)

        waffle_locator = (
            By.XPATH,
            "//i[@data-icon-name='Waffle']/ancestor::button[1]"
        )

        overlay_locator = (
            By.XPATH,
            "//div[@style='position: fixed; inset: 0px;']"
        )

        try:
            # Wait for blocking overlay to disappear
            try:
                wait.until(EC.invisibility_of_element_located(overlay_locator))
            except TimeoutException:
                print("Overlay still visible, trying ESC key or JS cleanup")

                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                time.sleep(1)

            waffle_btn = wait.until(
                EC.presence_of_element_located(waffle_locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                waffle_btn
            )

            time.sleep(0.5)

            waffle_btn = wait.until(
                EC.element_to_be_clickable(waffle_locator)
            )

            try:
                waffle_btn.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", waffle_btn)

            print("Clicked on Waffle icon successfully.")

        except Exception as e:
            print(f"Error on click Waffle icon: {type(e).__name__} - {e}")
            raise


        # try:
        #     WebDriverWait(self.driver, 30).until(
        #         EC.invisibility_of_element_located((By.CLASS_NAME, "ant-spin-spinning"))
        #     )
        #
        #     click_menu = WebDriverWait(self.driver, 30).until(
        #     EC.visibility_of_element_located(self.click_on_menu)
        #     )
        #     click_menu.click()
        #     time.sleep(.2)
        #     print("Test case - 2: Pass: Click an active employee section successfully.....!")
        #     time.sleep(.2)
        #
        # except Exception as e:
        #     print(f" Error on click: {e}")


    def Click_Bookkeeping(self):
        try:
            WebDriverWait(self.driver,30).until(
                EC.invisibility_of_element_located((By.CLASS_NAME,"ant-spin-spinning"))
            )
            click_bookkeeping = WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located(self.click_bookkeeping_section)
            )
            click_bookkeeping.click()
            time.sleep(.2)
            print("Test case - 3: Pass: Click an Bookkeeping section successfully.....!")
            time.sleep(.2)

        except Exception as e:
            print(f" Error on click:: {e}")






