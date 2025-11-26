from faker import Faker
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime, timedelta


fake = Faker()
random_first_name = fake.first_name()
random_last_name = fake.last_name()
full_name = f"{random_first_name} {random_last_name}"
date_time_value = datetime.now().strftime('%d/%m/%Y %I:%M %p')
tomorrow_date = datetime.today() + timedelta(days=1)
formatted_date = tomorrow_date.strftime("%d-%m-%y")

random_item_name = fake.word().capitalize() + " " + fake.word().capitalize()

random_email = fake.email()
random_email1 = fake.email()
random_indian_phone = fake.phone_number()
random_indian_phone_1 = fake.phone_number()
dob = fake.date_of_birth(minimum_age=18)
formatted_dob = dob.strftime('%d/%m/%Y')


class Dividend:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.--------------------------------------------------------


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.dividends_section  = (By.XPATH, "//a[@data-value='dividends']")


#-----------------------------------------------------------------------------------------------------------------------

        self.click_dividends = (By.XPATH, "//span[normalize-space(text())='Dividend']")
        self.select_director = (By.XPATH, "//label[normalize-space()='Authorised director']/following::div[contains(@class,'placeholder')][1]")
        self.select_type = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        self.select_class = (By.XPATH,"//div[@id='react-select-8-placeholder' and text()='Select']")
        self.dividend_per_share = (By.XPATH, "//label[text()='Dividend per share']/following::input[1]")
        self.payment = (By.XPATH, "//label[text()='Payment date']/following::input[1]")
        self.save_dividends = (By.XPATH, "//button[.//span[text()='Save']]")


#------------------------------------------------Method-----------------------------------------------------------------

    def Select_Business(self):
        try:
            client = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.select_business_name))
            time.sleep(.2)
            client.click()
            time.sleep(.2)
            print("Select a business name successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)

            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Dividends_Section(self):
        try:
            dividends = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dividends_section))
            time.sleep(.2)
            dividends.click()
            time.sleep(.2)
            print("Click on  dividends section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Dividends(self):
        try:
            click_div = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_dividends))
            time.sleep(.2)
            click_div .click()
            time.sleep(.2)
            print("Click on Add dividends  successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)




    def Authorised_director(self):

        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            dir = wait.until(
                EC.element_to_be_clickable(self.select_director)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dir
            )
            time.sleep(0.2)

            try:
                dir.click()
            except Exception:
                driver.execute_script("arguments[0].click();", dir)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Authorised director selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Account: {e}")


    def Select_Type(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:

            dropdown = wait.until(
                EC.visibility_of_element_located(self.select_type)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                dropdown
            )
            time.sleep(0.2)

            try:
                dropdown.click()
            except Exception:
                driver.execute_script("arguments[0].click();", dropdown)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            #active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Type selected successfully....!!")

        except TimeoutException:
            print("Timeout: 'Type' dropdown not found or not visible. Check the XPath self.select_type.")
        except Exception as e:
            print(f"Error while selecting Type: {e}")


    def Select_Class(self):

        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            cls = wait.until(
                EC.element_to_be_clickable(self.select_class)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                cls
            )
            time.sleep(0.2)

            try:
                cls.click()
            except Exception:
                driver.execute_script("arguments[0].click();", dir)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Class selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Account: {e}")

    def Dividend_Per_Share(self, value="100"):

            try:

                share = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(self.dividend_per_share)
                )

                share.click()
                time.sleep(0.3)

                share.send_keys(Keys.CONTROL, "a")
                time.sleep(0.1)
                share.send_keys(Keys.BACK_SPACE)
                time.sleep(0.3)

                share.send_keys(str(value))
                time.sleep(0.3)

                print("Enter share value successfully....!!")

            except Exception as e:
                print(f"Error on Enter_Value: {e}")
                time.sleep(0.2)

    def Enter_Payment_Date(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            # Generate today's date
            today = datetime.today().strftime("%d/%m/%Y")

            # Wait for element
            payment_date = wait.until(EC.visibility_of_element_located(self.payment))

            time.sleep(0.2)
            payment_date.clear()
            time.sleep(0.2)

            # Enter today's date
            payment_date.send_keys(today)
            time.sleep(0.3)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ENTER)

            print("Enter payment date successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)


    # def Enter_Payment_Date(self):
    #     driver = self.driver
    #     wait = WebDriverWait(driver, 15)
    #     try:
    #             payment_date = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.payment))
    #             time.sleep(.2)
    #             payment_date.send_keys("25/08/2025")
    #             time.sleep(.2)
    #             active = driver.switch_to.active_element
    #             time.sleep(0.2)
    #             active.send_keys(Keys.ENTER)
    #             time.sleep(0.2)
    #             print("Enter payment date  successfully....!!")
    #     except Exception as e:
    #             print(f"Error on Click:{e}")
    #             time.sleep(.2)

    def Save_Asset(self):

            try:
                save_ref = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.save_dividends))
                time.sleep(.2)
                save_ref.click()
                time.sleep(.2)

                update_message = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//*[contains(normalize-space(), 'Dividends created successfully')]"))
                )

                # Assert the presence of the success message
                assert update_message, "Dividends created successfully"

                print("Test Case  - Pass: Dividends created successfully.")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

















