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


class Banking:

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
        self.click_import = (By.XPATH, "//span[contains(text(),'Import')]")
        self.click_templet = (By.XPATH, "//span[contains(text(),'Template')]")
        self.click_upload = (By.XPATH, "//label[contains(text(),'Upload')]")
        self.upload_import = (By.XPATH, "//div[contains(@class,'ao-modal-container')]//button[.//span[normalize-space()='Import']]")
        self.click_next_button = (By.XPATH, "//span[contains(text(),'Next')]")
        self.click_checkbox_single_element = (By.XPATH, "(//div[contains(@class,'ms-Checkbox-checkbox')]//i[@data-icon-name='CheckMark']/ancestor::label)[2]")
        self.click_explain_1st = (By.XPATH, "(//button[starts-with(@id,'explain-btn-') and .//span[normalize-space()='Explain']])[1]")
        self.click_this_transaction = (By.XPATH, "//div[contains(text(),'This transaction')]")
        self.click_with_all_recommendation = (By.XPATH, "//div[contains(@class,'ms-Callout')]//label[contains(normalize-space(),'Recommendation')]")
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

        # self.last_plain_entry_checkbox = (
        #     By.XPATH,
        #     "(//div[contains(@class,'tr') "
        #     "and .//input[@type='checkbox'] "
        #     "and not(contains(normalize-space(.),'Recommendation')) "
        #     "and not(contains(normalize-space(.),'Similar transactions')) "
        #     "and .//div[normalize-space()='Select']]"
        #     "//input[@type='checkbox']/following-sibling::label)[last()]"
        # )

        self.click_last_select = (By.XPATH, "(//div[contains(@class,'tr-focus')][last()]//div[contains(@class,'rs-container')])[last()-2]")
        self.click_last_explain = (By.XPATH, "(//button[.//span[normalize-space()='Explain'] and not(@disabled)])[last()]")

        #----------------------------------------------------------------------------------------------------------------

        self.select_credit_account = (By.XPATH, "(//div[contains(@style,'cursor: pointer') and .//*[normalize-space()='Reconciled'] and .//*[contains(normalize-space(),'Unexplained transactions')]])[1]")


        self.click_exclude_button = (By.XPATH, "//button[@type='button' and .//i[@data-icon-name='PageRemove'] and .//span[normalize-space()='Exclude']]")
        self.select_excluded = (By.XPATH, "//button[@role='tab'][.//span[contains(normalize-space(),'Excluded')]]")
        self.click_first_checkbox = (By.XPATH, "(//div[contains(@class,'tr-focus')]//label[contains(@class,'ms-Checkbox-label')])[1]")
        self.click_second_checkbox = (By.XPATH, "(//div[contains(@class,'tr-focus')]//label[contains(@class,'ms-Checkbox-label')])[2]")
        self.click_delete_button = (By.XPATH, "//button[.//span[normalize-space()='Delete']]")

        self.click_revive_button = (By.XPATH, "(//div[contains(@class,'tr-focus')]//button[@id='btn-delete' and .//i[@data-icon-name='SyncOccurence']])[1]")

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
        self.clicks_yes_button =  (
    By.XPATH,
    "(//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Yes']])[last()]"
)


        self.click_unexplain_tab = (By.XPATH, "//button[@role='tab'][.//span[contains(normalize-space(),'Unexplained')]]")
        self.click_three_dot = (By.XPATH, "(//div[contains(@class,'tr-focus')][last()]//button[.//i[@data-icon-name='More']])[1]")
        self.click_split = (By.XPATH, "//button[@role='menuitem'][.//span[normalize-space()='Split']]")

        self.money_in_or_money_out = (By.XPATH, "//label[normalize-space()='Money in' or normalize-space()='Money out']/following-sibling::label")

        self.enter_money_in = (By.XPATH, "//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//input[contains(@name,'moneyIn')]")
        self.enter_money_out = (By.XPATH, "//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//input[contains(@name,'moneyOut')]")

        # self.enter_2nd_money_out = (By.XPATH, "//div[@role='dialog']//input[@name='transactions.1.moneyOut']")
        # self.enter_2nd_money_in = (By.XPATH, "//div[@role='dialog']//input[@name='transactions.1.moneyIn']")

        self.enter_2nd_money_out = (
            By.XPATH,
            "(//div[@role='dialog']//input[contains(@name,'moneyOut')])[2]"
        )

        self.enter_2nd_money_in = (
            By.XPATH,
            "(//div[@role='dialog']//input[contains(@name,'moneyIn')])[2]"
        )

        self.click_split_button = (By.XPATH, "//div[@role='dialog' and .//*[normalize-space()='Explain transactions']]//button[.//span[normalize-space()='Split']]")











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


