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
credit_card_no = fake.credit_card_number(card_type="visa")


class Detail_Explain_Filter:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH, "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH,"//a[@title='RDX LIMITED' and contains(@href,'/books/clients/')]")
        # self.click_company = (By.XPATH, "//a[@title='T.H. LIMITED' and contains(@href,'/books/clients/')]")
        # self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
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

        self.account = (By.XPATH,
                        "//button[contains(@class,'ms-Button--primary') and .//span[normalize-space()='Account']]")

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

        self.account = (By.XPATH, "//label[normalize-space()='Add account'] | //span[normalize-space()='Account']")
        self.select_bank = (By.XPATH,
                            "//label[normalize-space()='Bank']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_account_no = (By.XPATH, "//label[normalize-space()='Account no.']/following::input[1]")
        self.enter_sort_code = (By.XPATH, "//label[normalize-space()='Sort code']/following::input[1]")
        # self.enter_iban = (By.XPATH, "//label[normalize-space()='IBAN']/following::input[1]")
        self.click_primary_account = (By.XPATH, "//span[contains(text(),'Primary account')]")
        self.save_account = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        # -----------------Change date-------------------------------------------------------------------------------------------

        self.enter_from_date = (By.XPATH, "//input[@name='fromDate']")
        self.enter_to_date = (By.XPATH, "//input[@name='toDate']")
        self.refresh_icon = (By.XPATH, "//i[@data-icon-name='Refresh']/ancestor::button")

        # --------------------------Data filter----------------------------------------------------------------------------------

        self.click_data_filter_icon = (By.XPATH, "//i[@id='date-date-filter' and @data-icon-name='ChevronDown']")
        self.old_to_new = (By.XPATH, "//div[contains(@class,'ms-Callout')]//div[normalize-space()='Oldest to newest']")
        self.new_to_old = (By.XPATH, "//div[contains(@class,'ms-Callout')]//div[normalize-space()='Newest to oldest']")
        self.click_select_all_date = (By.XPATH,
                                      "//div[contains(@class,'ms-Callout')]//div[@data-is-focusable='true'][.//text()[normalize-space()='Select all']]//i[@data-icon-name='CheckMark']")
        self.first_option = (By.XPATH,
                             "(//div[@data-is-focusable='true'][normalize-space()='Select all']/following-sibling::div[@data-is-focusable='true'])[1]")
        self.second_option = (By.XPATH, "//div[@data-is-focusable='true' and normalize-space()='06/04/2024']")
        self.click_apply_button = (By.XPATH,
                                   "//button[contains(@class,'ms-Button--primary') and normalize-space()='Apply']")

        self.description_filter_icon = (By.XPATH, "//i[@id='desc-string-filter' and @data-icon-name='ChevronDown']")
        self.a_to_z = (By.XPATH, "//div[@data-is-focusable='true']//div[normalize-space()='A to Z']")
        self.z_to_a = (By.XPATH, "//div[@data-is-focusable='true']//div[normalize-space()='Z to A']")
        self.click_select_all_description = (By.XPATH,
                                             "//div[@data-is-focusable='true'][.//text()[normalize-space()='Select all']]")
        self.first_description = (By.XPATH,
                                  "//div[@data-is-focusable='true'][.//div[normalize-space()='EDF ENERGY-ECOM ON 31 MAR BDC']]")
        self.enter_data_search = (By.XPATH,
                                  "//div[contains(@class,'ms-TextField-fieldGroup')]//input[@title='Search term']")
        self.click_apply_for_des = (By.XPATH, "//span[normalize-space()='Apply']/ancestor::button")

        self.filter_icon_money_out = (By.XPATH, "//i[@data-icon-name='ChevronDown' and @id='mo-number-filter']")
        self.small_lest_to_largest = (By.XPATH,
                                      "//div[@data-is-focusable='true'][normalize-space()='Smallest to largest']")
        self.largest_to_smallest = (By.XPATH,
                                    "//div[@data-is-focusable='true'][normalize-space()='Largest to smallest']")
        self.click_apply_for_money_out = (By.XPATH, "//button[.//span[normalize-space()='Apply']]")

        self.filter_icon_money_in = (By.XPATH, "//i[@data-icon-name='ChevronDown' and @id='mi-number-filter']")
        self.small_lest_to_largest_mi = (By.XPATH,
                                         "//div[@data-is-focusable='true'][contains(normalize-space(.),'Smallest to largest')]")
        self.largest_to_smallest_mi = (By.XPATH,
                                       "//div[@data-is-focusable='true'][contains(normalize-space(.),'Largest to smallest')]")
        self.click_apply_mi = (By.XPATH, "//button[@id='ApplyBtn']//span[normalize-space()='Apply']")

        self.google_icon = (By.XPATH,
                            "(//section[contains(@class,'magnifier')]//i[@data-icon-name='googleMagnifier'])[1]")

        self.clear_data = (By.XPATH, "//i[@data-icon-name='Cancel' and @title='Clear sorts & filters']")

        self.change_vat = (By.XPATH,
                           "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[1]")
        self.change_vat_second = (By.XPATH,
                                  "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[1]/div[1]")


        self.enter_search = (By.XPATH, "//input[@placeholder='Search']")
        self.cancel_cross_button = (By.XPATH, "//i[@data-icon-name='Clear']")




    #-------------------------------------------------------------------------------------------------------------------------


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
            # def Enter_Company(self, company_name="T.H. LIMITED", timeout=30, os=None):

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
                invoice = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.invoice))
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

        # -----------------------------------------------Purchase----------------------------------------------------------------

    def Click_Purchases(self):
            try:
                sales = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_purchases))
                time.sleep(.2)
                sales.click()
                time.sleep(.2)
                print("Click on purchases successfully....!!")
            except Exception as e:
                print(f"Error on Click:{e}")

    def Add_Invoice(self):

            try:
                invoice = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.invoice))
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
                # dropdown_input.send_keys(Keys.ENTER)
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
                amount.send_keys("100000")
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

        # -----------------------------------------------------------------------------------------------------------------------

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

    def Click_Import(self):
            # try:
                import_click = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.click_import))
                time.sleep(.2)
                import_click.click()
                time.sleep(.2)

                print("Clicked on Import button successfully.....!! ")

            # except Exception as e:
            #     print(f"Error: {e}")

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

    def wait_for_spinner_to_disappear(self, timeout=40):
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located((
                        By.XPATH,
                        "//div[contains(@class,'spinner') or contains(@class,'ms-Spinner')]"
                    ))
                )
            except TimeoutException:
                print("Spinner not visible or already disappeared.")

    def Click_Back_Button(self):
            try:
                wait = WebDriverWait(self.driver, 40)

                self.wait_for_spinner_to_disappear()

                back_btn = wait.until(
                    EC.element_to_be_clickable(self.back_button)
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    back_btn
                )

                self.wait_for_spinner_to_disappear()

                self.driver.execute_script("arguments[0].click();", back_btn)

                time.sleep(.2)
                print("Clicked on Back button successfully.....!!")

            except Exception as e:
                print(f"Click_Back_Button error: {type(e).__name__} - {e}")
                self.driver.save_screenshot("back_button_error.png")
                raise


    def Select_Account_Type(self):
        try:
            wait = WebDriverWait(self.driver, 40)

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

            self.driver.execute_script("arguments[0].click();", account_type_input)
            time.sleep(0.3)

            account_type_input.send_keys(Keys.CONTROL, "a")
            account_type_input.send_keys("Savings account")
            time.sleep(1)

            savings_account_option = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//*[contains(@id,'react-select') and contains(@id,'-option') "
                "and contains(translate(normalize-space(.), "
                "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'savings account')]"
            )))

            self.driver.execute_script("arguments[0].click();", savings_account_option)

            print("Savings account selected successfully....!!")

        except Exception as e:
            print(f"Error in Select_Account_Type: {type(e).__name__} - {e}")
            raise


