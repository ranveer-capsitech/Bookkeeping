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
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

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


class Banking_detailed_explaination:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH, "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH,"//a[@title='RDX LIMITED' and contains(@href,'/books/clients/')]")


        # self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_purchase = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

        self.click_suppliers = (By.XPATH, "//button[@role='tab'][.//span[normalize-space()='Suppliers']]")
        self.add_suppliers_button = (By.XPATH, "//span[normalize-space()='Supplier']")
        self.enter_supplier_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")

        self.click_billing_field = (By.XPATH,
                                    "//label[normalize-space()='Billing address']/following::label[normalize-space()='Building, Street, City'][1]")

        self.enter_building_no = (By.XPATH, "//input[@placeholder='Building']")
        self.enter_street = (By.XPATH, "//input[@placeholder='Street']")
        self.enter_city = (By.XPATH, "//input[@placeholder='City']")
        # self.county_details = (By.XPATH,
        #                        "//label[normalize-space()='Billing address']/following::label[normalize-space()='County, Country, Postcode'][1]")
        self.enter_county = (By.XPATH, "//input[@placeholder='County']")
        self.select_country = (By.XPATH,
                               "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]")

        self.postcode = (By.XPATH,
                         "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/input[1]")

        self.click_contact_person = (By.XPATH,
                                     "//label[normalize-space()='Contact person']/following::input[@type='text'][1]")

        self.first_name = (By.XPATH,
                           "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")

        self.name = (By.XPATH,
                     "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")

        self.contact_number = (By.XPATH, "//i[@data-icon-name='Mobile']/following::input[1]")

        self.enter_mail = (By.XPATH, "//i[@data-icon-name='Envelope']/following::input[1]")

        self.account_name = (By.XPATH,
                             "//label[normalize-space()='Account name']/following::input[@type='text'][1]")

        self.vat = (By.XPATH,
                    "//label[normalize-space()='VAT number']/following::input[contains(@id,'react-select') and contains(@id,'-input')][1]")

        self.enter_vat = (By.XPATH,
                          "//label[normalize-space()='VAT number']/following::input[contains(@class,'ms-TextField-field')][1]")

        self.enter_eori = (By.XPATH,
                           "//label[normalize-space()='EORI number']/following::input[contains(@class,'ms-TextField-field')][1]")

        self.sort_code = (By.XPATH, "//label[normalize-space()='Sort code']/following::input[@type='text'][1]")

        self.account = (By.XPATH, "//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Account']]")

        self.project_tags = (By.XPATH,
                             "//label[normalize-space()='Project tags']/following::input[@role='combobox'][1]")

        self.attachment = (By.XPATH, "//i[@data-icon-name='Attachment' and @aria-label='Attachment']")

        self.save_supplier = (By.XPATH, "//button[@type='submit']//span[normalize-space()='Save']")

        # dropdown control (click area)
        self.select_country_control = (By.XPATH,
                                       "//label[normalize-space()='Country']/following::div[contains(@class,'rs-control')][1]")

        # actual input where typing happens (react-select input)
        self.select_country_input = (By.XPATH,
                                     "//label[normalize-space()='Country']/following::input[contains(@id,'react-select') and contains(@id,'-input')][1]")

        self.invoice = (By.XPATH, "(//span[contains(text(),'Invoice')])[1]")
        self.click_item_for_invoice = (By.XPATH,
                                       "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.table = (By.XPATH, " (//div[contains(text(),'Tables')])[1]")

        self.save_invoice = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.add_discount = (By.XPATH, "//input[@name='discount']")

        self.click_for_enter_note = (By.XPATH,
                                     "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note = (By.XPATH,
                          "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.allocate_save_button = (By.XPATH, "//div[@role='dialog']//button[.//span[normalize-space()='Save']]")

        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")

        self.invoice = (By.XPATH, "//button[@aria-label='btnInvoice']")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")

        self.click_item_for_invoice = (By.XPATH,
                                       "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

        self.net_amount = (By.XPATH, "(//table[contains(@class,'table')]//input[contains(@name,'amount.net')])[1]")

        self.loc_save_button = (By.XPATH, "//div[contains(@class,'modal')]//span[normalize-space(text())='Save']")

        self.banking_section = (By.XPATH, "//div[contains(text(),'Banking')]")

        self.select_bank = (By.XPATH,
                            "//label[normalize-space()='Bank']/following::div[contains(@class,'rs-input-container')][1]")

        self.enter_credit_card_number = (By.XPATH,
                                         "//label[normalize-space()='Credit card number']/following::input[1]")

        self.save_account = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        self.select_credit_account = (By.XPATH,
                                      "(//div[contains(@style,'cursor: pointer') and .//*[normalize-space()='Reconciled'] and .//*[contains(normalize-space(),'Unexplained transactions')]])[1]")

        self.click_next_button = (By.XPATH, "//span[contains(text(),'Next')]")
        self.upload_import = (By.XPATH,
                              "//div[contains(@class,'ao-modal-container')]//button[.//span[normalize-space()='Import']]")

        self.click_templet = (By.XPATH, "//span[contains(text(),'Template')]")

        self.click_import = (By.XPATH, "//span[contains(text(),'Import')]")

        self.back_button = (
            By.XPATH,
            "//button[@title='Bank Dashboard']//i[@data-icon-name='ChromeBack']/ancestor::button[1]"
        )

        self.add_manual_transaction = (By.XPATH,
            "//button[@title='Add manual transactions']//i[@data-icon-name='Add']/ancestor::button[1]")

        self.enter_date = (By.XPATH, "//input[@name='transactions.0.date']/following::i[@data-icon-name='Calendar'][1]")
        self.first_description = (By.XPATH,"//input[@name='transactions.0.description']")
        self.enter_money_out = (By.XPATH, "//div[@role='dialog']//input[@name='transactions.0.moneyOut']")
        self.click_save_manual_transaction = (By.XPATH, "//div[@role='dialog' and .//*[normalize-space()='Add manual transactions']]//button[.//span[normalize-space()='Save']]")
        self.money_out_value = (
            By.XPATH,
            "//div[contains(@class,'itemContainer') and .//*[contains(normalize-space(),'PAYMENT RECEIVED -- THANK')]]"
            "//div[contains(@class,'td-focus')][4]"
        )
        self.click_find_match = (By.XPATH, "//button[@role='tab' and .//span[normalize-space()='Find match']]")

        self.click_contact_dropdown = (By.XPATH,"//label[normalize-space()='Contact']/following::div[contains(@class,'rs-indicators-container')][1]")

        self.select_claims = (By.XPATH, "//input[@name='invoices.0']/preceding-sibling::div[contains(@class,'rs-control')][1]")
        self.enter_allocated_amount = (By.XPATH, "//input[@name='invoices.0.amount']")
        self.click_match = (By.XPATH, "//span[contains(text(),'Match')]")
        self.click_attachment_icon = (By.XPATH, "//label[normalize-space()='Contact']/following::button[.//i[@data-icon-name='attachment']][1]")
        self.drag_drop_file = (By.XPATH, "//span[contains(text(),'Drag & drop files here or ')]")
        self.click_explain = (By.XPATH, "//button[@role='tab']//span[normalize-space()='Explain']/ancestor::button")
        self.contact_name_dropdown = (
            By.XPATH,
            "//label[normalize-space()='Contact name']/following::div[contains(@class,'rs-control') and .//div[normalize-space()='Select']][1]"
        )
        self.explain_submit_button = (
            By.XPATH,
            "//div[contains(@class,'linked-transaction')]"
    "//button[contains(@class,'ms-Button--primary') and not(@disabled) and .//span[normalize-space()='Explain']]"
        )
        # self.transfer_section = (By.XPATH, "//button[contains(@id,'Pivot') and @role='tab' and .//span[normalize-space()='Transfer']]")
        #
        # self.transfer_select_account_dropdown = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        #
        # # self.transfer_select_account_dropdown = (
        # #     By.XPATH,
        # #     "//div[@role='tabpanel' and @aria-hidden='false']//label[normalize-space()='Select account']/following::div[contains(@class,'rs-control')][1]"
        # # )
        #
        # self.transfer_submit_button = (
        #     By.XPATH,
        #     "//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Transfer']]"
        # )

        self.transfer_section = (
            By.XPATH,
            "//button[@role='tab' and @data-content='Transfer']"
        )

        self.transfer_select_account_dropdown = (
            By.XPATH,
            "//div[@role='tabpanel' and @aria-hidden='false']"
            "//label[normalize-space()='Select account']"
            "/following::div[contains(@class,'rs-control')][1]"
        )

        self.transfer_select_account_input = (
            By.XPATH,
            "//div[@role='tabpanel' and @aria-hidden='false']"
            "//label[normalize-space()='Select account']"
            "/following::input[@role='combobox'][1]"
        )








    #------------------------------------------- Method---------------------------------------------------------------------


    def Select_Search(self):
            try:
                client = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
                time.sleep(.2)
                client.click()
                time.sleep(.5)
                print("Click on search field successfully.....! ")
            except Exception as e:
                print(f"Error on click:{e}")



    def Enter_Company(self, company_name="RDX LIMITED", timeout=30, os=None):

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


    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)
            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_Sales(self):
        try:
            sales = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_sales))
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




    def Select_Customer_Keyboard(self):
        driver = self.driver
        wait = WebDriverWait(driver, 40)

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
            file_input.send_keys(r"C:\Users\CT_USER\Desktop\test\Revolut Template.csv")

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


    def Enter_Discount(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)

        try:
            control = wait.until(EC.visibility_of_element_located(self.add_discount))
            time.sleep(.2)
            control.click()
            time.sleep(.2)
            control.send_keys("10")
            time.sleep(.2)
            print("Discount added successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")


    def Click_Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_note))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)


            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Click_Save(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            save_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[.//span[normalize-space()='Save'] and not(@disabled)]"
                ))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                save_button
            )

            time.sleep(0.5)

            self.driver.execute_script("arguments[0].click();", save_button)

            print("Clicked on Save button successfully")

            # wait for any success toast/message
            success_message = wait.until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//*[contains(normalize-space(),'created successfully') "
                    "or contains(normalize-space(),'Invoice created') "
                    "or contains(normalize-space(),'saved successfully') "
                    "or contains(normalize-space(),'Invoice saved')]"
                ))
            )

            assert success_message.is_displayed(), "Success message not displayed"
            print("Test Case Create Invoice - Pass:")

            # print("Test Case Create Invoice - Pass:", success_message.text)

            time.sleep(2)

        except Exception as e:
            print(f"Error in Click_Save: {type(e).__name__} - {e}")
            raise
