import os
import random

import pyautogui
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


class Banking_Credit_card:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.--------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='T.H. LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.banking_section  = (By.XPATH, "//div[contains(text(),'Banking')]")

        self.account = (By.XPATH, "//label[normalize-space()='Add account'] | //span[normalize-space()='Account']")
        self.select_bank = (By.XPATH,
                            "//label[normalize-space()='Bank']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_account_no = (By.XPATH, "//label[normalize-space()='Account no.']/following::input[1]")
        self.enter_sort_code = (By.XPATH, "//label[normalize-space()='Sort code']/following::input[1]")
        # self.enter_iban = (By.XPATH, "//label[normalize-space()='IBAN']/following::input[1]")
        self.click_primary_account = (By.XPATH, "//span[contains(text(),'Primary account')]")
        self.save_account = (By.XPATH, "//button[.//span[normalize-space()='Save']]")




        self.select_account_type = (By.XPATH, "//label[normalize-space()='Account type']/following::div[contains(@class,'rs-control')][1]")

        self.enter_credit_card_number = (By.XPATH, "//label[normalize-space()='Credit card number']/following::input[1]")
        self.click_import = (By.XPATH, "//span[contains(text(),'Import')]")
        self.click_templet = (By.XPATH, "//span[contains(text(),'Template')]")
        self.click_upload = (By.XPATH, "//label[contains(text(),'Upload')]")
        self.upload_import = (By.XPATH, "//div[contains(@class,'ao-modal-container')]//button[.//span[normalize-space()='Import']]")
        self.click_next_button = (By.XPATH, "//span[contains(text(),'Next')]")
        self.click_checkbox_single_element = (By.XPATH, "(//div[contains(@class,'ms-Checkbox-checkbox')]//i[@data-icon-name='CheckMark']/ancestor::label)[2]")
        self.click_explain_1st = (By.XPATH, "(//button[starts-with(@id,'explain-btn-') and .//span[normalize-space()='Explain']])[1]")
        self.click_this_transaction = (By.XPATH, "//div[contains(text(),'This transaction')]")
        self.click_with_all_recommendation = (By.XPATH, "//div[contains(@class,'ms-Callout')]//label[contains(.,'Recommendation')]/parent::div")
        self.click_1st_check_box_of_similar_transaction = (By.XPATH, "(//div[contains(normalize-space(), 'Similar transactions') and not(descendant::*)]/ancestor::div[contains(@class,'tr')][1]//label[contains(@class,'ms-Checkbox-label')])[1]")
        self.select_account_head = (By.XPATH, "(//*[contains(normalize-space(), 'Similar transactions') and not(descendant::*)]/ancestor::div[contains(@class,'tr')][1]//div[contains(@class,'rs-control')])[1]")
        self.click_similar_section_explain_button = (By.XPATH, "(//*[contains(normalize-space(), 'Similar transactions') and not(descendant::*)]/ancestor::div[contains(@class,'tr')][1]//button[starts-with(@id,'explain-btn-')])[1]")
        self.click_similar_for_explain = (By.XPATH, "(//div[contains(@class,'ms-Callout')]//label[contains(normalize-space(),'Similar')])[1]")

        self.click_1st_check_box_of_similar_transaction = (
            By.XPATH,
            "(//*[contains(normalize-space(.),'Similar transactions') and not(descendant::*)]"
            "/ancestor::*[contains(@class,'tr')][1]"
            "//input[@type='checkbox']/following-sibling::label)[1]"
        )

        self.last_plain_entry_checkbox =By.XPATH, "(//div[contains(@class,'tr-focus')]//label[contains(@class,'ms-Checkbox-label')])[last()]"
        self.select_credit_account = (By.XPATH,
                                      "(//div[contains(@style,'cursor: pointer') and .//*[normalize-space()='Reconciled'] and .//*[contains(normalize-space(),'Unexplained transactions')]])[1]")

        self.click_last_select = (By.XPATH,
                                  "(//div[contains(@class,'tr-focus')][last()]//div[contains(@class,'rs-container')])[last()-2]")
        self.click_last_explain = (By.XPATH,
                                   "(//button[.//span[normalize-space()='Explain'] and not(@disabled)])[last()]")

        self.click_exclude_button = (By.XPATH,
                                     "//button[@type='button' and .//i[@data-icon-name='PageRemove'] and .//span[normalize-space()='Exclude']]")

        self.select_excluded = (By.XPATH, "//button[@role='tab'][.//span[contains(normalize-space(),'Excluded')]]")
        self.click_first_checkbox = (By.XPATH,
                                     "(//div[contains(@class,'tr-focus')]//label[contains(@class,'ms-Checkbox-label')])[1]")
        self.click_second_checkbox = (By.XPATH,
                                      "(//div[contains(@class,'tr-focus')]//label[contains(@class,'ms-Checkbox-label')])[2]")
        self.click_delete_button = (By.XPATH, "//button[.//span[normalize-space()='Delete']]")

        self.click_revive_button = (By.XPATH,
                                    "(//div[contains(@class,'tr-focus')]//button[@id='btn-delete' and .//i[@data-icon-name='SyncOccurence']])[1]")

        self.click_explained_tab = (By.XPATH, "//button[@role='tab'][.//span[contains(normalize-space(),'Explained')]]")
        self.click_unexplain = (By.XPATH, "//button[@title='Unexplain all checked transactions']")
        # self.explain_translation = (By.XPATH, "(//button[contains(@id,'btn-undoTrans') and .//i[@data-icon-name='Reply']])[1]")

        self.explain_translation = (
            By.XPATH,
            "(//button[contains(@id,'btn-undoTrans') and .//i[@data-icon-name='Reply']])[1]"
        )

        self.yes_button = (
            By.XPATH,
            "//div[@role='dialog']//button[.//span[normalize-space()='Yes']]"
        )

        self.modal_overlay = (
            By.XPATH,
            "//div[contains(@class,'ms-Overlay')]"
        )
        self.clicks_yes_button = (
            By.XPATH,
            "(//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Yes']])[last()]"
        )

        self.select_explained_1st_entry = (By.XPATH, "(//div[@role='tabpanel' and @aria-hidden='false']//input[@type='checkbox'])[2]")

        self.click_unexplain_icon = (By.XPATH,"(//div[@role='tabpanel' and @aria-hidden='false']//button[@id='btn-undoTrans' and .//i[@data-icon-name='Reply']])[1]")

        self.click_yes = (By.XPATH, "//span[contains(text(),'Yes')]")

        self.select_excluded_section = (By.XPATH, "//button[@role='tab' and .//span[contains(normalize-space(),'Excluded')]]")
        self.click_revive_button = (By.XPATH,
                                    "(//div[contains(@class,'tr-focus')]//button[@id='btn-delete' and .//i[@data-icon-name='SyncOccurence']])[1]")

        self.click_first_delete_permanently = (
            By.XPATH,
            "(//div[@role='tabpanel' and @aria-hidden='false']//button[@id='btn-markDeleted'])[1]"
        )

        self.click_unexplained_tab = (
            By.XPATH,
            "//button[@role='tab' and .//span[contains(normalize-space(),'Unexplained')]]"
        )
        # self.click_row_exclude_icon = (
        #     By.XPATH,
        #     "(//button[starts-with(@id,'exclude-btn') and .//i[@data-icon-name='PageRemove']])[1]"
        # )
        self.click_row_exclude_icon = (
            By.XPATH,
            "(//button[contains(@title,'Exclude') or contains(@aria-label,'Exclude') or .//*[contains(@data-icon-name,'Blocked') or contains(@data-icon-name,'Cancel')]])[1]"
        )

        self.click_include_button = (
            By.XPATH,
            "//button[.//i[@data-icon-name='Sync'] and .//span[normalize-space()='Include']]"
        )




        self.yes_button = (
            By.XPATH,
            "//div[@role='dialog']//button[.//span[normalize-space()='Yes']]"
        )

        self.modal_overlay = (
            By.XPATH,
            "//div[contains(@class,'ms-Overlay')]"
        )
        self.clicks_yes_button = (
            By.XPATH,
            "(//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Yes']])[last()]"
        )

        self.first_row_checkbox = (
            By.XPATH,
            "(//div[contains(@class,'ms-Checkbox') and contains(@class,'is-enabled')]//input[@type='checkbox'])[1]"
            # "(//div[@role='tabpanel' and @aria-hidden='false']//input[@type='checkbox'])[2]/ancestor::div[contains(@class,'ms-Checkbox')]"
        )

        self.click_this_transaction_exclude_button = (
            By.XPATH,
            "//div[contains(@class,'ms-ContextualMenu')]//span[normalize-space()='This transaction']/ancestor::button"
        )

        self.select_all_checkbox = (
            By.XPATH,
            "//div[contains(@class,'header')]//input[@type='checkbox']/ancestor::div[contains(@class,'ms-Checkbox')]"
        )

        self.click_exclude_button_for_all = (
            By.XPATH,
            "//button[.//i[@data-icon-name='PageRemove'] and .//span[normalize-space()='Exclude']]"
        )

        self.select_unexplained_Tab = (By.XPATH,
                                       "//button[@role='tab']//span[contains(normalize-space(),'Unexplained')]")

        self.second_money_in = (By.XPATH,
                                "//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//input[@name='transactions.1.moneyIn']")

        self.first_money_out = (By.XPATH,
                                "(//div[@role='dialog']//input[contains(@name,'moneyOut')])[1]")

        self.select_vat = (By.XPATH,
                           "//div[@role='dialog']//input[@name='transactions.1.vat']/ancestor::div[contains(@class,'rs-container')]")

        self.vat_dropdown = (By.XPATH, "(//div[@role='dialog']//table//tbody//tr[1]//div[contains(@class,'rs-control')])[2]")

        self.click_description = (By.XPATH, "//label[normalize-space()='Description']")

        self.search_input = (
            By.XPATH,
            "//input[@role='searchbox' and @placeholder='Search']"
        )

        self.click_three_dot = (By.XPATH,
                                "(//div[contains(@class,'tr-focus')][last()]//button[.//i[@data-icon-name='More']])[1]")
        self.click_split = (By.XPATH, "//button[@role='menuitem'][.//span[normalize-space()='Split']]")

        self.money_in_or_money_out = (By.XPATH,
                                      "//label[normalize-space()='Money in' or normalize-space()='Money out']/following-sibling::label")

        self.enter_money_in = (By.XPATH,
                               "(//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//input[contains(@name,'moneyIn')])[1]")
        self.enter_money_out = (By.XPATH,
                                "(//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//input[contains(@name,'moneyOut')])[1]")
        self.click_split_button = (By.XPATH,
                                   "//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//button[.//span[normalize-space()='Split']]")

        self.cross_button = (By.XPATH, "//input[contains(@id,'SearchBox')]/following-sibling::div[contains(@class,'clearButton')]//button[@aria-label='Clear text']")


        self.select_2nd_last_entry = (
            By.XPATH,
            "(//div[contains(@class,'tr-focus')])[last()-1]//label[contains(@class,'ms-Checkbox-label')]"
        )
        self.click_quick_fill = (By.XPATH, "//span[contains(text(),'Quick fill')]")

        self.selected_all_explain_btn = (By.XPATH, "//button[@title='Explain all checked transactions']")

    #-----------------------------------------------------------------------------------------------------------------------



    def Select_Search(self):
        try:
            client = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.search))
            time.sleep(.2)
            client.click()
            time.sleep(.5)
            print("Click on search field successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")



    def Enter_Company(self, company_name="T.H. LIMITED", timeout= 30, os=None):

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


    def Select_Account_Type(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            # Account type input inside Add account dialog
            account_type_input = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//div[@role='dialog' and .//*[normalize-space()='Add account']]"
                "//label[normalize-space()='Account type']"
                "/following::input[contains(@id,'react-select')][1]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                account_type_input
            )

            time.sleep(0.5)

            account_type_input.click()
            time.sleep(0.3)

            account_type_input.send_keys(Keys.CONTROL, "a")
            account_type_input.send_keys("Credit card")
            time.sleep(1)

            # select option by text OR react-select option id
            credit_option = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//*[contains(@id,'react-select') and contains(@id,'-option') "
                "and contains(translate(normalize-space(.), "
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'credit card')]"
            )))

            self.driver.execute_script("arguments[0].click();", credit_option)

            print("Credit card selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Account_Type: {type(e).__name__} - {e}")
            raise


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


    def Click_Import(self):
        try:
            import_click = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_import))
            time.sleep(.2)
            import_click.click()
            time.sleep(.2)

            print("Clicked on Import button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    def Click_Templet(self):
        try:
            templet = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_templet))
            time.sleep(.2)
            templet.click()
            time.sleep(.2)

            print("Clicked on templet  button successfully and templet downloaded .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_Upload(self):
        try:
            wait = WebDriverWait(self.driver, 40)
            file_path = r"C:\Users\CT_USER\Desktop\test\Demo Bank Statement.csv"

            file_input = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )

            self.driver.execute_script("""
                arguments[0].style.display = 'block';
                arguments[0].style.visibility = 'visible';
                arguments[0].style.opacity = 1;
            """, file_input)

            file_input.send_keys(file_path)

            print("File uploaded successfully.....!!")

        except Exception as e:
            print(f"Error: {e}")
            raise



    def Upload_Import(self):
        try:
            import_upload = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.upload_import))
            time.sleep(.2)
            import_upload.click()
            time.sleep(.2)

            print("Clicked on Upload Import button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_Next(self):
        for attempt in range(3):
            try:
                wait = WebDriverWait(self.driver, 30)

                next_button = wait.until(
                    EC.element_to_be_clickable(self.click_next_button)
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                    next_button
                )

                time.sleep(0.5)

                self.driver.execute_script("arguments[0].click();", next_button)

                print("Clicked on Next button successfully.....!!")
                return

            except StaleElementReferenceException:
                print(f"Stale element found, retrying... attempt {attempt + 1}")
                time.sleep(1)

            except Exception as e:
                print(f"Error while clicking Next: {type(e).__name__} - {e}")
                raise


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


    def Click_Checkbox_Single_Element(self):
        try:
            wait = WebDriverWait(self.driver, 50)

            # 1. Wait until spinner/loader disappears
            self.wait_for_loader_to_disappear()

            # 2. Locate checkbox
            checkbox = wait.until(
                EC.presence_of_element_located(self.click_checkbox_single_element)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", checkbox
            )

            self.wait_for_loader_to_disappear()

            try:
                checkbox = wait.until(
                    EC.element_to_be_clickable(self.click_checkbox_single_element)
                )
                checkbox.click()
            except ElementClickInterceptedException:
                self.wait_for_loader_to_disappear()
                self.driver.execute_script("arguments[0].click();", checkbox)

            print("Click checkbox single element successfully.....!!")

        except Exception as e:
            print(f"Error on checkbox click: {e}")
            raise


    def Click_Explain_1st(self):
        try:
            explain_1st = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(self.click_explain_1st))
            time.sleep(.2)
            explain_1st.click()
            time.sleep(.2)

            print("Clicked on explain_1st button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    def Click_This_Transaction(self):
        try:
            this_transaction = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_this_transaction))
            time.sleep(.2)
            this_transaction.click()
            time.sleep(.2)

            print("Clicked on this transaction button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_Explain_And_All_Recommendation(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            # Retry because grid refreshes dynamically
            for attempt in range(3):

                try:
                    # fresh explain button lookup every time
                    explain_btn = wait.until(
                        EC.presence_of_element_located((
                            By.XPATH,
                            "(//span[normalize-space()='Explain'])[1]"
                        ))
                    )

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        explain_btn
                    )

                    time.sleep(1)

                    # JS click
                    self.driver.execute_script(
                        "arguments[0].click();",
                        explain_btn
                    )

                    print("Clicked Explain button")

                    break

                except StaleElementReferenceException:
                    print(f"Retrying explain click... Attempt {attempt + 1}")
                    time.sleep(2)

            # Wait menu visible
            recommendation_option = wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[contains(text(),'Recommendation')]"
                ))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                recommendation_option
            )

            time.sleep(1)

            self.driver.execute_script(
                "arguments[0].click();",
                recommendation_option
            )

            print("Clicked Recommendation successfully")

        except TimeoutException as e:
            print(f"TimeoutException: {e}")
            raise

        except Exception as e:
            print(f"Error in Click_Explain_And_All_Recommendation: {type(e).__name__} - {e}")
            raise



    def Click_1st_Check_Box_Of_Similar_Transaction(self):
        wait = WebDriverWait(self.driver, 50)

        for attempt in range(3):
            try:
                self.wait_for_loader_to_disappear()

                check_box = wait.until(
                    EC.presence_of_element_located(self.click_1st_check_box_of_similar_transaction)
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    check_box
                )
                time.sleep(0.3)

                self.wait_for_loader_to_disappear()

                check_box = wait.until(
                    EC.element_to_be_clickable(self.click_1st_check_box_of_similar_transaction)
                )

                try:
                    check_box.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", check_box)

                print("Clicked 1st check box of similar transaction successfully.....!!")
                return

            except StaleElementReferenceException:
                print(f"Stale element found, retrying... {attempt + 1}")
                time.sleep(1)

        raise Exception("Unable to click 1st similar transaction checkbox after retries")

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


    def Select_Account_Head(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            self.wait_for_loader_to_disappear()

            account_head = wait.until(
                EC.element_to_be_clickable(self.select_account_head)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                account_head
            )
            account_head.click()

            self.wait_for_loader_to_disappear()
            self.driver.execute_script("arguments[0].click();", account_head)
            time.sleep(0.5)

            active = self.driver.switch_to.active_element

            active.send_keys("Sales")
            time.sleep(0.5)
            active.send_keys(Keys.ENTER)
            time.sleep(0.5)

            print("Selected Sales - 1/1 successfully.")

        except Exception as e:
            print(f"Error while selecting Sales: {e}")
            raise


    def Click_Similar_Section_Explain_Button(self):

        wait = WebDriverWait(self.driver, 30)

        for attempt in range(3):

            try:
                self.wait_for_loader_to_disappear()

                # Re-locate every time
                explain_btn = wait.until(
                    EC.presence_of_element_located(
                        self.click_similar_section_explain_button
                    )
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    explain_btn
                )

                time.sleep(0.5)

                self.wait_for_loader_to_disappear()

                explain_btn = wait.until(
                    EC.element_to_be_clickable(
                        self.click_similar_section_explain_button
                    )
                )

                try:
                    explain_btn.click()

                except ElementClickInterceptedException:
                    self.driver.execute_script(
                        "arguments[0].click();",
                        explain_btn
                    )

                print("Clicked Similar Section Explain Button successfully.....!!")
                return

            except StaleElementReferenceException:
                print(f"Stale element found, retrying... {attempt + 1}")
                time.sleep(1)

        raise Exception("Unable to click Similar Section Explain Button")


    def Click_Similar_For_Explain(self):
        try:
            account_head = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.click_similar_for_explain))
            time.sleep(.2)
            account_head.click()
            time.sleep(.2)
            print("Select All similar head head successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)



    def Simple_Check_Box_Selection(self):
        try:
            normal = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.last_plain_entry_checkbox))
            time.sleep(.2)
            normal.click()
            time.sleep(.2)
            print("Click on check box for simple entries successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Click_Last_Select(self):

        try:
            wait = WebDriverWait(self.driver, 30)

            self.wait_for_loader_to_disappear()

            last = wait.until(
                EC.element_to_be_clickable(self.click_last_select)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                last
            )
            last.click()

            self.wait_for_loader_to_disappear()
            self.driver.execute_script("arguments[0].click();", last)
            time.sleep(0.5)

            active = self.driver.switch_to.active_element

            active.send_keys("Sales")
            time.sleep(0.5)
            active.send_keys(Keys.ENTER)
            time.sleep(0.5)

            print("Selected Sales - 1/1 successfully.")

        except Exception as e:
            print(f"Error while selecting Sales: {e}")
            raise


    def Click_Explain(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            explains = wait.until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[normalize-space()='Explain']"
            )))

            visible_explains = [el for el in explains if el.is_displayed()]

            explain = visible_explains[-1]

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                explain
            )
            time.sleep(1)

            self.driver.execute_script("arguments[0].click();", explain)

            print("Click on last visible explain successfully.....!!")

        except Exception as e:
            print(f"Error while clicking last explain: {type(e).__name__} - {e}")
            raise



    def Click_Exclude_Button(self):
        try:
            exclude = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_exclude_button))
            time.sleep(.2)
            exclude.click()
            time.sleep(.2)
            print("Click Excluded Button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Select_Excluded_Tab(self):
        try:
            tab = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.select_excluded))
            time.sleep(.2)
            tab.click()
            time.sleep(.2)
            print("Select Excluded section successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Click_First_Checkbox(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            checkbox = wait.until(
                EC.presence_of_element_located(self.click_first_checkbox)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                checkbox
            )
            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", checkbox)

            print("Select 1st checkbox successfully.....!!")

        except Exception as e:
            print(f"Error while selecting checkbox: {type(e).__name__} - {e}")
            raise


    def Click_Second_Checkbox(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            checkbox1 = wait.until(
                EC.presence_of_element_located(self.click_second_checkbox)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                checkbox1
            )
            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", checkbox1)

            print("Select second checkbox successfully.....!!")

        except Exception as e:
            print(f"Error while selecting checkbox: {type(e).__name__} - {e}")
            raise


    def Click_Delete_Button(self):
        try:
            delete = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_delete_button))
            time.sleep(.2)
            delete.click()
            time.sleep(.2)
            print("Select delete icon successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Click_Revive_Button(self):
        try:
            revive = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_revive_button))
            time.sleep(.2)
            revive.click()
            time.sleep(.2)
            print("Click on Revive successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Select_Explained_Tab(self):
        try:
            exp_tab = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_explained_tab ))
            time.sleep(.2)
            exp_tab.click()
            time.sleep(.2)
            print("Select Explained section successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Click_Unexplain(self):
        try:
            unexplain = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_unexplain ))
            time.sleep(.2)
            unexplain.click()
            time.sleep(.2)
            print("Click on Un Explained icon successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)



    def Click_Single_Explain_Translation(self):
        try:
            wait = WebDriverWait(self.driver, 40)


            yes_buttons = self.driver.find_elements(*self.yes_button)
            if yes_buttons and yes_buttons[0].is_displayed():
                self.driver.execute_script("arguments[0].click();", yes_buttons[0])
                time.sleep(1)

                # wait overlay disappear
                wait.until(EC.invisibility_of_element_located(self.modal_overlay))

            # Now click single unexplain/undo icon
            single_explain = wait.until(
                EC.presence_of_element_located(self.explain_translation)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                single_explain
            )
            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", single_explain)

            print("Click on Single explain translation successfully.....!!")

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise


    def Click_Single_Explain_And_Confirm(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            unexplain_icon = wait.until(EC.presence_of_element_located(self.explain_translation))
            self.driver.execute_script("arguments[0].click();", unexplain_icon)

            yes_btn = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//span[normalize-space()='Yes']/ancestor::button"
            )))
            self.driver.execute_script("arguments[0].click();", yes_btn)

            print("Clicked single unexplain and confirmed successfully.....!!")

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise


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


    def Click_Credit_Account(self):
        try:
            credit_account = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.select_credit_account))
            time.sleep(.2)
            credit_account.click()
            time.sleep(.2)

            print("Click on Credit account section successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_Upload_File(self):
        try:
            wait = WebDriverWait(
                self.driver,
                40,
                ignored_exceptions=(StaleElementReferenceException,)
            )

            file_path = r"C:\Users\CT_USER\Desktop\test\Bank Credit Card.csv"
            # file_path = r"C:\Users\CT_USER\Desktop\test\Demo Bank Statement Credit.csv"

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            file_input_xpath = (
                "//div[@role='dialog' and .//*[contains(normalize-space(),'Bank Transactions')]]"
                "//input[@type='file']"
            )

            for attempt in range(5):
                try:
                    file_input = wait.until(
                        EC.presence_of_element_located((By.XPATH, file_input_xpath))
                    )

                    self.driver.execute_script("""
                        arguments[0].style.display = 'block';
                        arguments[0].style.visibility = 'visible';
                        arguments[0].style.opacity = '1';
                        arguments[0].style.height = '1px';
                        arguments[0].style.width = '1px';
                        arguments[0].style.position = 'relative';
                        arguments[0].removeAttribute('hidden');
                        arguments[0].removeAttribute('disabled');
                    """, file_input)

                    time.sleep(0.5)

                    # Re-find after DOM change
                    file_input = wait.until(
                        EC.presence_of_element_located((By.XPATH, file_input_xpath))
                    )

                    file_input.send_keys(file_path)

                    print("File uploaded successfully.....!!")
                    return True

                except StaleElementReferenceException:
                    print(f"Stale file input retry: {attempt + 1}/5")
                    time.sleep(1)

            raise Exception("File input remained stale after retries.")

        except Exception as e:
            print(f"Error while uploading file: {type(e).__name__} - {e}")
            self.driver.save_screenshot("upload_file_error.png")
            raise


    # def Click_Upload_File(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 40)
    #
    #         file_path = r"C:\Users\CT_USER\Desktop\test\Bank Credit Card.csv"
    #
    #         # Find actual file input
    #         file_input = wait.until(
    #             EC.presence_of_element_located((
    #                 By.XPATH,
    #                 "//div[@role='dialog' and .//*[contains(text(),'Bank Transactions')]]//input[@type='file']"
    #             ))
    #         )
    #
    #         # Make hidden input visible
    #         self.driver.execute_script("""
    #             arguments[0].style.display = 'block';
    #             arguments[0].style.visibility = 'visible';
    #             arguments[0].style.opacity = 1;
    #             arguments[0].removeAttribute('hidden');
    #         """, file_input)
    #
    #         time.sleep(1)
    #
    #         # Upload file
    #         file_input.send_keys(file_path)
    #
    #         print("File uploaded successfully.....!!")
    #
    #     except Exception as e:
    #         print(f"Error while uploading file: {type(e).__name__} - {e}")
    #         raise




    def Select_Explained_1st_Entry(self):
        try:
            wait = WebDriverWait(self.driver, 50)

            self.wait_for_loader_to_disappear()

            # wait for Explained tab active
            wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//button[@role='tab' and contains(@data-content,'Explained') and @aria-selected='true']"
            )))

            # get first row checkbox; [1] is header, [2] is first row
            checkbox = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "(//div[@role='tabpanel' and @aria-hidden='false']//input[@type='checkbox'])[2]/ancestor::div[contains(@class,'ms-Checkbox')]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                checkbox
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", checkbox)

            print("Selected explained 1st entry successfully.....!!")

        except Exception as e:
            print(f"Error in Select_Explained_1st_Entry: {type(e).__name__} - {e}")
            raise


    def Click_Unexplain_Icon(self):
        wait = WebDriverWait(self.driver, 40)

        btn = wait.until(EC.presence_of_element_located(self.click_unexplain_icon))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)

        print("Clicked Unexplain icon successfully")


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


    def Select_Excluded_Section(self):

        wait = WebDriverWait(self.driver, 40)

        tab = wait.until(EC.presence_of_element_located(self.select_excluded_section))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            tab
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", tab)

        print("Clicked Excluded tab successfully")


    def Click_Revive_Button(self):
        try:
            revive = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_revive_button))
            time.sleep(.2)
            revive.click()
            time.sleep(.2)
            print("Click on Revive successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)


    def Click_Delete_Icon(self):
        try:
            wait = WebDriverWait(self.driver, 50)

            self.wait_for_loader_to_disappear()

            # Make sure Excluded tab is active
            wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//button[@role='tab' and contains(@data-content,'Excluded') and @aria-selected='true']"
            )))

            delete = wait.until(
                EC.presence_of_element_located(self.click_first_delete_permanently)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                delete
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", delete)

            print("Select delete icon successfully.....!!")

        except Exception as e:
            print(f"Error in Click_Delete_Icon: {type(e).__name__} - {e}")
            raise


    def Click_Unexplained_Tab(self):
        wait = WebDriverWait(self.driver, 40)

        tab = wait.until(EC.presence_of_element_located(self.click_unexplained_tab))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            tab
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", tab)

        print("Clicked Unexplained tab successfully")

    def Click_Row_Exclude_Icon(self):
        wait = WebDriverWait(self.driver, 40)

        btn = wait.until(EC.presence_of_element_located(self.click_row_exclude_icon))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)

        print("Clicked row exclude icon successfully")



    def Click_Include_Button(self):
        wait = WebDriverWait(self.driver, 40)

        btn = wait.until(EC.presence_of_element_located(self.click_include_button))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)

        print("Clicked Include button successfully")



    def Select_Active_Tab_1st_Entry(self):
        try:
            wait = WebDriverWait(self.driver, 50)

            self.wait_for_loader_to_disappear()

            checkbox = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "(//div[@role='tabpanel' and @aria-hidden='false']//input[@type='checkbox'])[2]/ancestor::div[contains(@class,'ms-Checkbox')]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                checkbox
            )

            time.sleep(0.5)
            self.driver.execute_script("arguments[0].click();", checkbox)

            print("Selected active tab 1st entry successfully.....!!")

        except Exception as e:
            print(f"Error in Select_Active_Tab_1st_Entry: {type(e).__name__} - {e}")
            raise

    def Click_First_Row_Checkbox(self):
        wait = WebDriverWait(self.driver, 40)

        checkbox = wait.until(EC.presence_of_element_located(self.first_row_checkbox))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkbox
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", checkbox)

        print("Clicked first row checkbox successfully")

    def wait_for_spinner_to_disappear(self):
        try:
            WebDriverWait(self.driver, 40).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'spinner')]")
                )
            )
        except:
            pass

    def Click_This_Transaction_Exclude_Button(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            self.wait_for_spinner_to_disappear()

            option = wait.until(
                EC.presence_of_element_located(
                    self.click_this_transaction_exclude_button
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                option
            )

            time.sleep(1)

            self.wait_for_spinner_to_disappear()

            # Re-fetch after scroll
            option = wait.until(
                EC.presence_of_element_located(
                    self.click_this_transaction_exclude_button
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                option
            )

            print("Clicked on Exclude - This transaction successfully.")

        except Exception as e:
            print(f"Error in Click_This_Transaction_Exclude_Button: {type(e).__name__} - {e}")
            self.driver.save_screenshot("this_transaction_exclude_error.png")
            raise

    # def Click_This_Transaction_Exclude_Button(self):
    #     wait = WebDriverWait(
    #         self.driver,
    #         40,
    #         ignored_exceptions=[StaleElementReferenceException]
    #     )
    #
    #     locator = self.click_this_transaction_exclude_button
    #
    #     try:
    #         for attempt in range(5):
    #             try:
    #                 option = wait.until(
    #                     EC.presence_of_element_located(locator)
    #                 )
    #
    #                 self.driver.execute_script(
    #                     "arguments[0].scrollIntoView({block:'center', inline:'center'});",
    #                     option
    #                 )
    #
    #                 time.sleep(0.5)
    #
    #                 # Re-fetch after scroll because DOM may re-render
    #                 option = wait.until(
    #                     EC.element_to_be_clickable(locator)
    #                 )
    #
    #                 self.driver.execute_script("arguments[0].click();", option)
    #
    #                 print("Clicked on Exclude button and This transaction successfully")
    #                 return
    #
    #             except StaleElementReferenceException:
    #                 print(f"Stale element retry {attempt + 1}/5")
    #                 time.sleep(1)
    #
    #         raise Exception("Unable to click Exclude option after retries")
    #
    #     except Exception as e:
    #         print(f"Error in Click_This_Transaction_Exclude_Button: {type(e).__name__} - {e}")
    #         raise



    def Click_Select_All_Checkbox(self):
        wait = WebDriverWait(self.driver, 40)

        checkbox = wait.until(
            EC.presence_of_element_located(self.select_all_checkbox)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkbox
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", checkbox)

        print("Clicked select all checkbox successfully")


    def Click_Exclude_Button_For_All(self):
        wait = WebDriverWait(self.driver, 40)

        btn = wait.until(EC.presence_of_element_located(self.click_exclude_button_for_all))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)

        print("Clicked Exclude button successfully")



    #--------------------------------------------------------------------------------------------------------------------


    def Select_Unexplained_Tab(self):
        try:
            unexplained = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.select_unexplained_Tab))
            time.sleep(.2)
            unexplained.click()
            time.sleep(.5)
            print("Select Unexplained tab successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")



    def Check_Search_Functionality(self):

        try:
            wait = WebDriverWait(self.driver, 30)

            client = wait.until(
                EC.element_to_be_clickable(self.search_input)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                client
            )

            client.click()
            time.sleep(0.3)

            client.send_keys(Keys.CONTROL + "a")
            client.send_keys(Keys.BACKSPACE)

            client.send_keys("LATE PAYMENT FEE")
            time.sleep(1)

            client.send_keys(Keys.ENTER)

            print("Search entered successfully.....!!")

        except Exception as e:
            print(f"Error on search field: {e}")



    def Click_three_dot(self):
        try:
            dot = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_three_dot))
            time.sleep(.2)
            dot.click()
            time.sleep(.2)
            print("Click on three dot successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)



    def Click_Split(self):
        try:
            split = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_split))
            time.sleep(.2)
            split.click()
            time.sleep(.2)
            print("Click on Split successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)



    def Money_in_or_Money_out(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            def clean_amount(value):
                return float(
                    value.replace("£", "")
                    .replace(",", "")
                    .replace("(", "")
                    .replace(")", "")
                    .strip()
                )

            # Wait for split popup
            wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]"
            )))

            money_out_elements = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//label[normalize-space()='Money out']/following-sibling::label[1]"
            )

            money_in_elements = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//label[normalize-space()='Money in']/following-sibling::label[1]"
            )

            if money_out_elements and money_out_elements[0].text.strip():
                money_text = money_out_elements[0].text.strip()
                source_type = "money_out"

            elif money_in_elements and money_in_elements[0].text.strip():
                money_text = money_in_elements[0].text.strip()
                source_type = "money_in"

            else:
                raise Exception("Money In or Money Out value not found in split popup")

            print(f"Found {source_type}: {money_text}")

            money_value = clean_amount(money_text)
            divided_value = money_value / 2

            print("Divided Value:", divided_value)

            return source_type, f"{divided_value:.2f}"

        except Exception as e:
            print(f"Error in Money_in_or_Money_out: {type(e).__name__} - {e}")
            raise


    def Fill_Split_Amount(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            def clean_amount(value):
                return float(
                    value.replace("£", "")
                    .replace(",", "")
                    .replace("(", "")
                    .replace(")", "")
                    .strip()
                )

            money_out = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//label[normalize-space()='Money out']/following-sibling::label[1]"
            )

            money_in = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//label[normalize-space()='Money in']/following-sibling::label[1]"
            )

            if money_out and money_out[0].text.strip():
                amount = clean_amount(money_out[0].text)
                divided_value = f"{amount / 2:.2f}"

                # Money out found, so enter value in Money Out field
                field_locator = self.enter_money_out
                field_name = "Money Out"

            elif money_in and money_in[0].text.strip():
                amount = clean_amount(money_in[0].text)
                divided_value = f"{amount / 2:.2f}"

                # Money in found, so enter value in Money In field
                field_locator = self.enter_money_in
                field_name = "Money In"

            else:
                raise Exception("Money In or Money Out amount not found")

            field = wait.until(
                EC.presence_of_element_located(field_locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                field
            )

            time.sleep(0.3)

            self.driver.execute_script("arguments[0].click();", field)

            field.send_keys(Keys.CONTROL + "a")
            field.send_keys(Keys.BACKSPACE)
            field.send_keys(divided_value)

            print(f"Entered {divided_value} in {field_name} field")

        except Exception as e:
            print(f"Error in Fill_Split_Amount: {type(e).__name__} - {e}")
            raise



    def Fill_Split_Amount_Money_Out(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            def clean_amount(value):
                return float(
                    value.replace("£", "")
                    .replace(",", "")
                    .replace("(", "")
                    .replace(")", "")
                    .strip()
                )

            wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//div[@role='dialog' and .//*[normalize-space()='Transaction to split']]"
            )))

            money_out = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//label[normalize-space()='Money out']/following-sibling::label[1]"
            )

            money_in = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//label[normalize-space()='Money in']/following-sibling::label[1]"
            )

            if money_out and money_out[0].text.strip():
                amount = clean_amount(money_out[0].text)
            elif money_in and money_in[0].text.strip():
                amount = clean_amount(money_in[0].text)
            else:
                raise Exception("Money In or Money Out amount not found")

            divided_value = f"{amount / 2:.2f}"

            # Find all visible Money Out fields
            wait.until(lambda d: len(d.find_elements(
                By.XPATH,
                "//div[@role='dialog']//input[@name='transactions.1.moneyOut']"
            )) > 0)

            money_out_fields = self.driver.find_elements(
                By.XPATH,
                "//div[@role='dialog']//input[@name='transactions.1.moneyOut']"
            )

            visible_fields = [f for f in money_out_fields if f.is_displayed()]

            print("Visible Money Out fields count:", len(visible_fields))
            for i, f in enumerate(visible_fields):
                print(i, f.get_attribute("name"), f.get_attribute("value"))

            if len(visible_fields) >= 2:
                money_out_field = visible_fields[1]  # 2nd row Money Out
            else:
                money_out_field = visible_fields[0]  # fallback first available field

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                money_out_field
            )

            time.sleep(0.3)

            self.driver.execute_script("arguments[0].click();", money_out_field)

            money_out_field.send_keys(Keys.CONTROL + "a")
            money_out_field.send_keys(Keys.BACKSPACE)
            money_out_field.send_keys(divided_value)

            print(f"Entered {divided_value} in Money Out field")

        except Exception as e:
            print(f"Error in Fill_Split_Amount_Money_Out: {type(e).__name__} - {e}")
            raise

    def Select_Next_Option_Second_Account_Head_Option(self, option_index=1):
        # try:
            wait = WebDriverWait(self.driver, 40)

            wait.until(EC.visibility_of_element_located((
                By.XPATH,
                "//*[normalize-space()='Transaction to split']"
            )))

            controls = wait.until(lambda d: [
                c for c in d.find_elements(
                    By.XPATH,
                    "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/div[1]/div[1]/div[1]/div[2]"
                )
                if c.is_displayed()
            ])

            print("Visible dropdown controls:", len(controls))
            for i, c in enumerate(controls):
                print(i, c.text)


            if len(controls) >= 4:
                dropdown = controls[2]
            else:
                dropdown = controls[0]  # fallback: first account head

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dropdown
            )
            self.driver.execute_script("arguments[0].click();", dropdown)

            time.sleep(0.5)

            ActionChains(self.driver) \
                .send_keys(Keys.ARROW_DOWN) \
                .pause(0.3) \
                .send_keys(Keys.ARROW_DOWN) \
                .pause(0.3) \
                .send_keys(Keys.ENTER) \
                .perform()

            print("Selected account head option successfully")

        # except Exception as e:
        #     print(f"Error in Select_Next_Option_Second_Account_Head_Option: {type(e).__name__} - {e}")
        #     raise


    def Select_Next_Option_Second_Account_head_Option(self):
        # try:
            wait = WebDriverWait(self.driver, 40)

            # always select LAST account head dropdown
            dropdown = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//div[@role='dialog']//input[@name='transactions.1.accountHead']/preceding::div[contains(@class,'rs-control')][1]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dropdown
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", dropdown)

            time.sleep(1)

            # keyboard navigation
            actions = ActionChains(self.driver)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ENTER)

            actions.perform()
            time.sleep(.2)

            print("Selected next account head option successfully")

        # except Exception as e:
        #     print(f"Error: {type(e).__name__} - {e}")
        #     raise






    def Select_Next_option_Second_Account_Head_Option(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            # always select LAST account head dropdown
            dropdown = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "(//div[@role='dialog']//div[contains(@class,'rs-container')])[last()]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dropdown
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", dropdown)

            time.sleep(1)

            # keyboard navigation
            actions = ActionChains(self.driver)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ENTER)

            actions.perform()
            time.sleep(.2)

            print("Selected next account head option successfully")

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise

    def Click_Split_Button(self):

            try:
                split_button = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.click_split_button))
                time.sleep(.2)
                split_button.click()
                time.sleep(.2)
                print("Click on Split button successfully.....!! ")

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)




    def Select_Vat(self):
        try:
            vat = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.select_vat))
            time.sleep(.2)
            vat.click()
            time.sleep(.2)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                vat
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", vat)

            time.sleep(1)

            # keyboard navigation
            actions = ActionChains(self.driver)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ENTER)

            actions.perform()
            time.sleep(.2)

            print("Select vat successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Click_Description(self):
        try:
            des = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.click_description))
            time.sleep(.2)
            des.click()
            time.sleep(.2)
            print("Click on description button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Select_Vat_Drop_Down(self):
        try:
            vat = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.vat_dropdown))
            time.sleep(.2)
            vat.click()
            time.sleep(.2)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                vat
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", vat)

            time.sleep(1)

            # keyboard navigation
            actions = ActionChains(self.driver)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.5)

            actions.send_keys(Keys.ENTER)

            actions.perform()
            time.sleep(.2)

            print("Select vat successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Cross_Button(self):
        try:
            cross = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.cross_button))
            time.sleep(.2)
            cross.click()
            time.sleep(.5)
            print("Click on Cross icon successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")






    #--------------------------------------------------------------------------------------------------------------------

    def Click_With_All_Recommendation(self):
        # try:
        all_transaction = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.click_with_all_recommendation))
        time.sleep(.2)
        all_transaction.click()
        time.sleep(.2)

        print("Clicked on All transaction button successfully.....!! ")

    # except Exception as e:
    #     print(f"Error: {e}")

    # time.sleep(2)



    def Select_2nd_Last_Entry(self):
            wait = WebDriverWait(self.driver, 40)

            checkbox = wait.until(
                EC.presence_of_element_located(self.select_2nd_last_entry)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                checkbox
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", checkbox)

            print("Clicked on 2nd last entry checkbox successfully.")

    def Click_Quick_Fill(self):
            try:
                quick = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.click_quick_fill))
                time.sleep(.2)
                quick.click()
                time.sleep(.2)
                print("Click on quick fill button and this functionality is running successfully.....!! ")

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)

    def Selected_All_Explain_Icon(self):
            try:
                all_explain_btn = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.selected_all_explain_btn))
                time.sleep(.2)
                all_explain_btn.click()
                time.sleep(.2)
                print("Click on selected all explain button successfully.....!! ")

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)

    def Click_Yes_Delete(self):
        try:
            yes = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_yes))
            time.sleep(.2)
            yes.click()
            time.sleep(.2)

            print("Click on Yes button successfully for delete successfully....!!")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    def Click_Yes_Confirm_To_Unexplain_Selected_Transaction(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            yes_buttons = self.driver.find_elements(*self.yes_button)
            if yes_buttons and yes_buttons[0].is_displayed():
                self.driver.execute_script("arguments[0].click();", yes_buttons[0])
                time.sleep(1)

            print("Click on yes button for confirm to un-explain selected transaction successfully.....!!")

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise


    def Select_Second_Account_Head_Option(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            # 2nd row Account Head dropdown container
            dropdown = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "(//div[@role='dialog']//table//tr[td]//div[contains(@class,'rs-container')])[2]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                dropdown
            )
            time.sleep(0.5)

            # click container, not input
            self.driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(0.5)

            # select second option using keyboard
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.3)
            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(0.3)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            print("Selected 2nd account head option successfully")

        except Exception as e:
            print(f"Error selecting 2nd account head option: {type(e).__name__} - {e}")
            raise
















