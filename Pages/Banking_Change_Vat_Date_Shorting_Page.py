import random

from faker import Faker
import time



from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains


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


class Vat_Change:

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




#-----------------Change date-------------------------------------------------------------------------------------------

        self.enter_from_date = (By.XPATH, "//input[@name='fromDate']")
        self.enter_to_date = (By.XPATH, "//input[@name='toDate']")
        self.refresh_icon = (By.XPATH, "//i[@data-icon-name='Refresh']/ancestor::button")
#--------------------------Data filter----------------------------------------------------------------------------------

        self.click_data_filter_icon = (By.XPATH, "//i[@id='date-date-filter' and @data-icon-name='ChevronDown']")
        self.old_to_new = (By.XPATH, "//div[contains(@class,'ms-Callout')]//div[normalize-space()='Oldest to newest']")
        self.new_to_old = (By.XPATH, "//div[contains(@class,'ms-Callout')]//div[normalize-space()='Newest to oldest']")
        self.click_select_all_date = (By.XPATH, "//div[contains(@class,'ms-Callout')]//div[@data-is-focusable='true'][.//text()[normalize-space()='Select all']]//i[@data-icon-name='CheckMark']")
        self.first_option = (By.XPATH, "(//div[@data-is-focusable='true'][normalize-space()='Select all']/following-sibling::div[@data-is-focusable='true'])[1]")
        self.second_option = (By.XPATH, "//div[@data-is-focusable='true' and normalize-space()='06/04/2024']")
        # self.click_apply_button = (By.XPATH, "//button[contains(@class,'ms-Button--primary') and normalize-space()='Apply']")

        self.click_apply_button = (
            By.XPATH,
            "//button[not(@disabled) and @aria-disabled!='true' "
            "and (.//span[normalize-space()='Apply'] "
            "or normalize-space(.)='Apply')]"
        )



        self.description_filter_icon = (By.XPATH, "//i[@id='desc-string-filter' and @data-icon-name='ChevronDown']")
        self.a_to_z = (By.XPATH, "//div[@data-is-focusable='true']//div[normalize-space()='A to Z']")
        self.z_to_a = (By.XPATH, "//div[@data-is-focusable='true']//div[normalize-space()='Z to A']")
        self.click_select_all_description = (By.XPATH, "//div[@data-is-focusable='true'][.//text()[normalize-space()='Select all']]")
        self.first_description = (By.XPATH, "//div[@data-is-focusable='true'][.//div[normalize-space()='EDF ENERGY-ECOM ON 31 MAR BDC']]")
        self.enter_data_search = (By.XPATH, "//div[contains(@class,'ms-TextField-fieldGroup')]//input[@title='Search term']")
        self.click_apply_for_des = (By.XPATH, "//span[normalize-space()='Apply']/ancestor::button")

        self.filter_icon_money_out = (By.XPATH, "//i[@data-icon-name='ChevronDown' and @id='mo-number-filter']")
        self.small_lest_to_largest = (By.XPATH, "//div[@data-is-focusable='true'][normalize-space()='Smallest to largest']")
        self.largest_to_smallest = (By.XPATH, "//div[@data-is-focusable='true'][normalize-space()='Largest to smallest']")
        self.click_apply_for_money_out = (By.XPATH, "//button[.//span[normalize-space()='Apply']]")


        self.filter_icon_money_in = (By.XPATH, "//i[@data-icon-name='ChevronDown' and @id='mi-number-filter']")
        self.small_lest_to_largest_mi = (By.XPATH, "//div[@data-is-focusable='true'][contains(normalize-space(.),'Smallest to largest')]")
        self.largest_to_smallest_mi = (By.XPATH, "//div[@data-is-focusable='true'][contains(normalize-space(.),'Largest to smallest')]")
        self.click_apply_mi = (By.XPATH, "//button[@id='ApplyBtn']//span[normalize-space()='Apply']")

        self.google_icon = (By.XPATH, "(//section[contains(@class,'magnifier')]//i[@data-icon-name='googleMagnifier'])[1]")

        self.clear_data = (By.XPATH, "//i[@data-icon-name='Cancel' and @title='Clear sorts & filters']")















        self.change_vat = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[1]")
        self.change_vat_second = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[1]/div[1]")










