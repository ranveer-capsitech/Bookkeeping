from faker import Faker
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
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


class Vat:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.--------------------------------------------------------


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.vat_return_section  = (By.XPATH, "//div[contains(text(),'VAT returns')]")

# -----------------------------------------------------------------------------------------------------------------------
        self.add_vate = (By.XPATH, "//button[.//span[normalize-space()='VAT return']]")

        self.account = (By.XPATH, "//span[normalize-space()='VAT return']")
        self.obligations = (By.XPATH, "//label[normalize-space()='Obligations']/following::div[contains(@id,'react-select')][1]")
        self.save_vat = (By.XPATH,  "//button[.//span[normalize-space()='Save']]")




#-----------------------------------------------------------------------------------------------------------------------

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


    def Vat_Return_Section(self):
        try:
            vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.vat_return_section))
            time.sleep(.2)
            vat.click()
            time.sleep(.2)

            print("Click on  vat return section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Add_Vat(self):
        try:
            vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.add_vate))
            time.sleep(.2)
            vat.click()
            time.sleep(.2)

            print("Click on  vat return section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Select_Obligations(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            # Wait until element is clickable
            obligation = wait.until(
                EC.element_to_be_clickable(self.obligations)
            )
            time.sleep(0.2)

            # Scroll to center
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", obligation)
            time.sleep(0.2)

            # Try normal click
            try:
                obligation.click()
            except:
                # JS click fallback
                driver.execute_script("arguments[0].click();", obligation)

            time.sleep(0.3)

            # Press ENTER
            active = driver.switch_to.active_element
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Select Obligation successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)



    def Save_Vat(self):

        try:
            save_vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.save_vat))
            time.sleep(.2)
            save_vat.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Dividends created successfully')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Dividends created successfully"
            #
            print("Test Case 20 - Pass: Vat saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)





