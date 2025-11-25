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


class Journals:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.journals = (By.XPATH, "//a[@data-value='Journals']//div[normalize-space()='Journals']")


#----------------------------------------------Journals-----------------------------------------------------------------

        self.click_journal = (By.XPATH, "//button[.//span[contains(text(),'Journal')]]")
        self.journal_reference = (By.XPATH,"//label[normalize-space()='Journal reference']/following::input[@type='text'][1]")
        self.select_account = (By.XPATH, "//td//div[text()='Select']/following::input[1]")
        #self.select_vat = (By.XPATH, "//div[contains(@class,'rs-input-container')]/input[@id='react-select-4-input']")
        self.debit = (By.XPATH, "//input[@id='items.0.debit']")
        self.credit = (By.XPATH, "//input[contains(@id,'credit') and contains(@id,'1')]")
        self.save_journal = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

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


    def Click_Journals(self):
        try:
            click_journal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.journals))
            time.sleep(.2)
            click_journal.click()
            time.sleep(.2)
            print("Click on journal section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Journals_Button(self):
        try:
            click_journal_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_journal))
            time.sleep(.2)
            click_journal_btn.click()
            time.sleep(.2)
            print("Click on journal successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Journal_Reference(self):
        try:
            reference = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.journal_reference))
            time.sleep(.2)
            reference.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter journal Reference successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Select_Account(self):

        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.select_account)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                account
            )
            time.sleep(0.2)

            try:
                account.click()
            except Exception:
                driver.execute_script("arguments[0].click();", account)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Account selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Account: {e}")


    def Enter_Value_IN_Debit(self, value="100"):
        try:

            debit_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.debit)
            )


            debit_input.click()
            time.sleep(0.3)


            debit_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.1)
            debit_input.send_keys(Keys.BACK_SPACE)
            time.sleep(0.3)


            debit_input.send_keys(str(value))
            time.sleep(0.3)

            print("Enter Debit successfully....!!")

        except Exception as e:
            print(f"Error on Enter_Value_IN_Debit: {e}")
            time.sleep(0.2)




    def Enter_Value_IN_Credit(self, value="100"):
        try:

            credit_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.credit)
            )


            credit_input.click()
            time.sleep(0.3)


            credit_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.1)
            credit_input.send_keys(Keys.BACK_SPACE)  # or Keys.DELETE
            time.sleep(0.3)


            credit_input.send_keys(str(value))
            time.sleep(0.3)

            print("Enter Credit successfully....!!")

        except Exception as e:
            print(f"Error on Enter_Value_IN_Debit: {e}")
            time.sleep(0.2)

    def Save_Journal(self):


            try:
                journal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.save_journal))
                time.sleep(.2)
                journal.click()
                time.sleep(.2)



                print("Test Case  - Pass: Journal saved successfully.")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)