#------------------------------------------------------------------------------------------------------------------------


    def wait_for_spinner_to_disappear(self, timeout=40):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'spinner')]")
                )
            )
        except:
            pass

    def clear_and_enter_date(self, element, value):
        self.driver.execute_script("""
            const input = arguments[0];
            input.removeAttribute('disabled');
            input.removeAttribute('readonly');
            input.focus();
        """, element)

        time.sleep(0.3)

        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(0.2)

        element.send_keys(Keys.CONTROL, "a")
        time.sleep(0.2)

        element.send_keys(Keys.BACKSPACE)
        time.sleep(0.2)

        element.send_keys(value)
        time.sleep(0.3)

        element.send_keys(Keys.ENTER)
        time.sleep(0.3)

        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
        """, element)


    def Change_Date_Calendar(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            self.wait_for_spinner_to_disappear()

            from_date = wait.until(
                EC.presence_of_element_located(self.enter_from_date)
            )

            to_date = wait.until(
                EC.presence_of_element_located(self.enter_to_date)
            )

            self.clear_and_enter_date(from_date, "22/01/2023")
            time.sleep(1)

            self.clear_and_enter_date(to_date, "01/01/2028")
            time.sleep(1)

            try:
                refresh = wait.until(
                    EC.presence_of_element_located(self.refresh_icon)
                )
                self.driver.execute_script("arguments[0].click();", refresh)
            except:
                pass

            self.wait_for_spinner_to_disappear()

            print("Changed date successfully in calendar.")

        except Exception as e:
            print(f"Error in Change_Date_Calendar: {type(e).__name__} - {e}")
            self.driver.save_screenshot("change_date_calendar_error.png")
            raise

    def Click_Data_Filter_Icon(self):
            try:
                click_data_filter_icon = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.click_data_filter_icon))
                time.sleep(.2)
                click_data_filter_icon.click()
                time.sleep(.2)

                print("Clicked on data filter icon successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Shorting_old_to_new(self):
            try:
                data_old_to_new = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.old_to_new))
                time.sleep(.2)
                data_old_to_new.click()
                time.sleep(.2)

                print("Clicked on data shorting old to new successfully showing........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Shorting_new_to_old(self):
            try:
                data_new_to_old = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.new_to_old))
                time.sleep(.2)
                data_new_to_old.click()
                time.sleep(.2)

                print("Clicked on data shorting new to old successfully showing........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Click_Select_All_Date(self):
            try:
                select_all_date = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.click_select_all_date))
                time.sleep(.2)
                select_all_date.click()
                time.sleep(.2)

                print("Click on select_all_date successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Select_First_Option(self):
            # try:
            option = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.first_option))
            time.sleep(.2)
            option.click()
            time.sleep(.2)

            print("Select first option successfully........!! ")

            # except Exception as e:
            #     print(f"Error: {e}")

            time.sleep(2)

    def Second_Option(self):
            try:
                select_option = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.second_option))
                time.sleep(.2)
                select_option.click()
                time.sleep(.2)

                print("Select Second option successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Click_Apply_Button(self):
            try:
                apply_button = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.click_apply_button))
                time.sleep(.2)
                apply_button.click()
                time.sleep(.2)

                print("Click on apply button successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

        # ---------------------------------------Description---------------------------------------------------------------------

    def Click_Description_Filter_Icon(self):
            try:
                click_des_filter_icon = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.description_filter_icon))
                time.sleep(.2)
                click_des_filter_icon.click()
                time.sleep(.2)

                print("Clicked on Description filter icon successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Shorting_a_to_z(self):
            try:
                az = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.a_to_z))
                time.sleep(.2)
                az.click()
                time.sleep(.2)

                print("Clicked on data shorting A to Z successfully showing........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Shorting_z_to_a(self):
            try:
                data_new_to_old = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.z_to_a))
                time.sleep(.2)
                data_new_to_old.click()
                time.sleep(.2)

                print("Clicked on data shorting z to a successfully showing........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

        # -----------------------------------------money- out ----------------------------------------------------------------

    def Click_MoneyOut_Filter_Icon(self):
            try:
                money_out = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.filter_icon_money_out))
                time.sleep(.2)
                money_out.click()
                time.sleep(.2)

                print("Clicked on Money Out filter icon successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

        # def Click_MoneyOut_Filter_Icon(self):
        #     try:
        #         wait = WebDriverWait(self.driver, 40)
        #
        #         self.wait_for_spinner_to_disappear()
        #
        #         money_filter = wait.until(
        #             EC.presence_of_element_located(self.money_out_filter_icon)
        #         )
        #
        #         self.driver.execute_script(
        #             "arguments[0].scrollIntoView({block:'center'});",
        #             money_filter
        #         )
        #
        #         time.sleep(0.5)
        #         self.wait_for_spinner_to_disappear()
        #
        #         self.driver.execute_script("arguments[0].click();", money_filter)
        #
        #         print("Clicked Money Out filter successfully.")
        #
        #     except Exception as e:
        #         print(f"Error in Click_MoneyOut_Filter_Icon: {type(e).__name__} - {e}")
        #         self.driver.save_screenshot("money_out_filter_error.png")
        #         raise

    def Small_Lest_To_Largest(self):
            try:
                sl = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.small_lest_to_largest))
                time.sleep(.2)
                sl.click()
                time.sleep(2)

                print("Clicked on data shorting small to largest successfully showing........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

    def Largest_To_Small_Lest(self):
            try:
                ls = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.largest_to_smallest))
                time.sleep(.2)
                ls.click()
                time.sleep(.2)

                print("Clicked on data shorting largest to small  successfully showing........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

        # -----------------------------------------money in ---------------------------------------------------------------------

    def Click_MoneyIn_Filter_Icon(self):
            try:
                money_in = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.filter_icon_money_in))
                time.sleep(.2)
                money_in.click()
                time.sleep(.2)

                print("Clicked money in  filter icon successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

        # -------------------------------------------------google icon-----------------------------------------------------------

    def click_magnifier_icon(self):
            wait = WebDriverWait(self.driver, 20)

            # Hover first row (Uber Trip row in your screenshot)
            first_row = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//div[contains(@class,'tr')])[1]")
                )
            )

            ActionChains(self.driver).move_to_element(first_row).perform()

            # Magnifier icon
            icon = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//i[@data-icon-name='googleMagnifier'])[1]")
                )
            )

            # Scroll and click via JS
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                icon
            )

            self.driver.execute_script(
                "arguments[0].click();",
                icon
            )

            print("Magnifier icon clicked successfully")


    def Click_cross_icon(self):
            try:
                cross = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable(self.clear_data))
                time.sleep(.2)
                cross.click()
                time.sleep(.2)

                print("Clicked cross icon successfully........!! ")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)

#---------------------------------------search----------------------------------------------------------------------------

    def Enter_Search(self):
        try:
            search = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.enter_search))
            time.sleep(.2)
            search.click()
            time.sleep(.2)
            search.send_keys("LATE PAYMENT FEE")
            time.sleep(.2)
            search.send_keys(Keys.ENTER)
            time.sleep(.2)

            print("Enter Search value  successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    def Remove_Search(self):
        try:
            remove = WebDriverWait(self.driver,40).until(
                EC.element_to_be_clickable(self.cancel_cross_button)
            )
            time.sleep(.2)
            remove.click()
            time.sleep(.2)
            print("Search functionality reset  successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")