#-----------------------------------------------Purchase----------------------------------------------------------------




    def Click_Purchases(self):
        try:
            sales = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_purchases))
            time.sleep(.2)
            sales.click()
            time.sleep(.2)
            print("Click on purchases successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")



    def Add_Invoice(self):

        try:
            invoice = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(self.invoice))
            time.sleep(.2)
            invoice.click()
            time.sleep(.2)
            print("Click on Add invoice button successfully....!!")


        except Exception as e:
            print(f"Error on Click : {e}")



    def Select_Customer(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            dropdown_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='react-select-'][id$='-input']"))
            )
            time.sleep(.2)
            dropdown_input.click()
            time.sleep(.2)
            dropdown_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ENTER)
            time.sleep(0.5)

            time.sleep(.2)
            #dropdown_input.send_keys(Keys.ENTER)
            time.sleep(.5)
            print("Customer selected successfully....!!")

        except Exception as e:
            print(f"Error on Click : {e}")



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



    def Enter_Discount(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)

        try:
            control = wait.until(EC.visibility_of_element_located(self.add_discount))
            time.sleep(.2)
            control.click()
            time.sleep(.2)
            control.send_keys("10")
            time.sleep(.2)
            print("Discount added successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")


    def Click_Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_note))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)


            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")






    def Select_item_purchase(self, value="test"):
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
                time.sleep(2)

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ENTER)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.4)


    def Enter_amount(self):
        try:
            amount = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.net_amount))
            time.sleep(.2)
            amount.send_keys("100")
            time.sleep(.2)
            print("Enter amount successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")


    def Save_Services(self):
        wait = WebDriverWait(self.driver, 30)

        try:

            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
        except:
            pass

        save_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']/ancestor::button"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        time.sleep(0.4)
        save_button.click()
        time.sleep(0.4)
        print("Invoice created successfully")
        try:
            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Invoice created successfully')]")
                )
            )
        except TimeoutException:
            raise AssertionError(
                "Expected 'Invoice created successfully' toast but did not see it."
            )

        assert update_message.is_displayed(), "Invoice created successfully"
        print("Test Case - :  Pass:: Invoice created successfully.")