#----------------------------------------------setting------------------------------------------------------------------

        self.setting_section = (By.XPATH, "//a[@aria-label='Settings' and contains(@href,'/settings')]")
        self.chart_of_account = (By.XPATH, "//span[normalize-space()='Chart of accounts']/ancestor::button")
        self.click_add_account = (By.XPATH, "//span[normalize-space()='Account']/ancestor::button")
        self.select_account_type_setting  = (By.XPATH, "//label[normalize-space()='Account type']/following::input[contains(@id,'react-select')][1]")
        self.enter_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")
        self.enter_vat = (By.XPATH, "//label[normalize-space()='Default VAT rate']/following::div[contains(@class,'rs-control')][1]")
        self.click_credit_card = (By.XPATH, "//span[contains(text(),'is credit card')]")


        self.click_active_account = (By.XPATH, "//span[contains(text(),'Activate')]")
        self.click_yes = (By.XPATH, "//span[contains(text(),'Yes')]")
        self.select_unexplained_Tab = (By.XPATH,
                                       "//button[@role='tab']//span[contains(normalize-space(),'Unexplained')]")
        self.search_input = (
            By.XPATH,
            "//input[@role='searchbox' and @placeholder='Search']"
        )



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




    def Sort_Code(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            code = wait.until(EC.visibility_of_element_located(self.enter_sort_code))

            self.sort_code_value = "112233"
            time.sleep(.2)

            code.clear()
            time.sleep(.2)
            code.send_keys(self.sort_code_value)
            time.sleep(.2)

            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(.2)

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


#-----------------------------------------------------------------------------------------------------------------------


    def Click_Data_Filter_Icon(self):
        try:
            click_data_filter_icon = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.click_data_filter_icon))
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

    # def Select_First_Option(self):
    #     driver = self.driver
    #
    #     wait = WebDriverWait(
    #         driver,
    #         40,
    #         poll_frequency=0.3,
    #         ignored_exceptions=(StaleElementReferenceException,)
    #     )
    #
    #     def get_first_visible_option(d):
    #         # Fluent UI dropdowns/callouts which are currently visible
    #         containers = d.find_elements(
    #             By.XPATH,
    #             """
    #             //div[
    #                 @role='listbox'
    #                 or contains(@class,'ms-Callout')
    #                 or contains(@class,'ms-Dropdown-callout')
    #                 or contains(@class,'ms-ContextualMenu')
    #             ]
    #             """
    #         )
    #
    #         for container in containers:
    #             try:
    #                 if not container.is_displayed():
    #                     continue
    #
    #                 # Find all possible selectable options inside visible popup
    #                 options = container.find_elements(
    #                     By.XPATH,
    #                     """
    #                     .//*[
    #                         @role='option'
    #                         or @role='menuitemcheckbox'
    #                         or @data-is-focusable='true'
    #                     ]
    #                     """
    #                 )
    #
    #                 for option in options:
    #                     try:
    #                         if not option.is_displayed():
    #                             continue
    #
    #                         if not option.is_enabled():
    #                             continue
    #
    #                         text = option.text.strip()
    #
    #                         # Ignore empty rows and Select all
    #                         if not text:
    #                             continue
    #
    #                         if text.lower() == "select all":
    #                             continue
    #
    #                         # Ignore disabled options
    #                         aria_disabled = option.get_attribute("aria-disabled")
    #                         disabled = option.get_attribute("disabled")
    #
    #                         if aria_disabled == "true" or disabled is not None:
    #                             continue
    #
    #                         return option
    #
    #                     except StaleElementReferenceException:
    #                         continue
    #
    #             except StaleElementReferenceException:
    #                 continue
    #
    #         return False
    #
    #     try:
    #         option = wait.until(
    #             get_first_visible_option,
    #             message="No visible selectable option was found."
    #         )
    #
    #         option_text = option.text.strip()
    #
    #         driver.execute_script(
    #             """
    #             arguments[0].scrollIntoView({
    #                 block: 'center',
    #                 inline: 'nearest'
    #             });
    #             """,
    #             option
    #         )
    #
    #         time.sleep(0.3)
    #
    #         # Re-find because Fluent UI may rerender after scrolling
    #         option = wait.until(get_first_visible_option)
    #
    #         try:
    #             option.click()
    #
    #         except (
    #                 ElementClickInterceptedException,
    #                 StaleElementReferenceException
    #         ):
    #             option = wait.until(get_first_visible_option)
    #
    #             driver.execute_script(
    #                 """
    #                 arguments[0].dispatchEvent(
    #                     new MouseEvent('mousedown', {
    #                         bubbles: true,
    #                         cancelable: true,
    #                         view: window
    #                     })
    #                 );
    #
    #                 arguments[0].dispatchEvent(
    #                     new MouseEvent('mouseup', {
    #                         bubbles: true,
    #                         cancelable: true,
    #                         view: window
    #                     })
    #                 );
    #
    #                 arguments[0].click();
    #                 """,
    #                 option
    #             )
    #
    #         print(
    #             f"First option selected successfully: {option_text}"
    #         )
    #
    #     except TimeoutException:
    #         driver.save_screenshot(
    #             "select_first_option_timeout.png"
    #         )
    #
    #         print("No visible option found in the opened filter.")
    #         print("Current URL:", driver.current_url)
    #
    #         # Debug visible popup elements
    #         visible_focusable = driver.find_elements(
    #             By.XPATH,
    #             "//*[@data-is-focusable='true']"
    #         )
    #
    #         print(
    #             "Total focusable elements found:",
    #             len(visible_focusable)
    #         )
    #
    #         for index, element in enumerate(visible_focusable):
    #             try:
    #                 if element.is_displayed():
    #                     print(
    #                         f"Visible element {index}: "
    #                         f"text='{element.text.strip()}', "
    #                         f"role='{element.get_attribute('role')}', "
    #                         f"tag='{element.tag_name}'"
    #                     )
    #             except StaleElementReferenceException:
    #                 pass
    #
    #         raise



    def Select_First_Option(self):
        driver = self.driver
        wait = WebDriverWait(driver, 40)

        def find_visible_option(d):
            select_all_list = d.find_elements(
                By.XPATH,
                "//div[@data-is-focusable='true' and normalize-space()='Select all']"
            )

            for select_all in select_all_list:
                try:
                    if not select_all.is_displayed():
                        continue

                    options = select_all.find_elements(
                        By.XPATH,
                        "following-sibling::div[@data-is-focusable='true']"
                    )

                    for option in options:
                        if option.is_displayed() and option.is_enabled():
                            return option

                except StaleElementReferenceException:
                    continue

            return False

        try:
            option = wait.until(find_visible_option)

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'nearest'});",
                option
            )

            time.sleep(0.3)

            try:
                option.click()
            except (
                    ElementClickInterceptedException,
                    StaleElementReferenceException
            ):
                option = wait.until(find_visible_option)
                driver.execute_script("arguments[0].click();", option)

            print(f"First option selected successfully: {option.text.strip()}")

        except TimeoutException:
            driver.save_screenshot("select_first_option_timeout.png")
            print("No visible option found in the currently opened filter.")
            raise


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


    # def Click_Apply_Button(self):
    #     try:
    #         apply_button = WebDriverWait(self.driver, 40).until(
    #             EC.element_to_be_clickable(self.click_apply_button))
    #         time.sleep(.2)
    #         apply_button.click()
    #         time.sleep(.2)
    #
    #         print("Click on apply button successfully........!! ")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #
    #         time.sleep(2)

    def Click_Apply_Button(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            40,
            poll_frequency=0.3,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        def find_visible_apply_button(d):
            # Search all possible Apply buttons
            buttons = d.find_elements(
                By.XPATH,
                """
                //button[
                    normalize-space(.)='Apply'
                    or .//span[normalize-space()='Apply']
                ]
                |
                //*[
                    @role='button'
                    and normalize-space(.)='Apply'
                ]
                """
            )

            for button in buttons:
                try:
                    if not button.is_displayed():
                        continue

                    if not button.is_enabled():
                        continue

                    if button.get_attribute("aria-disabled") == "true":
                        continue

                    if button.get_attribute("disabled") is not None:
                        continue

                    return button

                except StaleElementReferenceException:
                    continue

            return False

        last_error = None

        for attempt in range(1, 4):
            try:
                print(f"Apply button click attempt: {attempt}")

                # Wait for loader before searching
                self.wait_for_loader_to_disappear()

                apply_button = wait.until(
                    find_visible_apply_button,
                    message="No visible and enabled Apply button found."
                )

                driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        block: 'center',
                        inline: 'nearest'
                    });
                    """,
                    apply_button
                )

                time.sleep(0.3)

                self.wait_for_loader_to_disappear()

                # Re-locate because Fluent UI/React may rerender
                apply_button = wait.until(find_visible_apply_button)

                try:
                    apply_button.click()

                except (
                        ElementClickInterceptedException,
                        StaleElementReferenceException
                ):
                    apply_button = wait.until(find_visible_apply_button)

                    driver.execute_script(
                        """
                        const element = arguments[0];

                        element.dispatchEvent(
                            new MouseEvent('mousedown', {
                                bubbles: true,
                                cancelable: true,
                                view: window
                            })
                        );

                        element.dispatchEvent(
                            new MouseEvent('mouseup', {
                                bubbles: true,
                                cancelable: true,
                                view: window
                            })
                        );

                        element.click();
                        """,
                        apply_button
                    )

                print("Clicked Apply button successfully.")

                # Optional: confirm popup closes after Apply
                wait.until(
                    lambda d: not any(
                        element.is_displayed()
                        for element in d.find_elements(
                            By.XPATH,
                            """
                            //button[
                                normalize-space(.)='Apply'
                                or .//span[normalize-space()='Apply']
                            ]
                            """
                        )
                    )
                )

                print("Filter popup closed successfully.")
                return

            except (
                    TimeoutException,
                    StaleElementReferenceException,
                    ElementClickInterceptedException
            ) as error:
                last_error = error

                print(
                    f"Attempt {attempt} failed: "
                    f"{type(error).__name__}: {error}"
                )

                driver.save_screenshot(
                    f"apply_button_attempt_{attempt}.png"
                )

                time.sleep(1)

        # Final debugging
        print("Current URL:", driver.current_url)

        all_buttons = driver.find_elements(By.TAG_NAME, "button")

        print("Visible buttons on page:")

        for index, button in enumerate(all_buttons):
            try:
                if button.is_displayed():
                    print(
                        f"{index}: "
                        f"text='{button.text.strip()}', "
                        f"id='{button.get_attribute('id')}', "
                        f"disabled='{button.get_attribute('disabled')}', "
                        f"aria-disabled='{button.get_attribute('aria-disabled')}'"
                    )
            except StaleElementReferenceException:
                continue

        driver.save_screenshot("apply_button_final_error.png")

        raise TimeoutException(
            "Unable to click visible Apply button after 3 attempts. "
            f"Last error: {last_error}"
        )

#---------------------------------------Description---------------------------------------------------------------------

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


    #-----------------------------------------money- out ----------------------------------------------------------------


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




#-----------------------------------------money in ---------------------------------------------------------------------

    def Click_MoneyIn_Filter_Icon(self):
        try:
            money_in = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.filter_icon_money_in))
            time.sleep(.2)
            money_in .click()
            time.sleep(.2)

            print("Clicked money in  filter icon successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

#-------------------------------------------------google icon-----------------------------------------------------------

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
















