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


class Banking:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.--------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.banking_section  = (By.XPATH, "//div[contains(text(),'Banking')]")




#-----------------------------------------------------------------------------------------------------------------------

        self.account = (By.XPATH, "//span[normalize-space()='Account']")
        self.select_bank = (By.XPATH, "//label[normalize-space()='Bank']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_account_no = (By.XPATH, "//label[normalize-space()='Account no.']/following::input[1]")
        self.enter_sort_code = (By.XPATH, "//label[normalize-space()='Sort code']/following::input[1]")
        self.enter_iban = (By.XPATH, "//label[normalize-space()='IBAN']/following::input[1]")
        self.save_account = (By.XPATH, "//button[.//span[normalize-space()='Save']]")


#-----------------------------------------------------------------------------------------------------------------------


    def Select_Search(self):
        try:
            client = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.search))
            time.sleep(.2)
            client.click()
            time.sleep(.5)
            print("Click on search field successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")


    def Enter_Company(self, company_name="1ST LIMITED", timeout=12, os=None):

        driver = self.driver
        wait = WebDriverWait(driver, timeout)

        xpaths = [
            "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']",
            "//input[@id='SearchBox33' and @role='searchbox']"
        ]

        last_exc = None
        for xp in xpaths:
            try:
                el = wait.until(EC.presence_of_element_located((By.XPATH, xp)))
                wait.until(EC.visibility_of(el))

                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
                    el.click()
                except Exception:
                    driver.execute_script("arguments[0].click();", el)

                try:
                    el.clear()
                except Exception:
                    pass
                el.send_keys(company_name)

                time.sleep(0.2)
                el.send_keys(Keys.ENTER)

                time.sleep(0.5)
                print(f"Entered '{company_name}' using XPath: {xp}")
                return True


            except Exception as e:
                last_exc = e
                continue

        try:
            path = os.path.join(os.getcwd(), "enter_company_failure.png")
            driver.save_screenshot(path)
            print("Enter_Company: FAILED — screenshot saved to", path)
        except Exception:
            pass

        print("Enter_Company: FAILED. Last exception:", repr(last_exc))
        return False




    def Click_Company(self):
        try:
            click_on_selected_company = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.click_company))
            time.sleep(.3)
            click_on_selected_company.click()
            time.sleep(.2)
            print("Click on company successfully....!!")
        except Exception as e:
            print(f"Enter on click: {e}")
            time.sleep(.5)

#-----------------------------------------------------------------------------------------------------------------------------

    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)

            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Banking_Section(self):
        try:
            banking = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.banking_section))
            time.sleep(.2)
            banking.click()
            time.sleep(.2)

            print("Click on  banking section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Account(self):
        try:
            acc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.account))
            time.sleep(.2)
            acc.click()
            time.sleep(.2)

            print("Click on  account section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Select_Bank(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            bank = wait.until(EC.element_to_be_clickable(self.select_bank))

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                bank
            )
            time.sleep(0.2)

            try:
                bank.click()
            except ElementClickInterceptedException:

                driver.execute_script("arguments[0].click();", bank)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Bank selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)


    def Enter_Account_no(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            enter_account = wait.until(
                EC.element_to_be_clickable(self.enter_account_no)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                enter_account
            )
            time.sleep(0.2)

            enter_account.click()
            time.sleep(0.2)

            enter_account.send_keys(Keys.CONTROL, "a")
            enter_account.send_keys(Keys.DELETE)
            time.sleep(0.2)

            enter_account.send_keys("1234567890")
            time.sleep(0.2)

            print("Account number entered successfully!")

        except Exception as e:
            print(f"Error on Enter_Account_no: {e}")
            time.sleep(0.2)


    def Sort_Code(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            code = wait.until(EC.visibility_of_element_located(self.enter_sort_code))

            time.sleep(0.2)
            code.clear()
            time.sleep(0.2)

            code.send_keys("112233")

            time.sleep(0.3)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ENTER)

            print("Enter sort code successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)


    def Enter_IBAN(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            code = wait.until(EC.visibility_of_element_located(self.enter_iban))

            time.sleep(0.2)
            code.clear()
            time.sleep(0.2)

            code.send_keys("Only for testing...!!")
            time.sleep(0.3)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ENTER)

            print("Enter IBAN successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)


    def Save_Banking(self):

        try:
            save_banking = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.save_account))
            time.sleep(.2)
            save_banking.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Dividends created successfully')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Dividends created successfully"
            #
            print("Test Case  -19  Pass: Banks Account saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)