#-------------------------------------------Banking---------------------------------------------------------------------

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

        wait = WebDriverWait(self.driver, 30)

        for attempt in range(3):
            try:
                credit_account = wait.until(
                    EC.element_to_be_clickable(self.select_credit_account)
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    credit_account
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    credit_account
                )

                print("Click on Credit account section successfully.")
                return

            except StaleElementReferenceException:
                print(f"Stale element detected. Retry {attempt + 1}/3")
                time.sleep(1)

        raise Exception("Unable to click Credit Account after retries.")

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

    def Click_Back_Button(self):
        try:
            back_btn = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.back_button))
            time.sleep(.2)
            back_btn.click()
            time.sleep(.2)

            print("Clicked on Back button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Add_Manual_Transaction(self):
        try:
            manual_transaction = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.add_manual_transaction))
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
                    "//input[@name='transactions.0.date']"
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

    def Enter_Money_Out(self, moneyout="100"):
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

    def Click_Save_Manual_Transaction(self):
        try:
            save_manual_transaction = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_save_manual_transaction))
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
    #
    # def Money_Out_Value(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 30)
    #
    #         first_row = wait.until(
    #             EC.presence_of_element_located((
    #                 By.XPATH,
    #                 "(//div[contains(@class,'bkDetailList')]//label[normalize-space()='Manual'])[1]"
    #             ))
    #         )
    #
    #         self.driver.execute_script(
    #             "arguments[0].scrollIntoView({block:'center'});",
    #             first_row
    #         )
    #
    #         time.sleep(0.5)
    #
    #         self.driver.execute_script(
    #             "arguments[0].click();",
    #             first_row
    #         )
    #
    #         print("First transaction row clicked successfully.")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         raise

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


    def Click_Contact_Dropdown(self):

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
                active.send_keys("KM Consultancy Limited")
                # active.send_keys(Keys.ARROW_DOWN)
                # time.sleep(0.2)
                # active.send_keys(Keys.ARROW_DOWN)
                # time.sleep(0.2)
                # active.send_keys(Keys.ARROW_DOWN)
                # time.sleep(0.2)
                # active.send_keys(Keys.ARROW_DOWN)
                time.sleep(2)
                active.send_keys(Keys.ENTER)
                time.sleep(1)

                print("Contact selected successfully....!!")

            except Exception as e:
                print(f"Error in Select_Bank: {e}")
                time.sleep(0.2)


    def Select_Claims(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            claims = wait.until(
                EC.element_to_be_clickable(self.select_claims)
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

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)
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


    def Enter_Allocated_Amount(self, money="100"):

            # try:
                wait = WebDriverWait(self.driver, 30)

                amount = wait.until(
                    EC.element_to_be_clickable(self.enter_allocated_amount))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                    amount
                )

                self.driver.execute_script("arguments[0].click();", amount)

                amount.send_keys(Keys.CONTROL + "a")
                amount.send_keys(Keys.BACKSPACE)
                amount.send_keys(money)

                print(f"Allocated amount entered successfully: {money}")

            # except Exception as e:
            #     print(f"Error in Enter_Description: {type(e).__name__} - {e}")
            #     raise

    def Click_Match(self):
        # try:
            match = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_match))
            time.sleep(1)
            match.click()
            time.sleep(1)

            print("Clicked on match button successfully.....!! ")

        # except Exception as e:
        #     print(f"Error: {e}")

            time.sleep(2)

    def Click_Attachment_Icon(self):
        try:
            attachment = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_attachment_icon))
            time.sleep(.2)
            attachment.click()
            time.sleep(.2)

            time.sleep(1)


            print("Clicked on attachment button successfully.....!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Drag_Drop_File(self, file_path=r"C:\Users\CT_USER\Desktop\test\Sample.CSV.xlsx"):
                try:
                    wait = WebDriverWait(self.driver, 30)

                    if not os.path.exists(file_path):
                        raise FileNotFoundError(f"File not found: {file_path}")

                    for attempt in range(3):
                        try:
                            drag_drop = wait.until(
                                EC.element_to_be_clickable(self.drag_drop_file)
                            )

                            self.driver.execute_script(
                                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                                drag_drop
                            )

                            time.sleep(0.5)

                            try:
                                drag_drop.click()
                            except ElementClickInterceptedException:
                                self.driver.execute_script("arguments[0].click();", drag_drop)

                            time.sleep(1)

                            pyautogui.write(file_path)
                            time.sleep(0.5)
                            pyautogui.press("enter")

                            print(f"Attachment file added successfully: {file_path}")
                            return

                        except StaleElementReferenceException:
                            print(f"Stale element retry {attempt + 1}/3")
                            time.sleep(1)

                    raise Exception("Unable to upload attachment after retries")

                except Exception as e:
                    print(f"Error in Drag_Drop_File: {type(e).__name__} - {e}")
                    raise




    def Click_Explain(self):
        try:
            explain = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_explain))
            time.sleep(.2)
            explain.click()
            time.sleep(.2)
            print("Click on Explain section successfully....!!")
        except Exception as e:
            print(f"Error: {e}")


    def Contact_Name_Dropdown(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            contact_name = wait.until(EC.element_to_be_clickable(self.contact_name_dropdown))

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                contact_name
            )
            time.sleep(0.2)

            try:
                contact_name.click()
            except ElementClickInterceptedException:

                driver.execute_script("arguments[0].click();",  contact_name)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys("Alex")
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)

            time.sleep(2)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Explain Contact selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)



    def Select_Account_Head(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            account_head = wait.until(EC.element_to_be_clickable(self.contact_name_dropdown))

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                account_head
            )
            time.sleep(0.2)

            try:
                account_head.click()
            except ElementClickInterceptedException:

                driver.execute_script("arguments[0].click();", account_head)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys("Telephone & internet")
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(0.2)

            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Account head selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Bank: {e}")
            time.sleep(0.2)



    def Explain_Submit_Button(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            explain_submit_locator = (
                By.XPATH,
                "//label[normalize-space()='Description']"
                "/following::button[.//span[normalize-space()='Explain']][1]"
            )

            # wait until button exists
            explain_submit = wait.until(
                EC.presence_of_element_located(explain_submit_locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                explain_submit
            )

            time.sleep(1)

            # if button disabled, print and stop
            disabled = explain_submit.get_attribute("disabled")
            aria_disabled = explain_submit.get_attribute("aria-disabled")

            print("Explain disabled:", disabled)
            print("Explain aria-disabled:", aria_disabled)

            if disabled or aria_disabled == "true":
                raise Exception(
                    "Explain button is disabled. Please select required fields: Contact name, Account head, and VAT."
                )

            self.driver.execute_script("arguments[0].click();", explain_submit)

            print("Click on Explain submit button successfully....!!")

        except Exception as e:
            print(f"Error in Explain_Submit_Button: {type(e).__name__} - {e}")
            raise



    def Click_Transfer_Section(self):
        wait = WebDriverWait(self.driver, 30)

        transfer = wait.until(
            EC.element_to_be_clickable(self.transfer_section)
        )

        self.driver.execute_script("arguments[0].click();", transfer)

        wait.until(
            EC.presence_of_element_located(self.transfer_select_account_dropdown)
        )

        print("Clicked on Transfer section successfully.")


    def Select_Transfer_Account_Dropdown(self, account_name="Monzo - Current"):
        try:
            wait = WebDriverWait(self.driver, 40)

            dropdown = wait.until(
                EC.element_to_be_clickable(self.transfer_select_account_dropdown)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dropdown
            )

            self.driver.execute_script("arguments[0].click();", dropdown)

            input_box = wait.until(
                EC.presence_of_element_located(self.transfer_select_account_input)
            )

            self.driver.execute_script("arguments[0].focus();", input_box)

            input_box.send_keys(Keys.CONTROL + "a")
            input_box.send_keys(Keys.BACKSPACE)
            input_box.send_keys(account_name)

            time.sleep(1)

            # input_box.send_keys(Keys.ARROW_DOWN)
            input_box.send_keys(Keys.ENTER)
            time.sleep(.2)

            print(f"Transfer account selected successfully: {account_name}")

        except Exception as e:
            print(f"Error in Select_Transfer_Account_Dropdown: {type(e).__name__} - {e}")
            raise


    def Transfer_Submit_Button(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            transfer_btn_locator = (
                By.XPATH,
                "//div[@role='tabpanel' and @aria-hidden='false']"
                "//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Transfer']]"
            )

            for attempt in range(3):
                try:
                    transfer_btn = wait.until(
                        EC.presence_of_element_located(transfer_btn_locator)
                    )

                    print("Transfer button displayed:", transfer_btn.is_displayed())
                    print("Transfer button enabled:", transfer_btn.is_enabled())
                    print("Transfer button disabled attr:", transfer_btn.get_attribute("disabled"))
                    print("Transfer button text:", transfer_btn.text)

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                        transfer_btn
                    )

                    time.sleep(0.5)

                    # Re-fetch after scroll
                    transfer_btn = wait.until(
                        EC.element_to_be_clickable(transfer_btn_locator)
                    )

                    self.driver.execute_script("arguments[0].click();", transfer_btn)

                    print("Clicked on Transfer submit button successfully....!!")
                    return

                except StaleElementReferenceException:
                    print(f"Stale element retry {attempt + 1}/3")
                    time.sleep(1)

            raise Exception("Unable to click Transfer submit button after retries")

        except TimeoutException:
            buttons = self.driver.find_elements(
                By.XPATH,
                "//button[.//span[normalize-space()='Transfer']]"
            )

            print("Total Transfer buttons found:", len(buttons))

            for i, btn in enumerate(buttons, start=1):
                print(
                    f"Button {i}: text='{btn.text}', "
                    f"displayed={btn.is_displayed()}, "
                    f"enabled={btn.is_enabled()}, "
                    f"disabled={btn.get_attribute('disabled')}, "
                    f"aria-disabled={btn.get_attribute('aria-disabled')}"
                )

            raise

        except Exception as e:
            print(f"Error in Transfer_Submit_Button: {type(e).__name__} - {e}")
            raise



    # def Transfer_Submit_Button(self):
    #     # try:
    #         transfer_submit = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.transfer_submit_button))
    #         time.sleep(.2)
    #         transfer_submit.click()
    #         time.sleep(.2)
    #         print("Click on transfer submit section successfully....!!")
        # except Exception as e:
        #     print(f"Error: {e}")































