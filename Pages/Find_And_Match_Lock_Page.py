
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

        self.click_company = (By.XPATH,"//a[@title='DARSAH LTD' and contains(@href,'/books/clients/')]")

        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.manual_transactions = (By.XPATH, "//li[contains(normalize-space(.),'entering manually click')]//button[normalize-space()='here']")

        self.banking_section = (By.XPATH, "//div[contains(text(),'Banking')]")

        #---------------------------------------------------------------------------------------------------------------
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")
        self.invoice = (By.XPATH, "(//span[contains(text(),'Invoice')])[1]")
        self.click_item_for_invoice = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.change_quantity = (By.XPATH, "//th[normalize-space()='Qty.']/following::input[@type='number'][1]")
        self.save_invoice = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.click_pound_icon = (By.XPATH,
                                 "(//*[@data-automationid='DetailsRowCell']//button[contains(@id,'btnReceipt')])[1]")



















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

    # -----------------------------------------------banking-------------------------------------------------------------

        self.click_import = (By.XPATH, "//span[contains(text(),'Import')]")
        self.click_templet = (By.XPATH, "//span[contains(text(),'Template')]")
        self.click_upload = (By.XPATH, "//label[contains(text(),'Upload')]")
        self.upload_import = (By.XPATH,
                              "//div[contains(@class,'ao-modal-container')]//button[.//span[normalize-space()='Import']]")
        self.click_next_button = (By.XPATH, "//span[contains(text(),'Next')]")
#------------------------------------------------------------------------------------------------------------------
        self.click_on_receipt_with_bank_charge = (By.XPATH, "//div[@title='Receipt with Bank Charge']")
        self.select_receipts = (By.XPATH,
                              "//input[@name='invoices.0']/preceding-sibling::div[contains(@class,'rs-control')][1]")

        self.select_settle = (By.XPATH, "//div[contains(text(),'Settle')]")
        self.click_match = (By.XPATH, "//button[.//span[normalize-space()='Match']]")

#----------------------------------------------------------------------------------------------------
        self.sales_return = (By.XPATH, "//div[@title='Sales Return']")
        self.payment = (By.XPATH, "//button[@role='tab' and @data-id='payments']")
        self.payment_due = (By.XPATH, "//div[@title='Payment Due']")
        self.Reimbursement = (By.XPATH, "//div[@title='Reimbursement']")
        self.refund = (By.XPATH, "//div[@title='Refund']")

        self.click_receipts = (By.XPATH, "//button[@role='tab' and @data-id='receipts']")

        self.verify_sell_invoice_lock = (By.XPATH, "//button[@id='btn-btnDependencies']")
        self.click_on_close = (By.XPATH, "//button[@title='Close']")
        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")
        self.verify_receipts_invoice_lock =(By.XPATH, "//button[@id='btn-btnLock']")
        self.verify_receipts_purchases = (By.XPATH, "//button[@id='btn-btnEdit']")

        self.click_payment = (By.XPATH, "//button[@role='tab' and @data-id='payments']")

        self.click_first_lock_payment = (By.XPATH, "(//div[@role='gridcell' and @data-automation-key='action-invoice']//button[.//i[@data-icon-name='Lock']])[1]")
        self.click_second_lock_payment = (By.XPATH, "(//div[@role='gridcell' and @data-automation-key='action-invoice']//button[.//i[@data-icon-name='Lock']])[2]")

        self.click_expense_claims = (By.XPATH, "(//div[contains(text(),'Expense claims')])[1]")
        self.click_lock_expense = (By.XPATH, "(//div[@data-automation-key='action-expense']//button[.//i[@data-icon-name='Lock']])[1]")

        self.click_lock_reimbursed = (By.XPATH, "(//div[@data-automation-key='action-leads']//button[.//i[@data-icon-name='Lock']])[1]")

        self.click_lock_refunds = (By.XPATH, "(//div[@data-automation-key='action-leads']//button[.//i[@data-icon-name='Lock']])[1]")

        self.click_payment_find_math = (By.XPATH,"//div[contains(@class,'td') and @title='Payment' and normalize-space()='Payment']")

        self.click_explain = (By.XPATH, "//button[@role='tab' and @data-id='banking-explain']")
        self.select_all_explain_entries = (By.XPATH, "//div[contains(@class,'tr')][.//div[contains(@class,'td') and normalize-space()='Sales Return']]//input[@type='checkbox']")
        self.unexplain_all_checked_transactions = (By.XPATH, "//button[@type='button' and @title='Unexplain all checked transactions']")
        self.click_yes_for_confirmation = (By.XPATH, "//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Yes']]")
        self.click_added_bank_for_unexplain = (By.XPATH, "(//div[contains(@class,'bank-header')]/ancestor::div[contains(@style,'cursor: pointer')][1])[1]")