#----------------------------------------------------Current account----------------------------------------------------


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


    # def Sort_Code(self):
    #     driver = self.driver
    #     wait = WebDriverWait(driver, 30)
    #
    #     try:
    #
    #         code = wait.until(EC.visibility_of_element_located(self.enter_sort_code))
    #
    #         time.sleep(0.2)
    #         code.clear()
    #         time.sleep(0.2)
    #
    #         code.send_keys("112233")
    #
    #         time.sleep(0.3)
    #
    #         active = driver.switch_to.active_element
    #         active.send_keys(Keys.ENTER)
    #
    #         print("Enter sort code successfully...!!")
    #
    #     except Exception as e:
    #         print(f"Error on Click: {e}")
    #         time.sleep(0.2)

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




#------------------------------------------------------------------------------------------------------------------------------




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

    # def Click_Upload(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 30)
    #
    #         upload = wait.until(EC.element_to_be_clickable(self.click_upload))
    #         upload.click()
    #         time.sleep(2)
    #
    #         pyautogui.moveTo(500, 500)
    #         pyautogui.write(r"C:\Users\CT_USER\Desktop\test\Demo Bank Statement.csv", interval=0.01)
    #         pyautogui.press("enter")
    #
    #         print("Clicked on upload button successfully.....!! ")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         raise


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




    # def Click_Upload(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 40)
    #         file_path = r"C:\Users\CT_USER\Desktop\test\Demo Bank Statement.csv"
    #
    #         upload = wait.until(EC.element_to_be_clickable(self.click_upload))
    #         self.driver.execute_script("arguments[0].click();", upload)
    #         time.sleep(1)
    #
    #         file_input = wait.until(
    #             EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    #         )
    #
    #         file_input.send_keys(file_path)
    #
    #         print("File uploaded successfully.....!!")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         raise



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

    # def Click_Next(self):
    #     try:
    #         next_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_next_button))
    #         time.sleep(.2)
    #         next_button.click()
    #         time.sleep(.2)
    #
    #         print("Clicked on Next button successfully.....!! ")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #
    #         time.sleep(2)

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

    def Click_With_All_Recommendation(self):
        # try:
            all_transaction = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_with_all_recommendation))
            time.sleep(.2)
            all_transaction.click()
            time.sleep(.2)

            print("Clicked on All transaction button successfully.....!! ")

        # except Exception as e:
        #     print(f"Error: {e}")

            # time.sleep(2)

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


    # def Click_Similar_Section_Explain_Button(self):
    #     try:
    #         account_head = WebDriverWait(self.driver, 30).until(
    #             EC.element_to_be_clickable(self.click_similar_section_explain_button))
    #         time.sleep(.2)
    #         account_head.click()
    #         time.sleep(.2)
    #         print("Select Account head  successfully.....!! ")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         time.sleep(2)
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

    # def Click_Single_Explain_Translation(self):
    #     #     try:
    #     #         single_explain = WebDriverWait(self.driver, 40).until(
    #     #             EC.element_to_be_clickable(self.explain_translation))
    #     #         time.sleep(.2)
    #     #         single_explain.click()
    #     #         time.sleep(.2)
    #     #         print("Click on Single explain translation successfully.....!! ")
    #     #
    #     #     except Exception as e:
    #     #         print(f"Error: {e}")
    #     #         time.sleep(2)

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


