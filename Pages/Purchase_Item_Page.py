from faker import Faker
import time
from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
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


class ClientPurchase:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")

        self.item = (By.XPATH, "//button[@role='tab' and .//span[normalize-space()='Items']]")
        self.click_add_item = (By.XPATH, "//button[.//span[normalize-space()='Item']]")
        self.enter_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")
        self.pur_description = (By.XPATH, "//label[normalize-space()='Description']/following::input[1]")
        self.sell_description = (By.XPATH, "//span[normalize-space()='For sales']/following::input[@type='text'][2]")
        self.enter_pur_price = (By.XPATH, "//td[normalize-space()='Unit price']/following::input[@type='text'][1]")
        self.enter_sell_price = (By.XPATH, "//div[@role='dialog']//td[normalize-space()='Unit price']/following::input[@type='text'][2]")
        self.click_on_create = (By.XPATH, "//span[contains(text(),'Create')]")

    def Item_Section(self):

        try:
            item_section = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.item))
            time.sleep(.2)
            item_section.click()
            time.sleep(.2)
            print("click on item section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_on_item(self):
        try:
            click_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_add_item))
            time.sleep(.2)
            click_item.click()
            time.sleep(.2)
            print("Click on add item successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Name(self):
        try:
            name_el = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.enter_name)
            )

            # Create random name
            random_item_name = fake.word().capitalize() + " " + fake.word().capitalize()

            # Step 1: Clear using JS
            self.driver.execute_script("arguments[0].value='';", name_el)
            time.sleep(0.2)

            # Step 2: Slow typing to avoid React override
            for ch in random_item_name:
                name_el.send_keys(ch)
                time.sleep(0.1)

            print(f"Enter name successfully: {random_item_name}")

        except Exception as e:
            print(f"Error on entering name: {e}")

    def Enter_Description_For_Purchases(self):
        try:
            pur_des = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pur_description))
            time.sleep(.2)
            pur_des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description for purchases successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Description_For_Sell(self):
        try:
            pur_des = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sell_description))
            time.sleep(.2)
            pur_des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description for sell successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Unit_Price_Purchases(self):
        try:
            pur_price = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.enter_pur_price))
            time.sleep(.2)
            pur_price.send_keys("100")
            time.sleep(.2)
            print("Enter Unit price for purchases successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Unit_Price_Sell(self):
        try:
            sell_price = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.enter_sell_price))
            time.sleep(.2)
            sell_price.send_keys("100")
            time.sleep(.2)
            print("Enter Unit price for Sell successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Create_Item(self):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_on_create))
            time.sleep(.2)
            item.click()
            time.sleep(.2)

            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Items created successfully')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Items created successfully"

            print("Test Case -13 :  Pass: Items created successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