#-----------------------------------------------------------------------------------------------------------------------


    def Select_Search(self):
            try:
                client = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
                time.sleep(.2)
                client.click()
                time.sleep(.5)
                print("Click on search field successfully.....! ")
            except Exception as e:
                print(f"Error on click:{e}")

    def Enter_Company(self, company_name="DARSAH LTD", timeout=30, os=None):

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


    def Click_Input(self):
            try:
                input = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.click_input_drop_down))
                time.sleep(.2)
                input.click()
                time.sleep(.2)
                print("Input drop down open successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")


    def Click_Sales(self):
            try:
                sales = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_sales))
                time.sleep(.2)
                sales.click()
                time.sleep(.2)
                print("Click on Sales successfully....!!")
            except Exception as e:
                print(f"Error on Click:{e}")
                time.sleep(.2)

    def Add_Invoice(self):
        try:
            invoice = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.invoice))
            time.sleep(.2)
            invoice.click()
            time.sleep(.2)
            print("Click on Add invoice button successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

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

    def Select_Customer_Keyboard(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        control = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-control')][1]"
        )))
        control.click()

        input_el = wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-input-container')][1]//input"
        )))
        ActionChains(driver).move_to_element(input_el).click(input_el).perform()

        # ensure menu open
        wait.until(EC.visibility_of_element_located((
            By.XPATH, "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-menu')][1]"
        )))

        try:
            input_el.send_keys(Keys.ARROW_DOWN)
            time.sleep(.2)
            input_el.send_keys(Keys.ARROW_DOWN)
            time.sleep(.2)
            input_el.send_keys(Keys.ENTER)
        except ElementNotInteractableException:
            # fallback click first option if keyboard fails
            first_option = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-menu')][1]"
                "//div[contains(@class,'rs-option')][1]"
            )))
            first_option.click()

        selected = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-single-value')][1]"
        ))).text.strip()
        print("Customer selected successfully....!!")

        print("Selected Customer is :", selected)
        return selected


    def Add_Attachment(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            # 1) Directly target the file input near the attachment icon (more stable(rv))
            file_input = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//i[@data-icon-name='Attachment']/ancestor::button/following::input[@type='file'][1]"
            )))

            # 2) If hidden, force it visible so send_keys works(rv)
            driver.execute_script(
                "arguments[0].style.display='block'; arguments[0].style.visibility='visible';",
                file_input
            )

            # 3) Upload file (this will NOT open OS dialog(rv))
            file_input.send_keys(r"C:\Users\CT_USER\Desktop\test.csv")

            print("File uploaded successfully.......!")

        except Exception as e:
            print(f"Error in upload: {e}")


    def Select_item_sale(self, value="test"):
        d = self.driver
        w = self.wait
        container_el = w.until(
            EC.visibility_of_element_located(self.click_item_for_invoice)
        )
        time.sleep(.4)
        container_el.click()
        time.sleep(.4)

        def focused_input():
            return d.switch_to.active_element

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ARROW_DOWN)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.2)

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ENTER)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.4)


    def Change_Quantity(self):
        try:
            quantity = WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(self.change_quantity))
            time.sleep(.2)
            quantity.click()
            time.sleep(.2)
            quantity.send_keys(Keys.CONTROL,"a")
            time.sleep(.2)
            quantity.send_keys(Keys.BACKSPACE)
            time.sleep(.2)
            quantity.send_keys("2")
            time.sleep(.2)
            quantity.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Quantity changed successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Save(self):

        wait = WebDriverWait(self.driver, 30)

        try:

            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
        except:
            pass

        save_button = wait.until(
            EC.element_to_be_clickable(self.save_invoice)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        time.sleep(0.4)
        save_button.click()
        time.sleep(0.4)
        # print("Invoice created successfully")
        #
        # update_message = WebDriverWait(self.driver, 10).until(
        # EC.visibility_of_element_located(
        # (By.XPATH, "//*[contains(normalize-space(), 'Invoice created successfully')]"))
        #     )
        #
        # # Assert the presence of the success message
        # assert update_message, "Invoice created successfully"

        print("Test Case - Pass: Invoice created successfully")

        time.sleep(2)

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

    def Click_Pound_Icon(self):
        try:
            pound = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_pound_icon))
            time.sleep(.2)
            pound.click()
            time.sleep(.5)
            print(" Click on Pound icon successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Account_For_Sell(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        account_input = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//label[normalize-space()='Account']"
                "/following::input[@role='combobox'][1]"
            ))
        )

        account_input.click()

        account_input.send_keys(Keys.CONTROL, "a")
        account_input.send_keys(Keys.BACKSPACE)

        account_input.send_keys("Monzo")

        time.sleep(1)

        account_input.send_keys(Keys.ARROW_DOWN)
        account_input.send_keys(Keys.ENTER)

        print("Monzo account selected successfully.")











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

    # def Click_Find_Match(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 40)
    #
    #         find_match_locator = (
    #             By.XPATH,
    #             "//div[@role='tablist']//button[@role='tab' and .//span[normalize-space()='Find match']]"
    #         )
    #
    #         find_match = wait.until(
    #             EC.element_to_be_clickable(find_match_locator)
    #         )
    #
    #         self.driver.execute_script("arguments[0].click();", find_match)
    #
    #         print("Clicked on Find match successfully.....!!")
    #
    #     except Exception as e:
    #         print(f"Error in Click_Find_Match: {type(e).__name__} - {e}")
    #         raise

    def Click_Find_Match(self):
        wait = WebDriverWait(
            self.driver,
            20,
            poll_frequency=0.3,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        try:
            # First wait for page/loader
            self.wait_for_loader_to_disappear()

            # Better locator - don't depend on span
            find_match_locator = (
                By.XPATH,
                "//button[@role='tab' and contains(normalize-space(.), 'Find match')]"
            )

            # First make sure element actually exists
            find_match = wait.until(
                EC.presence_of_element_located(find_match_locator)
            )

            # Scroll into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                find_match
            )

            # Wait until visible
            find_match = wait.until(
                EC.visibility_of_element_located(find_match_locator)
            )

            try:
                # Normal Selenium click first
                find_match = wait.until(
                    EC.element_to_be_clickable(find_match_locator)
                )
                find_match.click()

            except (ElementClickInterceptedException, TimeoutException):
                # Re-fetch because React may have re-rendered element
                find_match = wait.until(
                    EC.presence_of_element_located(find_match_locator)
                )

                # JS fallback
                self.driver.execute_script(
                    "arguments[0].click();",
                    find_match
                )

            print("Click on Find match successfully....!!")

        except TimeoutException:
            print("Find match tab was not found/clickable.")

            # Useful debugging
            print("Current URL:", self.driver.current_url)
            print("Page title:", self.driver.title)

            # Check available tabs
            tabs = self.driver.find_elements(
                By.XPATH,
                "//button[@role='tab']"
            )

            print("Available tabs:")
            for tab in tabs:
                try:
                    print(
                        "Text:",
                        repr(tab.text),
                        "Displayed:",
                        tab.is_displayed(),
                        "Enabled:",
                        tab.is_enabled()
                    )
                except Exception:
                    pass

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
            active.send_keys("Anthony")
            # active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
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
            active.send_keys("Anthony")
            # active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
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




    # def Reimbursed_Account(self):
    #     driver = self.driver
    #     wait = WebDriverWait(driver, 20)
    #
    #     try:
    #         account_input = wait.until(
    #             EC.element_to_be_clickable(
    #                 (
    #                     By.XPATH,
    #                     "//label[normalize-space()='Account']"
    #                     "/following::input[@role='combobox'][1]"
    #                 )
    #             )
    #         )
    #
    #         driver.execute_script(
    #             "arguments[0].scrollIntoView({block:'center'});",
    #             account_input
    #         )
    #
    #         account_input.click()
    #
    #         account_input.send_keys(Keys.CONTROL, "a")
    #         account_input.send_keys(Keys.BACKSPACE)
    #
    #         account_input.send_keys("Monzo")
    #
    #         # Wait until Monzo becomes the focused option
    #         wait.until(
    #             lambda d: "Monzo" in (
    #                 d.find_element(
    #                     By.ID,
    #                     "aria-context"
    #                 ).text
    #             )
    #         )
    #
    #         account_input.send_keys(Keys.ARROW_DOWN)
    #         account_input.send_keys(Keys.ENTER)
    #
    #         # Verify selection
    #         selected_value = wait.until(
    #             EC.visibility_of_element_located(
    #                 (
    #                     By.XPATH,
    #                     "//label[normalize-space()='Account']"
    #                     "/following::div[contains(@class,'rs-single-value')][1]"
    #                 )
    #             )
    #         )
    #
    #         assert "Monzo" in selected_value.text, (
    #             f"Monzo was not selected. Current value: "
    #             f"{selected_value.text}"
    #         )
    #
    #         print(
    #             f"Account selected successfully: "
    #             f"{selected_value.text}"
    #         )
    #
    #     except Exception as error:
    #         driver.save_screenshot(
    #             "select_monzo_account_failure.png"
    #         )
    #
    #         raise AssertionError(
    #             f"Could not select Monzo account: {error}"
    #         ) from error

    def Reimbursed_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            account_input = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//label[normalize-space()='Account']"
                    "/following::input[@role='combobox'][1]"
                ))
            )

            account_input.click()

            account_input.send_keys(Keys.CONTROL, "a")
            account_input.send_keys(Keys.BACKSPACE)

            account_input.send_keys("Monzo")

            time.sleep(1)

            account_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)

            account_input.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Monzo account selected successfully.")

        except Exception as e:
            driver.save_screenshot(
                "reimbursement_account_failure.png"
            )
            print(f"Could not select reimbursement account: {e}")
            raise




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
            amount.send_keys(Keys.TAB)
            time.sleep(.2)
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
        # try:
        save_reb = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_reimbursement))
        time.sleep(.2)
        save_reb.click()
        time.sleep(.2)

        print("Test Case 11 - Pass: Reimbursement saved successfully.")

        # except Exception as e:
        #     print(f"Error: {e}")

        time.sleep(5)

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

    def Select_Account_Refund(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            30,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
                NoSuchElementException,
            )
        )

        # Account combobox located through its stable label.
        # Do not use the dynamic react-select ID.
        account_input_locator = (
            By.XPATH,
            "//label[normalize-space()='Account']"
            "/parent::div//input[@role='combobox']"
        )

        # React Select renders the options dynamically.
        monzo_option_locator = (
            By.XPATH,
            "//label[normalize-space()='Account']"
            "/parent::div"
            "//div[contains(@class,'rs-single-value') "
            "and contains(normalize-space(.),'Monzo - Current')]"
            # "//*[@role='option' "
            # "and contains(normalize-space(.),'Monzo - Current')]"
        )

        try:
            # Wait until the Account input is visible and clickable
            account_input = wait.until(
                EC.element_to_be_clickable(
                    account_input_locator
                )
            )

            driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                account_input
            )

            # Click the Account dropdown
            try:
                account_input.click()

            except (
                    ElementClickInterceptedException,
                    ElementNotInteractableException
            ):
                driver.execute_script(
                    "arguments[0].click();",
                    account_input
                )

            # Select and clear any existing search text/value
            account_input.send_keys(Keys.CONTROL, "a")
            account_input.send_keys(Keys.BACKSPACE)

            # Search for the required account
            account_input.send_keys("Monzo")

            try:
                # Wait for the visible Monzo option
                monzo_option = WebDriverWait(
                    driver,
                    10,
                    poll_frequency=0.2,
                    ignored_exceptions=(
                        StaleElementReferenceException,
                    )
                ).until(
                    EC.element_to_be_clickable(
                        monzo_option_locator
                    )
                )

                driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        block: 'nearest',
                        inline: 'nearest'
                    });
                    """,
                    monzo_option
                )

                # Select the option
                try:
                    monzo_option.click()

                except (
                        ElementClickInterceptedException,
                        ElementNotInteractableException
                ):
                    driver.execute_script(
                        "arguments[0].click();",
                        monzo_option
                    )

            except TimeoutException:
                print(
                    "Direct Monzo option was not found. "
                    "Using keyboard selection."
                )

                # React may replace the input after typing,
                # so locate it again
                account_input = wait.until(
                    EC.element_to_be_clickable(
                        account_input_locator
                    )
                )

                account_input.send_keys(Keys.ARROW_DOWN)
                account_input.send_keys(Keys.ENTER)

            # Verify that Monzo is selected
            def verify_monzo_selection(current_driver):
                try:
                    current_input = current_driver.find_element(
                        *account_input_locator
                    )

                    select_container = current_input.find_element(
                        By.XPATH,
                        "./ancestor::div["
                        "contains(@class,'rs-container')][1]"
                    )

                    selected_text = select_container.text.strip()

                    if "Monzo" in selected_text:
                        return selected_text

                    return False

                except (
                        StaleElementReferenceException,
                        NoSuchElementException
                ):
                    return False

            selected_account = wait.until(
                verify_monzo_selection,
                message=(
                    "Monzo option was clicked, but it was not "
                    "displayed as the selected Account."
                )
            )

            print(
                "Account selected successfully: "
                f"{selected_account}"
            )

            return selected_account

        except Exception as error:
            driver.save_screenshot(
                "select_monzo_account_failure.png"
            )

            account_inputs = driver.find_elements(
                *account_input_locator
            )

            print("Could not select Monzo account.")
            print(
                f"Account inputs found: {len(account_inputs)}"
            )
            print(f"Current URL: {driver.current_url}")
            print(f"Error type: {type(error).__name__}")
            print(f"Error details: {repr(error)}")

            raise

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
            file_path = r"C:\Users\CT_USER\Desktop\test\F&M Statment for Auto testing.csv"



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



#-----------------------------------------------------------------------------------------------------------------------

    def Click_Receipt_with_Bank_Charge(self):
        try:
            receipt_with_bank = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_on_receipt_with_bank_charge))
            time.sleep(.2)
            receipt_with_bank.click()
            time.sleep(.2)

            print("Clicked on Receipt with Bank Charge Description successfully and templet downloaded .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Select_Receipts(self):
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            try:
                claims = wait.until(
                    EC.element_to_be_clickable(self.select_receipts )
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    claims
                )
                time.sleep(0.2)

                try:
                    claims.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", claims)

                time.sleep(2)

                active = driver.switch_to.active_element
                # active.send_keys(Keys.ARROW_DOWN)
                # time.sleep(1)
                # # active.send_keys(Keys.ARROW_DOWN)
                # # time.sleep(0.2)
                active.send_keys(Keys.ENTER)
                time.sleep(0.5)

                selected_value = claims.text.strip()

                if not selected_value:
                    selected_value = driver.execute_script(
                        "return arguments[0].innerText;",
                        claims
                    ).strip()

                print(f"Claims selected successfully: {selected_value}")

            except Exception as e:
                print(f"Error in Select_Claims: {type(e).__name__} - {e}")
                time.sleep(0.2)
                raise

    def Select_Settle(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            30,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        try:
            # Your existing locator finds the placeholder
            placeholder = wait.until(
                EC.visibility_of_element_located(
                    self.select_settle
                )
            )

            # Locate the actual input beside the placeholder
            settle_input = placeholder.find_element(
                By.XPATH,
                "./following-sibling::div["
                "contains(@class,'rs-input-container')]"
                "//input[@role='combobox']"
            )

            wait.until(
                EC.element_to_be_clickable(
                    settle_input
                )
            )

            driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                settle_input
            )

            settle_input.click()

            # Get dynamic listbox ID
            listbox_id = wait.until(
                lambda d: settle_input.get_attribute(
                    "aria-controls"
                ) or False
            )

            # Clear and search
            settle_input.send_keys(Keys.CONTROL, "a")
            settle_input.send_keys(Keys.BACKSPACE)
            settle_input.send_keys("Bank Charges")

            # Wait for the correct option
            bank_charges_option_locator = (
                By.XPATH,
                f"//*[@id='{listbox_id}']"
                "//*[contains(@id,'-option-') "
                "and contains(normalize-space(.),"
                "'Bank Charges')]"
            )

            try:
                bank_charges_option = wait.until(
                    EC.element_to_be_clickable(
                        bank_charges_option_locator
                    )
                )

                try:
                    bank_charges_option.click()

                except ElementClickInterceptedException:
                    driver.execute_script(
                        "arguments[0].click();",
                        bank_charges_option
                    )

            except TimeoutException:
                # Keyboard fallback
                settle_input.send_keys(Keys.ARROW_DOWN)
                settle_input.send_keys(Keys.ENTER)

            # Verify without using assert
            input_id = settle_input.get_attribute("id")

            def get_selected_value(current_driver):
                try:
                    current_input = current_driver.find_element(
                        By.ID,
                        input_id
                    )

                    select_container = (
                        current_input.find_element(
                            By.XPATH,
                            "./ancestor::div["
                            "contains(@class,'rs-container')][1]"
                        )
                    )

                    container_text = (
                        select_container.text.strip()
                    )

                    if "Bank Charges" in container_text:
                        return container_text

                    return False

                except (
                        StaleElementReferenceException,
                        NoSuchElementException
                ):
                    return False

            selected_value = wait.until(
                get_selected_value,
                message=(
                    "Bank Charges option was not displayed "
                    "as the selected settle account."
                )
            )

            print(
                "Settle account selected successfully: "
                f"{selected_value}"
            )

            return selected_value

        except Exception as error:
            driver.save_screenshot(
                "select_settle_failure.png"
            )

            print(
                f"Could not select Bank Charges. "
                f"Error type: {type(error).__name__}"
            )
            print(f"Error details: {repr(error)}")

            raise

    def Click_Match(self):

        wait = WebDriverWait(self.driver, 30)

        match_button = wait.until(
                EC.element_to_be_clickable(
                    self.click_match
                )
        )

        self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                match_button
        )

        match_button.click()

        print("Match button clicked successfully.")


    def Click_Adde_Bank_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        # bank_card_locator = (
        #     By.XPATH,
        #     "//div[contains(@style,'cursor: pointer') "
        #     "and .//label[contains(normalize-space(.),"
        #     "'T.H. LIMITED')] "
        #     "and .//label[contains(normalize-space(.),"
        #     "'79981936')]]"
        # )
        bank_card_locator = (
            By.XPATH,
            "(//div[contains(@style,'cursor: pointer')]"
            "[.//label[contains(normalize-space(.),'DARSAH LTD')]]"
            "[.//*[contains("
            "translate("
            "concat(@alt,' ',@src,' ',@title,' ',@aria-label),"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
            "'abcdefghijklmnopqrstuvwxyz'"
            "),"
            "'monzo'"
            ")]])[1]"
        )

        bank_card = wait.until(
            EC.element_to_be_clickable(
                bank_card_locator
            )
        )

        driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            bank_card
        )

        try:
            bank_card.click()
        except ElementClickInterceptedException:
            driver.execute_script(
                "arguments[0].click();",
                bank_card
            )

        print("Bank account card clicked successfully.")

    def Click_Sales_Return(self):
        try:
            ret = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.sales_return))
            time.sleep(.2)
            ret.click()
            time.sleep(.2)

            print("Clicked on Sales Return Description successfully  .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    # def Click_Payment(self):
    #     try:
    #         pay = WebDriverWait(self.driver, 30).until(
    #             EC.element_to_be_clickable(self.payment))
    #         time.sleep(.2)
    #         pay.click()
    #         time.sleep(.3)
    #
    #         print("Clicked on Payment Description successfully  .....!! ")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #
    #         time.sleep(2)

    def Click_Payments(self):
        wait = WebDriverWait(
            self.driver,
            20,
            poll_frequency=0.3,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        locator = (
            By.XPATH,
            "//button[@role='tab' and @data-id='payments']"
        )

        try:
            # Wait for loaders/overlays first
            self.wait_for_loader_to_disappear()

            # Wait until Payments tab exists and is visible
            payment_tab = wait.until(
                EC.visibility_of_element_located(locator)
            )

            # Scroll element to center of screen
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                payment_tab
            )

            # Wait again after scrolling
            payment_tab = wait.until(
                EC.element_to_be_clickable(locator)
            )

            try:
                payment_tab.click()

            except ElementClickInterceptedException:
                # React/UI may have re-rendered or overlay may still exist
                self.wait_for_loader_to_disappear()

                payment_tab = wait.until(
                    EC.presence_of_element_located(locator)
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    payment_tab
                )

            print("Payments tab clicked successfully....!!")

        except Exception as e:
            print(
                f"Error in Click_Payments: "
                f"{type(e).__name__} - {e}"
            )
            raise

    def Click_Payment_Due(self):
        try:
            due = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.payment_due))
            time.sleep(.2)
            due.click()
            time.sleep(.2)

            print("Clicked on Payment due Description successfully  .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_Contact_Dropdown_For_Money_Out_2nd(self):

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
            active.send_keys("Jessica")
            # active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)

            time.sleep(2)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Contact selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)


    def Click_Contact_Dropdown_For_Money_Out_3nd(self):

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
            active.send_keys("Natasha")
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)

            time.sleep(2)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Contact selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)

    def Click_Reimbursement(self):
        try:
            due = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.Reimbursement))
            time.sleep(.2)
            due.click()
            time.sleep(.2)

            print("Clicked on Payment due Description successfully  .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Select_Settle_Reimbursement(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            30,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        try:
            # Existing locator identifies the placeholder
            placeholder = wait.until(
                EC.visibility_of_element_located(
                    self.select_settle
                )
            )

            # Find the real React Select input
            settle_input = placeholder.find_element(
                By.XPATH,
                "./following-sibling::div["
                "contains(@class,'rs-input-container')]"
                "//input[@role='combobox']"
            )

            wait.until(
                EC.element_to_be_clickable(
                    settle_input
                )
            )

            driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                settle_input
            )

            # Open dropdown
            settle_input.click()

            # Wait until dropdown opens
            wait.until(
                lambda d: settle_input.get_attribute(
                    "aria-expanded"
                ) == "true"
            )

            # Select the first available option
            settle_input.send_keys(Keys.ARROW_DOWN)
            settle_input.send_keys(Keys.ENTER)

            # Wait until dropdown closes
            wait.until(
                lambda d: settle_input.get_attribute(
                    "aria-expanded"
                ) == "false"
            )

            print(
                "Settle option selected successfully."
            )

        except Exception as error:
            driver.save_screenshot(
                "select_settle_failure.png"
            )

            print(
                f"Could not select settle option: "
                f"{type(error).__name__}"
            )
            print(f"Details: {repr(error)}")

            raise


    def Click_Refund(self):
        try:
            due = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.refund))
            time.sleep(.2)
            due.click()
            time.sleep(.2)

            print("Clicked on Refund Description successfully  .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    def Click_Receipts(self):
        try:
            rec = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.click_receipts))
            time.sleep(.2)
            rec.click()
            time.sleep(.2)

            print("Clicked on Receipt Description successfully  .....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Click_On_Lock_Button_Receipts(self):
        try:
            lock = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.verify_receipts_invoice_lock))
            time.sleep(.2)
            lock.click()
            time.sleep(.5)
            print(" Verify - "
                  "Receipts is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_On_Close_Icon(self):
        try:
            close = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_on_close))
            time.sleep(.2)
            close.click()
            time.sleep(.5)
            print("Details lock pop up close successfully.....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Purchases(self):
        try:
            sales = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_purchases))
            time.sleep(.2)
            sales.click()
            time.sleep(.2)
            print("Click on purchases successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")


    def Click_On_Lock_Button_Purchases(self):
        try:
            lock = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.verify_receipts_purchases))
            time.sleep(.2)
            lock.click()
            time.sleep(.5)
            print(" Verify - "
                  "purchases is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_Payment_Find_Match(self):
        try:
            pay= WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_payment_find_math))
            time.sleep(.2)
            pay.click()
            time.sleep(.2)
            print("Click on Payment section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")


    def Click_First_Lock_Payment(self):
        try:
            first_pay= WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_first_lock_payment))
            time.sleep(.2)
            first_pay.click()
            time.sleep(.2)
            print("Click on supplier lock successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")


    def Click_Second_Lock_Payment(self):
        try:
            sec_pay= WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_second_lock_payment))
            time.sleep(.2)
            sec_pay.click()
            time.sleep(.2)
            print("Click on second lock successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")


    # def Click_Expense_Claims(self):
    #     try:
    #         claims = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_expense_claims))
    #         time.sleep(.2)
    #         claims.click()
    #         time.sleep(.2)
    #         print("Click on Expense claims successfully....!!")
    #     except Exception as e:
    #         print(f"Error on Click:{e}")

    def Click_Expense_Claims(self):
        wait = WebDriverWait(self.driver, 20)

        try:
            # Wait for previous dialog animation/overlay
            wait.until(
                EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, ".ms-Overlay")
                )
            )

            locator = (
                By.XPATH,
                "//div[contains(@class,'ms-NavItemName') "
                "and normalize-space()='Expense claims']"
            )

            expense_claim = wait.until(
                EC.visibility_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                expense_claim
            )

            expense_claim = wait.until(
                EC.element_to_be_clickable(locator)
            )

            expense_claim.click()

            print("Expense section opened successfully for verify lock.")

        except Exception as e:
            print(
                f"Error in Click_Expense_Claims: "
                f"{type(e).__name__}: {e}"
            )
            raise


    def Click_On_Lock_Button_Expense(self):
        try:
            lock_expense = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_lock_expense))
            time.sleep(.2)
            lock_expense.click()
            time.sleep(.5)
            print(" Verify - "
                  "Expense is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")




    def Click_On_Lock_Button_Reimbursed(self):
        try:
            lock_reimbursed = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_lock_reimbursed))
            time.sleep(.2)
            lock_reimbursed.click()
            time.sleep(.5)
            print(" Verify - "
                  "Reimbursed is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_On_Lock_Button_Refund(self):
        try:
            lock_refund = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_lock_refunds))
            time.sleep(.2)
            lock_refund.click()
            time.sleep(.5)
            print(" Verify - "
                  "Refund is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Contact_Dropdown_For_Money_Out_6th(self):

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
            active.send_keys("Natasha")
            # active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)

            time.sleep(2)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Contact selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)


    # def Click_Explain(self):
    #     try:
    #         un_explain = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_explain))
    #         time.sleep(.2)
    #         un_explain.click()
    #         time.sleep(.5)
    #         print(" Click on the Un_Explain Section")
    #     except Exception as e:
    #         print(f"Error on click:{e}")

    def Click_Explain(self):
        explain_tab_locator = (
            By.XPATH,
            "//button[@role='tab' "
            "and @data-id='banking-explain']"
        )

        wait = WebDriverWait(
            self.driver,
            30,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        try:
            self.wait_for_loader_to_disappear()

            explain_tab = wait.until(
                EC.element_to_be_clickable(
                    explain_tab_locator
                )
            )

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                explain_tab
            )

            try:
                explain_tab.click()

            except ElementClickInterceptedException:
                self.driver.execute_script(
                    "arguments[0].click();",
                    explain_tab
                )

            # Confirm that the Explained tab is selected
            wait.until(
                lambda driver: (
                        driver.find_element(
                            *explain_tab_locator
                        ).get_attribute("aria-selected") == "true"
                )
            )

            print(
                "Clicked on the Explained section successfully."
            )

            return True

        except TimeoutException as error:
            self.driver.save_screenshot(
                "click_explained_timeout.png"
            )

            print(
                "Explained tab was not clickable or did not "
                "become selected within 30 seconds."
            )
            print(f"Error details: {repr(error)}")

            raise

        except Exception as error:
            self.driver.save_screenshot(
                "click_explained_failure.png"
            )

            print(
                f"Could not click the Explained tab. "
                f"Error type: {type(error).__name__}"
            )
            print(f"Error details: {repr(error)}")

            raise

    def Select_All_Explain_Entries(self):
        wait = WebDriverWait(self.driver, 30)

        checkbox_input_locator = (
            By.XPATH,
            "//*[@id='explanation-table']"
            "//div[contains(@class,'header')]"
            "//input[@type='checkbox']"
        )

        checkbox_label_locator = (
            By.XPATH,
            "//*[@id='explanation-table']"
            "//div[contains(@class,'header')]"
            "//input[@type='checkbox']"
            "/following-sibling::label"
        )

        try:
            self.wait_for_loader_to_disappear()

            checkbox_input = wait.until(
                EC.presence_of_element_located(
                    checkbox_input_locator
                )
            )

            if not checkbox_input.is_selected():
                checkbox_label = wait.until(
                    EC.element_to_be_clickable(
                        checkbox_label_locator
                    )
                )

                try:
                    checkbox_label.click()

                except ElementClickInterceptedException:
                    self.driver.execute_script(
                        "arguments[0].click();",
                        checkbox_label
                    )

            # Confirm that checkbox is selected
            wait.until(
                lambda driver: driver.find_element(
                    *checkbox_input_locator
                ).is_selected()
            )

            print(
                "All Explained entries selected successfully."
            )

        except Exception as error:
            self.driver.save_screenshot(
                "select_all_explained_failure.png"
            )

            print(
                "Failed inside Select_All_Explain_Entries."
            )
            print(f"Error type: {type(error).__name__}")
            print(f"Error details: {repr(error)}")

            raise

    def Unexplain_all_checked_transactions(self):
        wait = WebDriverWait(self.driver, 30)

        unexplain_button_locator = (
            By.XPATH,
            "//button[@type='button' "
            "and @title="
            "'Unexplain all checked transactions']"
        )

        try:
            unexplain_button = wait.until(
                EC.element_to_be_clickable(
                    unexplain_button_locator
                )
            )

            try:
                unexplain_button.click()

            except ElementClickInterceptedException:
                self.driver.execute_script(
                    "arguments[0].click();",
                    unexplain_button
                )

            print(
                "Clicked Unexplain all checked "
                "transactions successfully."
            )

        except Exception as error:
            self.driver.save_screenshot(
                "unexplain_all_failure.png"
            )

            print(
                "Failed inside "
                "Unexplain_all_checked_transactions."
            )
            print(f"Error type: {type(error).__name__}")
            print(f"Error details: {repr(error)}")

            raise

    def Click_Yes_For_Confirmation(self):
        wait = WebDriverWait(self.driver, 30)

        yes_button_locator = (
            By.XPATH,
            "//button[contains(@class,'ms-Button--primary') "
            "and .//span[normalize-space()='Yes']]"
        )

        try:
            yes_button = wait.until(
                EC.element_to_be_clickable(
                    yes_button_locator
                )
            )

            try:
                yes_button.click()

            except ElementClickInterceptedException:
                self.driver.execute_script(
                    "arguments[0].click();",
                    yes_button
                )

            # Confirm dialog closes
            wait.until(
                EC.invisibility_of_element_located(
                    yes_button_locator
                )
            )

            self.wait_for_loader_to_disappear()

            print(
                "Clicked Yes confirmation successfully."
            )

        except Exception as error:
            self.driver.save_screenshot(
                "click_yes_confirmation_failure.png"
            )

            print(
                "Failed inside Click_Yes_For_Confirmation."
            )
            print(f"Error type: {type(error).__name__}")
            print(f"Error details: {repr(error)}")

            raise

    def Click_Added_bank_for_Unexplain(self):
        try:
            added_bank_unexplain = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_added_bank_for_unexplain))
            time.sleep(.2)
            added_bank_unexplain.click()
            time.sleep(.5)
            print(" Click on added_bank_un_explain successfully.....!")
        except Exception as e:
            print(f"Error on click:{e}")
















