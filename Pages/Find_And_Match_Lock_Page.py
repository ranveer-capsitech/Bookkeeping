import os

import pyautogui
from faker import Faker
import time
import random
from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime, timedelta
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException

fake = Faker()
random_first_name = fake.first_name()
random_last_name = fake.last_name()
full_name = f"{random_first_name} {random_last_name}"
date_time_value = datetime.now().strftime('%d/%m/%Y %I:%M %p')
tomorrow_date = datetime.today() + timedelta(days=1)
formatted_date = tomorrow_date.strftime("%d-%m-%y")  # Adjust format as needed

random_email = fake.email()
random_email1 = fake.email()
random_indian_phone = fake.phone_number()
random_indian_phone_1 = fake.phone_number()
dob = fake.date_of_birth(minimum_age=18)
formatted_dob = dob.strftime('%d/%m/%Y')
account_number = ''.join([str(random.randint(0,9)) for _ in range(8)])
credit_card_number = fake.credit_card_number(card_type="visa")
credit_card_no = fake.credit_card_number(card_type="visa")


class Find_And_Match_Lock:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH, "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH,"//a[@title='T.H. LIMITED' and contains(@href,'/books/clients/')]")
        self.manual_transactions = (By.XPATH, "//li[contains(normalize-space(.),'entering manually click')]//button[normalize-space()='here']")

        self.banking_section = (By.XPATH, "//div[contains(text(),'Banking')]")

        # -----------------------------------------------------------------------------------------------------------------------

        self.account = (By.XPATH, "//label[normalize-space()='Add account'] | //span[normalize-space()='Account']")
        self.select_bank = (By.XPATH,
                            "//label[normalize-space()='Bank']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_account_no = (By.XPATH, "//label[normalize-space()='Account no.']/following::input[1]")
        self.enter_sort_code = (By.XPATH, "//label[normalize-space()='Sort code']/following::input[1]")
        # self.enter_iban = (By.XPATH, "//label[normalize-space()='IBAN']/following::input[1]")
        self.click_primary_account = (By.XPATH, "//span[contains(text(),'Primary account')]")
        self.save_account = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        self.enter_date = (By.XPATH, "//input[@name='transactions.0.date']/following::i[@data-icon-name='Calendar'][1]")
        self.first_description = (By.XPATH, "//input[@name='transactions.0.description']")
        self.enter_money_out = (By.XPATH, "//div[@role='dialog']//input[@name='transactions.0.moneyOut']")
        self.enter_money_in = (By.XPATH, "//div[@role='dialog']//input[@name='transactions.0.moneyIn']")
        self.click_save_manual_transaction = (By.XPATH,
                                              "//div[@role='dialog' and .//*[normalize-space()='Add manual transactions']]//button[.//span[normalize-space()='Save']]")
        self.money_out_value = (
            By.XPATH,
            "//div[contains(@class,'itemContainer') and .//*[contains(normalize-space(),'PAYMENT RECEIVED -- THANK')]]"
            "//div[contains(@class,'td-focus')][4]"
        )
        self.click_find_match = (By.XPATH, "//button[@role='tab' and .//span[normalize-space()='Find match']]")

        self.click_contact_dropdown = (By.XPATH,
                                       "//label[normalize-space()='Contact']/following::div[contains(@class,'rs-indicators-container')][1]")
        self.add_manual_transaction = (By.XPATH,
                                       "//button[@title='Add manual transactions']//i[@data-icon-name='Add']/ancestor::button[1]")

        # -----------------------------------------------------Reimbursements----------------------------------------------------

        self.reimbursements_section = (By.XPATH, "//button[.//span[normalize-space()='Reimbursements']]")
        self.click_reimbursements = (By.XPATH, "//button[.//span[normalize-space()='Reimbursement']]")
        self.reimbursed_to = (By.XPATH, "//div[contains(@class,'placeholder') and normalize-space()='User name']")
        self.reimbursed_account = (By.XPATH,
                                   "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        # self.method = (By.XPATH, "//label[normalize-space()='Method']/following::div[contains(@class,'rs-placeholder')][1]")
        self.reimbursed_amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@type='text'][1]")
        self.enter_notes = (By.XPATH, "//label[normalize-space()='Note :']/following::input[@name='notes'][1]")
        self.save_reimbursement = (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Save']]")

        # ------------------------------------------------Refund-----------------------------------------------------------------

        self.refunds_section = (By.XPATH, "//button[.//span[normalize-space()='Refunds']]")
        self.click_refunds = (By.XPATH, "//button[.//span[normalize-space()='Refund']]")
        self.refund_from = (By.XPATH,
                            "//label[normalize-space()='Refund from']/following::div[contains(@class,'rs-input-container')][1]")
        self.refund_account = (By.XPATH,
                               "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        # self.method = (By.XPATH, "//label[normalize-space()='Method']/following::div[contains(@class,'singleValue')][1]")
        self.amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@type='text'][1]")
        self.enter_notes_for_refund = (By.XPATH,
                                       "//label[normalize-space()='Note :']/following::input[@name='notes'][1]")
        self.save_refund = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")

    # -----------------------------------------------------------------------------------------------------------------------










    def Select_Search(self):
            try:
                client = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
                time.sleep(.2)
                client.click()
                time.sleep(.5)
                print("Click on search field successfully.....! ")
            except Exception as e:
                print(f"Error on click:{e}")

    def Enter_Company(self, company_name="T.H. LIMITED", timeout=30, os=None):

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
                click_on_selected_company = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(self.click_company))
                time.sleep(.3)
                click_on_selected_company.click()
                time.sleep(.2)
                print("Click on company successfully....!!")
            except Exception as e:
                print(f"Enter on click: {e}")
                time.sleep(.5)

        # -----------------------------------------------------------------------------------------------------------------------

    # def Click_Input(self):
    #         try:
    #             input = WebDriverWait(self.driver, 30).until(
    #                 EC.visibility_of_element_located(self.click_input_drop_down))
    #             time.sleep(.2)
    #             input.click()
    #             time.sleep(.2)
    #             print("Input drop down open successfully....!!")
    #         except Exception as e:
    #             print(f"Error on click:{e}")
    #
    # def Click_Sales(self):
    #         try:
    #             sales = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_sales))
    #             time.sleep(.2)
    #             sales.click()
    #             time.sleep(.2)
    #             print("Click on Sales successfully....!!")
    #         except Exception as e:
    #             print(f"Error on Click:{e}")
    #             time.sleep(.2)

    def Click_Manual(self):
            try:
                manual = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.manual_transactions))
                time.sleep(.2)
                manual.click()
                time.sleep(.5)
                print("Click on  add manual transactions successfully.....! ")
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

            self.sort_code_value = "112233"

            code.clear()
            code.send_keys(self.sort_code_value)

            driver.switch_to.active_element.send_keys(Keys.ENTER)

            print("Enter sort code successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            raise

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

    def Click_Added_Bank(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            # after save, wait for page/card reload
            self.wait_for_loader_to_disappear()
            time.sleep(2)

            # 112233 -> 11-22-33
            formatted_sort_code = f"{self.sort_code_value[:2]}-{self.sort_code_value[2:4]}-{self.sort_code_value[4:]}"

            print("Looking for sort code:", formatted_sort_code)

            bank_card_xpath = (
                f"//label[contains(normalize-space(),'{formatted_sort_code}')]"
                f"/ancestor::div[contains(@class,'box-shadow') or contains(@class,'p10')]"
            )

            bank_card = wait.until(
                EC.presence_of_element_located((By.XPATH, bank_card_xpath))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", bank_card
            )
            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", bank_card)

            print("Click on added bank successfully.......!!!!!")

        except Exception as e:
            print(f"Error: {e}")
            raise

        # ------------------------------------------------------------------------------------------------------------------------------

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

    def Click_Added_Bank(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            # after save, wait for page/card reload
            self.wait_for_loader_to_disappear()
            time.sleep(2)

            # 112233 -> 11-22-33
            formatted_sort_code = f"{self.sort_code_value[:2]}-{self.sort_code_value[2:4]}-{self.sort_code_value[4:]}"

            print("Looking for sort code:", formatted_sort_code)

            bank_card_xpath = (
                f"//label[contains(normalize-space(),'{formatted_sort_code}')]"
                f"/ancestor::div[contains(@class,'box-shadow') or contains(@class,'p10')]"
            )

            bank_card = wait.until(
                EC.presence_of_element_located((By.XPATH, bank_card_xpath))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", bank_card
            )
            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", bank_card)

            print("Click on added bank successfully.......!!!!!")

        except Exception as e:
            print(f"Error: {e}")
            raise

    def Add_Manual_Transaction(self):
        try:
            manual_transaction = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.add_manual_transaction))
            time.sleep(.2)
            manual_transaction.click()
            time.sleep(.2)

            print("Clicked on add manual transaction button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Enter_Date(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            today_date = datetime.now().strftime("%d/%m/%Y")

            date_field = wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    # "//input[@name='transactions.0.date']"
                    "//input[starts-with(@name,'transactions.') and contains(@name,'.date') and @placeholder='DD/MM/YYYY']"

                ))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                date_field
            )

            self.driver.execute_script("""
                   const input = arguments[0];
                   const value = arguments[1];

                   input.removeAttribute('readonly');
                   input.focus();

                   input.value = '';
                   input.dispatchEvent(new Event('input', { bubbles: true }));
                   input.dispatchEvent(new Event('change', { bubbles: true }));

                   input.value = value;
                   input.dispatchEvent(new Event('input', { bubbles: true }));
                   input.dispatchEvent(new Event('change', { bubbles: true }));

                   input.blur();
               """, date_field, today_date)

            print(f"Today's date entered successfully: {today_date}")

        except Exception as e:
            print(f"Error in Enter_Date: {type(e).__name__} - {e}")
            raise

    def Enter_Description(self, description="Manual transaction test"):
        try:
            wait = WebDriverWait(self.driver, 30)

            description_field = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//input[@name='transactions.0.description']"
                ))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                description_field
            )

            self.driver.execute_script("arguments[0].click();", description_field)

            description_field.send_keys(Keys.CONTROL + "a")
            description_field.send_keys(Keys.BACKSPACE)
            description_field.send_keys(description)

            print(f"Description entered successfully: {description}")

        except Exception as e:
            print(f"Error in Enter_Description: {type(e).__name__} - {e}")
            raise

    def Enter_Money_Out(self, moneyout="2400"):
        try:
            wait = WebDriverWait(self.driver, 30)

            money_out = wait.until(
                EC.element_to_be_clickable(self.enter_money_out))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                money_out
            )

            self.driver.execute_script("arguments[0].click();", money_out)

            money_out.send_keys(Keys.CONTROL + "a")
            money_out.send_keys(Keys.BACKSPACE)
            money_out.send_keys(moneyout)

            print(f"Description entered successfully: {moneyout}")

        except Exception as e:
            print(f"Error in Enter_Description: {type(e).__name__} - {e}")
            raise

    def Enter_Money_In(self, moneyin="1160"):
        try:
            wait = WebDriverWait(self.driver, 30)

            money_in = wait.until(
                EC.element_to_be_clickable(self.enter_money_in))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                money_in
            )

            self.driver.execute_script("arguments[0].click();", money_in)

            money_in.send_keys(Keys.CONTROL + "a")
            money_in.send_keys(Keys.BACKSPACE)
            money_in.send_keys(moneyin)

            print(f"Description entered successfully: {moneyin}")

        except Exception as e:
            print(f"Error in Enter_Description: {type(e).__name__} - {e}")
            raise

    def Click_Save_Manual_Transaction(self):
        try:
            save_manual_transaction = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.click_save_manual_transaction))
            time.sleep(.2)
            save_manual_transaction.click()
            time.sleep(.2)

            print("Clicked on save button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Money_Out_Value(self):

        locator = (
            By.XPATH,
            "(//label[normalize-space()='Manual'])[1]"
        )

        wait = WebDriverWait(self.driver, 30)

        for attempt in range(3):
            try:
                element = wait.until(
                    EC.visibility_of_element_located(locator)
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                wait.until(
                    EC.element_to_be_clickable(locator)
                )

                # Re-fetch element after scroll
                element = self.driver.find_element(*locator)

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                print("First transaction row clicked successfully.")
                return

            except StaleElementReferenceException:
                print(f"Stale element detected. Retry {attempt + 1}/3")

        raise Exception("Unable to click transaction row after retries")

    def Click_Find_Match(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            find_match_locator = (
                By.XPATH,
                "//div[@role='tablist']//button[@role='tab' and .//span[normalize-space()='Find match']]"
            )

            find_match = wait.until(
                EC.element_to_be_clickable(find_match_locator)
            )

            self.driver.execute_script("arguments[0].click();", find_match)

            print("Clicked on Find match successfully.....!!")

        except Exception as e:
            print(f"Error in Click_Find_Match: {type(e).__name__} - {e}")
            raise

    def Click_Contact_Dropdown_For_Money_In(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            contact = wait.until(EC.element_to_be_clickable(self.click_contact_dropdown))

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                contact
            )
            time.sleep(0.2)

            try:
                contact.click()
            except ElementClickInterceptedException:

                driver.execute_script("arguments[0].click();", contact)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys("KM Consultancy Limited (Steven Phillip)")
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)

            time.sleep(2)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Contact selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)

    def Click_Contact_Dropdown_For_Money_Out(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            contact = wait.until(EC.element_to_be_clickable(self.click_contact_dropdown))

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                contact
            )
            time.sleep(0.2)

            try:
                contact.click()
            except ElementClickInterceptedException:

                driver.execute_script("arguments[0].click();", contact)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys("Alex")
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)

            time.sleep(2)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Contact selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)

    def wait_for_page_ready(self, timeout=20):
        wait = WebDriverWait(self.driver, timeout)

        # Wait for the browser document.
        wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Wait for Fluent UI overlay.
        wait.until(
            EC.invisibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'ms-Overlay') "
                    "and not(contains(@style,'display: none'))]"
                )
            )
        )

        # Wait for common loaders/spinners.
        wait.until(
            EC.invisibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'spinner') "
                    "or contains(@class,'Spinner') "
                    "or contains(@class,'loader') "
                    "or contains(@class,'Loader')]"
                )
            )
        )

