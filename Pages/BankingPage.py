import random

from faker import Faker
import time

from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
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
account_number = ''.join([str(random.randint(0,9)) for _ in range(8)])
credit_card_number = fake.credit_card_number(card_type="visa")


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

        self.account = (By.XPATH, "//label[normalize-space()='Add account'] | //span[normalize-space()='Account']")
        self.select_bank = (By.XPATH, "//label[normalize-space()='Bank']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_account_no = (By.XPATH, "//label[normalize-space()='Account no.']/following::input[1]")
        self.enter_sort_code = (By.XPATH, "//label[normalize-space()='Sort code']/following::input[1]")
        # self.enter_iban = (By.XPATH, "//label[normalize-space()='IBAN']/following::input[1]")
        self.click_primary_account = (By.XPATH, "//span[contains(text(),'Primary account')]")
        self.save_account = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        self.select_account_type = (By.XPATH, "//label[normalize-space()='Account type']/following::div[contains(@class,'rs-control')][1]")

        self.enter_credit_card_number = (By.XPATH, "//label[normalize-space()='Credit card number']/following::input[1]")



#----------------------------------------------setting----------------------------------------------------------------

        self.setting_section = (By.XPATH, "//a[@aria-label='Settings' and contains(@href,'/settings')]")
        self.chart_of_account = (By.XPATH, "//span[normalize-space()='Chart of accounts']/ancestor::button")
        self.click_add_account = (By.XPATH, "//span[normalize-space()='Account']/ancestor::button")
        self.select_account_type_setting  = (By.XPATH, "//label[normalize-space()='Account type']/following::input[contains(@id,'react-select')][1]")
        self.enter_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")
        self.enter_vat = (By.XPATH, "//label[normalize-space()='Default VAT rate']/following::div[contains(@class,'rs-control')][1]")
        self.click_credit_card = (By.XPATH, "//span[contains(text(),'is credit card')]")


        self.click_active_account = (By.XPATH, "//span[contains(text(),'Activate')]")
        self.click_yes = (By.XPATH, "//span[contains(text(),'Yes')]")





    def Select_Search(self):
        try:
            client = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.search))
            time.sleep(.2)
            client.click()
            time.sleep(.5)
            print("Click on search field successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")



    def Enter_Company(self, company_name="1ST LIMITED", timeout= 30, os=None):

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
            click_on_selected_company = WebDriverWait(self.driver,30).until(EC.presence_of_element_located(self.click_company))
            time.sleep(.3)
            click_on_selected_company.click()
            time.sleep(.2)
            print("Click on company successfully....!!")
        except Exception as e:
            print(f"Enter on click: {e}")
            time.sleep(.5)


#--------------------------------------------------------------------------------------------------------------------------


    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)

            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Banking_Section(self):
        try:
            banking = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.banking_section))
            time.sleep(.2)
            banking.click()
            time.sleep(.2)

            print("Click on  banking section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)



    def wait_for_loader_to_disappear(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element_located(
                    (By.XPATH,
                     "//*[contains(@class,'spinner') or contains(@class,'loading') or contains(@class,'ms-Spinner')]")
                )
            )
        except TimeoutException:
            pass


    def Account(self):
        try:
            acc = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.account))
            time.sleep(.2)
            acc.click()
            time.sleep(.2)

            print("Click on  account section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Select_Bank(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

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
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)
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

            enter_account.send_keys(account_number)
            time.sleep(0.2)

            print("Account number entered successfully!")

        except Exception as e:
            print(f"Error on Enter_Account_no: {e}")
            time.sleep(0.2)


    def Sort_Code(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

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


    def Click_Primary_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            code = wait.until(EC.visibility_of_element_located(self.click_primary_account))

            time.sleep(0.2)

            code.click()
            time.sleep(0.3)

            print("Click on Primary Account successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)


    def Save_Banking(self):

        try:
            save_banking = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_account))
            time.sleep(.2)
            save_banking.click()
            time.sleep(.2)

            print("Test Case  -   Pass: Current banks Account saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    def Save_Credit_card(self):

        try:
            save_credit = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_account))
            time.sleep(.2)
            save_credit.click()
            time.sleep(.2)


            print("Test Case  -   Pass: Credit card saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Save_Account(self):

        try:
            save_banking = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_account))
            time.sleep(.2)
            save_banking.click()
            time.sleep(.2)

            print("Test Case  -   Pass:  Account saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)



    #-------------------------------------------------------------------------------------------------------------------

    def Select_Account_Type(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            bank = wait.until(EC.element_to_be_clickable(self.select_account_type))

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

            credit = driver.switch_to.active_element
            credit.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            credit.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            credit.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Credit Card selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)


    def Enter_Credit_Card(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:

            enter_account = wait.until(
                EC.element_to_be_clickable(self.enter_credit_card_number)
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

            enter_account.send_keys(credit_card_number)
            time.sleep(0.2)

            print("Credit card number entered successfully!")

        except Exception as e:
            print(f"Error on Enter_Account_no: {e}")
            time.sleep(0.2)

#-----------------------------------------------------------------------------------------------------------------------


    def Select_Setting_Section(self):


            try:
                setting = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.setting_section))
                time.sleep(.2)
                setting.click()
                time.sleep(.2)

                print("Click on Setting section successfully.")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Chart_Of_Account(self):
        try:
            account = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.chart_of_account))
            time.sleep(.2)
            account.click()
            time.sleep(.2)

            print("Click on Chart of account section successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_Add_Account(self):
        try:
            add_account = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_add_account))
            time.sleep(.2)
            add_account.click()
            time.sleep(.2)

            print("Click on Add Account successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Select_Account_Type_Setting(self):
        try:
            account_type = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.select_account_type_setting))
            time.sleep(.2)
            account_type.send_keys("Other creditors Less than one year")
            time.sleep(.2)
            account_type.send_keys(Keys.ENTER)
            time.sleep(.2)

            print("Select Account type successfully.")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Enter_name(self):
        try:
            name = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.enter_name))
            time.sleep(.2)
            name.send_keys("Only for testing")
            time.sleep(.2)


            print("Enter account name successfully....!!")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Select_vat_Rate(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            # 1. Click dropdown
            vat_dropdown = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//label[normalize-space()='Default VAT rate']/following::div[contains(@class,'rs-control')][1]")
                )
            )
            vat_dropdown.click()
            time.sleep(0.5)

            # 2. Use active element (react-select input)
            active = self.driver.switch_to.active_element

            active.send_keys("Exempt")
            time.sleep(0.5)
            active.send_keys(Keys.ENTER)

            print("Selected VAT type successfully: Exempt")

        except Exception as e:
            print(f"Error while selecting VAT rate: {e}")
            raise

    def Click_Is_Credit_Card(self):
        try:
            credit = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_credit_card))
            time.sleep(.2)
            credit.click()
            time.sleep(.2)


            print("Tick on check box of credit card successfully....!!")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Click_Active_Account(self):
        try:
            active = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_active_account))
            time.sleep(.2)
            active.click()
            time.sleep(.2)

            print("Click on Active button successfully....!!")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Click_Yes(self):
        try:
            yes = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_yes))
            time.sleep(.2)
            yes.click()
            time.sleep(.2)

            print("Click on Yes button successfully and Account activated successfully....!!")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)