#-------------------------------------------------------------------------------------------------------------------------

    # def Click_Unexplain_Tab(self):
    #     try:
    #         Unexplain_Tab = WebDriverWait(self.driver, 40).until(
    #             EC.element_to_be_clickable(self.click_unexplain_tab))
    #         time.sleep(.2)
    #         Unexplain_Tab.click()
    #         time.sleep(.2)
    #         print("Click on Unexplain Tab successfully.....!! ")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         time.sleep(2)

    def Click_Unexplain_Tab(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            # wait for overlay/modal to disappear
            try:
                wait.until(EC.invisibility_of_element_located((
                    By.XPATH,
                    "//div[contains(@class,'ms-Overlay')]"
                )))
            except TimeoutException:
                print("Overlay still visible, trying to close modal if available...")

                close_buttons = self.driver.find_elements(
                    By.XPATH,
                    "//button[@aria-label='Close' or @title='Close']"
                )

                for btn in close_buttons:
                    if btn.is_displayed():
                        self.driver.execute_script("arguments[0].click();", btn)
                        time.sleep(1)
                        break

                wait.until(EC.invisibility_of_element_located((
                    By.XPATH,
                    "//div[contains(@class,'ms-Overlay')]"
                )))

            unexplain_tab = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//button[@role='tab' and contains(@name,'Unexplained')]"
            )))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                unexplain_tab
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", unexplain_tab)

            print("Click on Unexplained Tab successfully.....!!")

        except Exception as e:
            print(f"Error on Click_Unexplain_Tab: {type(e).__name__} - {e}")
            raise
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

    # def Money_in_or_Money_out(self):
    #     try:
    #         money = WebDriverWait(self.driver, 40).until(
    #             EC.visibility_of_element_located(self.money_in_or_money_out)).text
    #         time.sleep(.2)
    #
    #
    #         print("Money In Value:", money)
    #
    #         clean_money = money.replace("£", "").replace(",", "").strip()
    #
    #         # Convert to float
    #         money_value = float(clean_money)
    #
    #         # Divide by 2
    #         divided_value = money_value / 2
    #
    #         print("Divided Value:", divided_value)
    #
    #         return f"{divided_value:.2f}"
    #
    #     except Exception as e:
    #         print(f"Error: {type(e).__name__} - {e}")
    #         raise

    def Money_In(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            divided_value = self.Money_in_or_Money_out()

            money_in = wait.until(
                EC.element_to_be_clickable(self.enter_money_in)
            )

            money_in.clear()
            money_in.send_keys(divided_value)

            print("Entered Money In Value:", divided_value)

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise

    def Money_Out(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            divided_value = self.Money_in_or_Money_out()

            money_out = wait.until(
                EC.element_to_be_clickable(self.enter_money_out)
            )

            money_out.clear()
            money_out.send_keys(divided_value)

            print("Entered Money In Value:", divided_value)

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise

    def Fill_Opposite_Split_Amount(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            def clean_amount(value):
                return float(value.replace("£", "").replace(",", "").replace("(", "").replace(")", "").strip())

            money_out = self.driver.find_elements(
                By.XPATH,
                "//label[normalize-space()='Money out']/following-sibling::label"
            )

            money_in = self.driver.find_elements(
                By.XPATH,
                "//label[normalize-space()='Money in']/following-sibling::label"
            )

            if money_out and money_out[0].text.strip():
                amount = clean_amount(money_out[0].text)
                divided_value = f"{amount / 2:.2f}"

                field = wait.until(EC.element_to_be_clickable(self.enter_money_in))
                field.clear()
                field.send_keys(divided_value)

                print(f"Money Out found, entered {divided_value} in Money In field")

            elif money_in and money_in[0].text.strip():
                amount = clean_amount(money_in[0].text)
                divided_value = f"{amount / 2:.2f}"

                field = wait.until(EC.element_to_be_clickable(self.enter_money_out))
                field.clear()
                field.send_keys(divided_value)

                print(f"Money In found, entered {divided_value} in Money Out field")

            else:
                print("No Money In or Money Out value found")

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

    def Fill_Opposite__Sec_Split_Amount(self):
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
                "//label[normalize-space()='Money out']/following-sibling::label"
            )

            money_in = self.driver.find_elements(
                By.XPATH,
                "//label[normalize-space()='Money in']/following-sibling::label"
            )

            print("MoneyIn input count:",
                  len(self.driver.find_elements(By.XPATH,
                                                "//div[@role='dialog']//input[contains(@name,'moneyIn')]")))

            print("MoneyOut input count:",
                  len(self.driver.find_elements(By.XPATH,
                                                "//div[@role='dialog']//input[contains(@name,'moneyOut')]")))

            if money_out and money_out[0].text.strip():

                amount = clean_amount(money_out[0].text)
                divided_value = f"{amount / 2:.2f}"

                # ALWAYS use LAST visible moneyIn field
                field = wait.until(EC.presence_of_element_located((
                    By.XPATH,
                    "(//div[@role='dialog']//input[contains(@name,'moneyIn')])[last()]"
                )))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", field
                )

                self.driver.execute_script("arguments[0].value='';", field)

                field.send_keys(divided_value)

                print(f"Entered {divided_value} in Money In")

            elif money_in and money_in[0].text.strip():

                amount = clean_amount(money_in[0].text)
                divided_value = f"{amount / 2:.2f}"

                field = wait.until(EC.presence_of_element_located((
                    By.XPATH,
                    "(//div[@role='dialog']//input[contains(@name,'moneyOut')])[last()]"
                )))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", field
                )

                self.driver.execute_script("arguments[0].value='';", field)

                field.send_keys(divided_value)

                print(f"Entered {divided_value} in Money Out")

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            raise

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















































    #--------------------------------------------Credit card--------------------------------------------------------------------


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
            wait = WebDriverWait(self.driver, 40)

            file_path = r"C:\Users\CT_USER\Desktop\test\Bank Credit Card.csv"

            # Find actual file input
            file_input = wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//div[@role='dialog' and .//*[contains(text(),'Bank Transactions')]]//input[@type='file']"
                ))
            )

            # Make hidden input visible
            self.driver.execute_script("""
                arguments[0].style.display = 'block';
                arguments[0].style.visibility = 'visible';
                arguments[0].style.opacity = 1;
                arguments[0].removeAttribute('hidden');
            """, file_input)

            time.sleep(1)

            # Upload file
            file_input.send_keys(file_path)

            print("File uploaded successfully.....!!")

        except Exception as e:
            print(f"Error while uploading file: {type(e).__name__} - {e}")
            raise





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
            name.send_keys("Cashplus Credit Card")
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


#-----------------------------------------------------------------------------------------------------------------------