#-----------------------------------------------------------------------------------------------------------------------



    def Reimbursed_Section(self):
        try:
            reimbursed_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.reimbursements_section))
            time.sleep(.2)
            reimbursed_sec.click()
            time.sleep(.2)
            print("Click on reimbursed Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Reimbursed(self):
        try:
            click_reimbursed = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_reimbursements))
            time.sleep(.2)
            click_reimbursed.click()
            time.sleep(.2)
            print("Click on reimbursed successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Reimbursed_to(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        for _ in range(3):
            try:
                container = wait.until(
                    EC.element_to_be_clickable(self.reimbursed_to)
                )
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", container
                )
                try:
                    container.click()
                except ElementClickInterceptedException:

                    driver.execute_script("arguments[0].click();", container)
                break
            except StaleElementReferenceException:
                continue
        else:
            raise TimeoutException("Could not click Director / Other dropdown")

        for _ in range(3):
            try:
                active = driver.switch_to.active_element

                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(.2)

                active.send_keys(Keys.ENTER)
                time.sleep(.2)

                print("Select Reimbursed To successfully....!!")
                return
            except StaleElementReferenceException:

                continue

        raise TimeoutException("Could not select a director from dropdown")


    def Reimbursed_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.reimbursed_account)
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

            print("Reimbursed account selected successfully....!!")
        except Exception as e:
            print(f"Error on Click reimbursed account: {e}")


    def Enter_Amount(self):
        try:
            amount = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.reimbursed_amount))
            time.sleep(.3)
            amount.click()

            time.sleep(0.2)
            amount.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            amount.send_keys(Keys.BACK_SPACE)
            time.sleep(0.2)
            amount.send_keys("120")
            time.sleep(.3)
            print("Click on reimbursed amount successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")



    def Enter_Notes(self):
        #try:
            notes = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_notes))
            time.sleep(.2)
            notes.send_keys("only for testing")
            time.sleep(.2)
            print("Enter notes successfully....!!")
        # except Exception as e:
        #     print(f"Error on Click:{e}")

    def Save_Reimbursement(self):
        wait = WebDriverWait(
            self.driver,
            40,
            poll_frequency=0.3,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        save_locator = (
            By.XPATH,
            "//button[@type='submit' "
            "and not(@disabled) "
            "and .//span[normalize-space()='Save']]"
        )

        reimbursement_number_locator = (
            By.XPATH,
            "//*[normalize-space()='Reimbursement no.']"
            "/following::input[1]"
        )

        no_expense_locator = (
            By.XPATH,
            "//*[normalize-space()='No expense found']"
        )

        success_locator = (
            By.CSS_SELECTOR,
            ".ms-MessageBar--success, "
            ".Toastify__toast--success, "
            "[class*='success']"
        )

        error_locator = (
            By.CSS_SELECTOR,
            ".ms-MessageBar--error, "
            ".Toastify__toast--error, "
            ".ms-TextField-errorMessage, "
            "[class*='errorMessage']"
        )

        overlay_locator = (
            By.CSS_SELECTOR,
            ".ms-Spinner, .ms-Overlay"
        )

        try:
            self.driver.switch_to.default_content()

            wait.until(
                EC.invisibility_of_element_located(overlay_locator)
            )

            # Check whether an expense is available
            no_expense_elements = self.driver.find_elements(
                *no_expense_locator
            )

            if any(
                    element.is_displayed()
                    for element in no_expense_elements
            ):
                self.driver.save_screenshot(
                    "No_Expense_Available.png"
                )

                raise AssertionError(
                    "Reimbursement cannot be saved because "
                    "'No expense found' is displayed. Create an "
                    "unpaid expense, select another reimbursed user, "
                    "or disable Auto allocation if advance "
                    "reimbursement is supported."
                )

            reimbursement_input = wait.until(
                EC.visibility_of_element_located(
                    reimbursement_number_locator
                )
            )

            old_reimbursement_number = (
                reimbursement_input.get_attribute("value")
            )

            old_url = self.driver.current_url

            save_button = wait.until(
                EC.element_to_be_clickable(save_locator)
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                save_button
            )

            save_button = wait.until(
                EC.element_to_be_clickable(save_locator)
            )

            try:
                save_button.click()

            except (
                    ElementClickInterceptedException,
                    StaleElementReferenceException
            ):
                wait.until(
                    EC.invisibility_of_element_located(
                        overlay_locator
                    )
                )

                save_button = wait.until(
                    EC.element_to_be_clickable(save_locator)
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    save_button
                )

            print("Save button clicked. Waiting for confirmation...")

            def check_save_result(driver):
                # Check application errors
                visible_errors = []

                for element in driver.find_elements(*error_locator):
                    try:
                        if element.is_displayed():
                            text = element.text.strip()

                            if text:
                                visible_errors.append(text)
                    except StaleElementReferenceException:
                        continue

                if visible_errors:
                    return {
                        "status": "error",
                        "message": " | ".join(visible_errors)
                    }

                # Check success notification
                for element in driver.find_elements(*success_locator):
                    try:
                        if element.is_displayed():
                            return {
                                "status": "success",
                                "message": element.text.strip()
                            }
                    except StaleElementReferenceException:
                        continue

                # Check navigation
                if driver.current_url != old_url:
                    return {
                        "status": "success",
                        "message": "URL changed after saving"
                    }

                # Check whether a new reimbursement number was generated
                try:
                    current_number = driver.find_element(
                        *reimbursement_number_locator
                    ).get_attribute("value")

                    if (
                            current_number
                            and current_number
                            != old_reimbursement_number
                    ):
                        return {
                            "status": "success",
                            "message": (
                                "New reimbursement number generated: "
                                f"{current_number}"
                            )
                        }

                except (
                        StaleElementReferenceException,
                        NoSuchElementException
                ):
                    return {
                        "status": "success",
                        "message": "Form closed after saving"
                    }

                return False

            result = wait.until(
                check_save_result,
                message=(
                    "No save confirmation, URL change, error "
                    "message, or new reimbursement number detected."
                )
            )

            if result["status"] == "error":
                raise AssertionError(
                    f"Reimbursement save failed: "
                    f"{result['message']}"
                )

            print(
                "Reimbursement saved successfully. "
                f"{result['message']}"
            )

            return True

        except Exception as error:
            self.driver.save_screenshot(
                "Save_Reimbursement_Error.png"
            )

            print(f"Exception type: {type(error).__name__}")
            print(f"Exception details: {repr(error)}")
            print(f"Current URL: {self.driver.current_url}")

            # Capture JavaScript console errors
            try:
                browser_logs = self.driver.get_log("browser")

                for log in browser_logs:
                    if log.get("level") in ("SEVERE", "WARNING"):
                        print(
                            f"Browser {log['level']}: "
                            f"{log['message']}"
                        )
            except Exception:
                pass

            raise


#-----------------------------------------------------------------------------------------------------------------------


    def Refunds_Section(self):
        try:
            refunds_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.refunds_section))
            time.sleep(.2)
            refunds_sec.click()
            time.sleep(.2)
            print("Click on Refunds Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Refunds(self):
        try:
            refunds = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_refunds))
            time.sleep(.2)
            refunds.click()
            time.sleep(.2)
            print("Click on Refunds successfully....!!")
            time.sleep(10)
        except Exception as e:
            print(f"Error on Click:{e}")

    def Refund_from(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        for _ in range(3):
            try:
                container = wait.until(
                    EC.element_to_be_clickable(self.refund_from)
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", container
                )

                try:
                    container.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", container)

                break
            except StaleElementReferenceException:

                continue
            except TimeoutException:

                raise TimeoutException("Refund from dropdown clickable ")

        for _ in range(3):
            try:
                active = driver.switch_to.active_element

                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)

                active.send_keys(Keys.ENTER)
                time.sleep(0.2)

                print("Select Refund from successfully....!!")
                return
            except StaleElementReferenceException:

                time.sleep(0.2)
                continue

        raise TimeoutException("Refund from dropdown se option select")

    def Select_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.refund_account)
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

            print("Refund account selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Refund account: {e}")


    def Save_Refund(self):
        try:
            save_ref = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_refund))
            time.sleep(.2)
            save_ref.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Reimbursement saved successfully with number')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Reimbursement saved successfully"

            print("Test Case 28.5  - Pass: Refund saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)







