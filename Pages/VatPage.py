import pyautogui
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


class Vat:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver
        self.expected_vat_page_url = None


# ------------------------ WebElements of admin for Client sell.--------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='TKG COUSINS LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.vat_return_section  = (By.XPATH, "//div[contains(text(),'VAT returns')]")

        self.click_enable_MTD =(By.XPATH, "//span[normalize-space()='Enable MTD']/ancestor::button[1]")
        self.click_reauthorized = (By.XPATH, "//span[normalize-space()='Re-authorise']/ancestor::button[1]")

        self.click_continue = (By.XPATH, "  (//a[normalize-space()='Continue'])[1]")
        self.click_HMRC_online = (By.XPATH, "(//a[normalize-space()='Sign in to the HMRC online service'])[1]")
        self.click_user_credentials = (By.XPATH, "//a[@href='https://developer.service.hmrc.gov.uk/api-test-user']")
        self.click_organization = (By.XPATH, "//label[@for='Organisation']")
        self.click_create = (By.XPATH, "(//button[normalize-space()='Create'])[1]")
        self.user_id_value = (By.XPATH, "//p[@id='userid-label']/following-sibling::p[1]")
        self.password_id_value = (By.XPATH, "//p[@id='password-label']/following-sibling::p[1]")
        self.vat_registration_date = (By.XPATH, "//p[@id='vatregistrationdate-label']/following-sibling::p[1]")
        self.vat_registration_no = (By.XPATH, "//p[@id='vrn-label']/following-sibling::p[1]")

        self.parent_window = self.driver.current_window_handle
        self.user_id = (By.XPATH, "(//input[@id='userId'])[1]")
        self.pass_id = (By.XPATH, "(//input[@id='password'])[1]")
        self.click_submit  = (By.XPATH, "//button[@id='submit']")

        self.give_permission = (By.XPATH, "//button[@id='givePermission']")
        self.success_message = (By.XPATH, "//*[contains(text(),'Setting updated successfully')]")

        self.click_edit = (By.XPATH, "//button[@aria-label='Edit']")
        self.vat_registration_date_input = (By.XPATH, "//label[normalize-space()='Registration date']/following::input[1]")

        self.enter_vat = (By.XPATH, "//label[normalize-space()='VAT number']/following::input[@type='number' and @placeholder='123456789'][1]")
        self.save = (By.XPATH, "//button[.//span[normalize-space()='Save']]")
        self.vat_return = (By.XPATH, "//button[@type='button' and .//span[normalize-space()='VAT return']]")




# -----------------------------------------------------------------------------------------------------------------------
        self.add_vate = (By.XPATH, "//button[.//span[normalize-space()='VAT return']]")

        self.account = (By.XPATH, "//span[normalize-space()='VAT return']")
        self.obligations = (By.XPATH, "//label[normalize-space()='Obligations']/following::div[contains(@id,'react-select')][1]")
        self.save_vat = (By.XPATH,  "//button[.//span[normalize-space()='Save']]")

#-----------------------------------------------------------------------------------------------------------------------
        self.edit_vat_return = (By.XPATH, "(//button[@id='btn-btnEdit'])[1]")
        self.click_import = (By.XPATH, "//span[normalize-space()='Import']/ancestor::button[1]")

        self.upload_input = (By.XPATH, "//input[@type='file' and contains(@accept,'.xlsx')]")


        self.click_send = (By.XPATH, "//span[normalize-space()='Send']/ancestor::button[1]")
        self.enter_reviewer = (By.XPATH, "//label[normalize-space()='Reviewer']/following::input[@role='combobox'][1]")
        self.add_attachment = (By.XPATH, "//label[@for='files-input']//span[normalize-space()='Working files']")

        self.save_request = (By.XPATH, "//div[contains(@class,'modal-footer')]//button[.//span[normalize-space()='Save']]")

        self.click_review = (By.XPATH, "//div[contains(@class,'actions')]//button[.//span[normalize-space()='Review']]")
        self.click_next = (By.XPATH, "//div[contains(@class,'modal')]//button[.//span[normalize-space()='Next']]")
        self.click_approve = (By.XPATH, "//div[contains(@class,'modal-footer')]//button[.//span[normalize-space()='Approve']]")
        self.click_yes = (By.XPATH, "//div[contains(@class,'Dialog')]//button[.//span[normalize-space()='Yes']]")
        self.e_sign = (By.XPATH, "//div[contains(@class,'actions')]//button[.//span[normalize-space()='E-Sign']]")
        self.send_mail = (By.XPATH, "//div[contains(@class,'actions')]//button[.//span[normalize-space()='Send mail']]")
        self.send = (By.XPATH, "//span[normalize-space()='Send']/ancestor::button[1]")

        self.recipient = (By.XPATH, "//label[normalize-space()='To']/following::input[@role='combobox'][1]")
        self.from_mail = (By.XPATH, "//label[normalize-space()='From']/following::div[contains(@class,'singleValue')][1]")

        self.from_mail = (By.XPATH, "//label[normalize-space()='From']/following::div[contains(@class,'control')][1]")
        self.from_mail_input = (By.XPATH, "//label[normalize-space()='From']/following::input[@role='combobox'][1]")

        self.click_mail_icon = (By.XPATH, "//div[normalize-space()='Email']/preceding::button[1]")

        self.review_mail = (By.XPATH,"//div[contains(@class,'current-message')]//a[normalize-space()='Review']")

        self.click_get_otp = (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Get OTP']]")
        self.otp_boxes = (By.XPATH, "//input[contains(@aria-label,'OTP character')]")
        self.proceed_securely = (By.XPATH, "//button[@type='button' and .//span[normalize-space()='Proceed Securely']]")
        self.click_accept = (By.XPATH, "//button[contains(@class,'btn-success') and normalize-space()='Accept']")
        self.enter_name_signature = (By.XPATH, "//div[contains(@class,'modal-content')]//input[@name='name' and contains(@class,'form-control')]")
        self.click_sing_button = (By.XPATH, "//button[contains(@class,'btn-primary') and normalize-space()='Sign']")
        self.click_okay = (By.XPATH, "//div[contains(@class,'modal-footer')]//button[normalize-space()='Okay']")
        self.close_cross = (By.XPATH, "//button[contains(@class,'ms-Panel-closeButton')]")
        self.click_three_dot = (By.XPATH, "//div[normalize-space()='Accepted by Client']/ancestor::div[@role='row']//button[.//i[@data-icon-name='More']]")
        self.submit_hmrc = (By.XPATH, "//ul[contains(@class,'ms-ContextualMenu-list')]//button[.//span[normalize-space()='Submit to HMRC']]")
        self.click_vat_return_submit = (By.XPATH, "//button[@id='submit-btn' and .//span[normalize-space()='Submit']]")


        self.click_download = (By.XPATH, "//div[contains(@class,'modal-header')]//button[@title='Download response']")









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


    def Enter_Company(self, company_name="TKG COUSINS LIMITED", timeout=12, os=None):

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

#--------------------------------------------------------------------------------------------------------------------------

    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)

            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Vat_Return_Section(self):
        try:
            vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.vat_return_section))
            time.sleep(.2)
            vat.click()
            time.sleep(.2)

            print("Click on  vat return section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)



    def Click_Enable_MTD(self):
        try:
            MTD = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_enable_MTD))
            time.sleep(.2)
            MTD.click()
            time.sleep(.2)

            print("Click on Enable MTD section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)




    def Click_Reauthorized(self):
        try:
            reauthorized = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_reauthorized))
            time.sleep(.2)
            reauthorized.click()
            time.sleep(.2)

            print("Click on Reauthorized section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Handle_MTD_Or_Reauthorized(self):
        try:
            time.sleep(1)

            enable_mtd = self.driver.find_elements(*self.click_enable_MTD)

            if enable_mtd and enable_mtd[0].is_displayed():
                print("Enable MTD is available, so clicking Enable MTD...")
                self.Click_Enable_MTD()

            else:
                reauthorized = self.driver.find_elements(*self.click_reauthorized)

                if reauthorized and reauthorized[0].is_displayed():
                    print("Enable MTD is not available, so clicking Reauthorized...")
                    self.Click_Reauthorized()
                else:
                    print("Neither Enable MTD nor Reauthorized button is available.")

            time.sleep(0.2)

        except Exception as e:
            print(f"Error while handling MTD/Reauthorized condition: {e}")
            time.sleep(0.2)



    def Click_Continue(self):
        try:
            cont = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_continue))
            time.sleep(.2)
            cont.click()
            time.sleep(.2)

            print("Click on Continue button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_HMRC_Online(self):
        try:
            hmrc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_HMRC_online))
            time.sleep(.2)
            hmrc.click()
            time.sleep(.2)

            print("Click on Sign in to the HMRC online service button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)



    def Click_Test_User_Credentials(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            old_windows = self.driver.window_handles.copy()

            user = wait.until(
                EC.element_to_be_clickable(self.click_user_credentials)
            )
            time.sleep(0.5)
            user.click()

            # wait for new tab
            wait.until(lambda d: len(d.window_handles) > len(old_windows))

            # switch to newly opened tab
            new_window = [w for w in self.driver.window_handles if w not in old_windows][0]
            self.driver.switch_to.window(new_window)

            # confirm correct page loaded
            wait.until(lambda d: "api-test-user" in d.current_url)
            time.sleep(1)

            print("Clicked on user credentials and switched to new tab successfully....!!")
            print("Current URL:", self.driver.current_url)

        except Exception as e:
            print(f"Error in Click_Test_User_Credentials: {e}")
            raise

    def Scroll_Down_Page(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(lambda d: "api-test-user" in d.current_url)

            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)

            print("Page scrolled down successfully on new tab....!!")

        except Exception as e:
            print(f"Error while scrolling: {e}")
            raise


    def Click_Radio_Organization(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            wait.until(lambda d: "api-test-user" in d.current_url)

            label = wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[@for='Organisation']"))
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'nearest'});",
                label
            )
            time.sleep(0.5)

            try:
                label.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", label)

            # verify selected
            radio = wait.until(
                EC.presence_of_element_located((By.ID, "Organisation"))
            )

            if not radio.is_selected():
                raise Exception("Organisation radio button was not selected.")

            print("Click on Radio button of organization successfully....!!")

        except Exception as e:
            print(f"Error on Click Radio Organization: {e}")
            raise


    def Click_Create(self):
        try:
            create = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_create))
            time.sleep(.2)
            create.click()
            time.sleep(.2)

            print("Click on create button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Get_User_ID(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            user_id_element = wait.until(
                EC.presence_of_element_located(self.user_id_value)
            )

            user_id = user_id_element.text.strip()

            print(f"User ID is: {user_id}")
            return user_id

        except Exception as e:
            print(f"Error while getting User ID: {e}")
            raise

    def Get_User_Pass(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            Password_id_element = wait.until(
                EC.presence_of_element_located(self.password_id_value)
            )

            Password = Password_id_element.text.strip()

            print(f"Password is: {Password}")
            return Password

        except Exception as e:
            print(f"Error while getting User Pass: {e}")
            raise

    # def Get_Vat_Registration_Date(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 20)
    #
    #         Vat_Date = wait.until(
    #             EC.presence_of_element_located(self.vat_registration_date)
    #         )
    #
    #         Vat_Registration_Date = Vat_Date.text.strip()
    #
    #         print(f"Registration Date: {Vat_Registration_Date}")
    #         return Vat_Registration_Date
    #
    #     except Exception as e:
    #         print(f"Error while getting Vat Date: {e}")
    #         raise

    def Get_Vat_Registration_Date(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            Vat_Date = wait.until(
                EC.presence_of_element_located(self.vat_registration_date)
            )

            raw_date = Vat_Date.text.strip()
            print(f"Raw Date: {raw_date}")

            # Try multiple formats
            for fmt in ("%d %B %Y", "%Y-%m-%d", "%d/%m/%Y"):
                try:
                    parsed_date = datetime.strptime(raw_date, fmt)
                    formatted_date = parsed_date.strftime("%d:%m:%Y")
                    print(f"Formatted Date: {formatted_date}")
                    return formatted_date
                except:
                    continue

            raise Exception(f"Unknown date format: {raw_date}")

        except Exception as e:
            print(f"Error while getting Vat Date: {e}")
            raise

    def Get_Vat_Registration(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            Vat_Reg = wait.until(
                EC.presence_of_element_located(self.vat_registration_no)
            )

            Vat_Registration_No = Vat_Reg.text.strip()

            print(f"Vat Registration Number: {Vat_Registration_No}")
            return Vat_Registration_No

        except Exception as e:
            print(f"Error while getting Vat No: {e}")
            raise

    def Switch_Back_And_Enter_User_ID(self, user_id):
        try:
            wait = WebDriverWait(self.driver, 20)

            # switch back to original tab
            self.driver.switch_to.window(self.parent_window)
            print("Switched back to parent/original tab successfully....!!")

            # wait for user id input on old page
            user_id_input = wait.until(
                EC.presence_of_element_located(self.user_id)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                user_id_input
            )
            time.sleep(0.5)

            user_id_input.clear()
            user_id_input.send_keys(user_id)

            print(f"User ID entered successfully: {user_id}")

        except Exception as e:
            print(f"Error while switching back and entering User ID: {e}")
            raise


    def Enter_Password(self, pass_id):
        try:
            wait = WebDriverWait(self.driver, 20)

            # switch back to original tab
            # self.driver.switch_to.window(self.parent_window)
            # print("Switched back to parent/original tab successfully....!!")

            # wait for user id input on old page
            user_id_input = wait.until(
                EC.presence_of_element_located(self.pass_id)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                user_id_input
            )
            time.sleep(0.5)

            user_id_input.clear()
            user_id_input.send_keys(pass_id)

            print(f"Password entered successfully: {pass_id}")

        except Exception as e:
            print(f"Error while switching back and entering Password ID: {e}")
            raise


    def Click_SignIn_Button(self):
        try:
            signIn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_submit))
            time.sleep(.2)
            signIn.click()
            time.sleep(.2)

            print("Click on signIn button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Give_Permission(self):
        try:
            permission = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.give_permission))
            time.sleep(.2)
            permission.click()
            time.sleep(.2)

            print("Click on Permission button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Store_Current_Vat_Page_URL(self):
        try:
            self.expected_vat_page_url = self.driver.current_url
            print(f"Stored VAT page URL: {self.expected_vat_page_url}")
        except Exception as e:
            print(f"Error while storing VAT page URL: {e}")
            raise

    def Verify_And_Return_To_Expected_Vat_Page(self):
        try:
            if not self.expected_vat_page_url:
                raise Exception(
                    "Expected VAT page URL is not stored. Call Store_Current_Vat_Page_URL() before redirect flow.")

            wait = WebDriverWait(self.driver, 20)
            wait.until(lambda d: d.current_url != "")

            current_url = self.driver.current_url
            print(f"Current URL after redirect: {current_url}")
            print(f"Expected URL: {self.expected_vat_page_url}")

            if current_url != self.expected_vat_page_url:
                print("Redirected to unexpected URL. Navigating back to expected VAT page...")
                self.driver.get(self.expected_vat_page_url)
                wait.until(lambda d: d.current_url == self.expected_vat_page_url)

            print("Returned to expected VAT page successfully....!!")

        except Exception as e:
            print(f"Error while verifying/navigating to expected VAT page: {e}")
            raise

    # def Verify_And_Return_To_Expected_Vat_Page(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 20)
    #         wait.until(lambda d: d.current_url != "")
    #
    #         current_url = self.driver.current_url
    #         print(f"Current URL after redirect: {current_url}")
    #         print(f"Expected URL: {self.expected_vat_page_url}")
    #
    #         if current_url != self.expected_vat_page_url:
    #             print("Redirected to unexpected URL. Navigating back to expected VAT page...")
    #             self.driver.get(self.expected_vat_page_url)
    #             wait.until(lambda d: d.current_url == self.expected_vat_page_url)
    #
    #         print("Returned to expected VAT page successfully....!!")
    #
    #     except Exception as e:
    #         print(f"Error while verifying/navigating to expected VAT page: {e}")
    #         raise




    def Click_Edit(self):
        try:
            edit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_edit))
            time.sleep(.2)
            edit.click()
            time.sleep(.2)

            print("Click on edit button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Enter_Vat_Registration_Date(self, formatted_date):
        try:
            wait = WebDriverWait(self.driver, 20)

            # convert 13:04:2017 -> 13/04/2017
            input_date = formatted_date.replace(":", "/")

            date_input = wait.until(
                EC.presence_of_element_located(self.vat_registration_date_input)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                date_input
            )
            time.sleep(0.5)

            # click field
            date_input.click()
            time.sleep(0.2)

            # clear existing value properly
            date_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            date_input.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)

            # fallback clear using JS also
            self.driver.execute_script("arguments[0].value = '';", date_input)
            time.sleep(0.2)

            # enter new value
            date_input.send_keys(input_date)
            time.sleep(0.5)

            print(f"VAT Registration Date entered successfully: {input_date}")

        except Exception as e:
            print(f"Error while entering VAT Registration Date: {e}")
            raise

    def Enter_Vat_No(self, formatted_date):
        try:
            wait = WebDriverWait(self.driver, 20)

            # convert 13:04:2017 -> 13/04/2017
            input_date = formatted_date.replace(":", "/")

            date_input = wait.until(
                EC.presence_of_element_located(self.vat_registration_date_input)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                date_input
            )
            time.sleep(0.5)

            # click field
            date_input.click()
            time.sleep(0.2)

            # clear existing value properly
            date_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            date_input.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)

            # fallback clear using JS also
            self.driver.execute_script("arguments[0].value = '';", date_input)
            time.sleep(0.2)

            # enter new value
            date_input.send_keys(input_date)
            time.sleep(0.5)

            print(f"VAT Registration Date entered successfully: {input_date}")

        except Exception as e:
            print(f"Error while entering VAT Registration Date: {e}")
            raise



    def Enter_Vat_Registration_Number(self, vat_number):
        try:
            wait = WebDriverWait(self.driver, 20)

            vat_input = wait.until(
                EC.presence_of_element_located(self.enter_vat)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                vat_input
            )
            time.sleep(0.5)

            # click field first
            vat_input.click()
            time.sleep(0.2)

            # clear old value
            vat_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            vat_input.send_keys(Keys.DELETE)
            time.sleep(0.2)

            # extra fallback clear
            self.driver.execute_script("arguments[0].value = '';", vat_input)
            time.sleep(0.2)

            # enter new VAT registration number
            vat_input.send_keys(str(vat_number))
            time.sleep(0.5)

            entered_value = vat_input.get_attribute("value")
            print(f"VAT Registration Number entered successfully: {entered_value}")

        except Exception as e:
            print(f"Error while entering VAT Registration Number: {e}")
            raise

    # def Clcik_Save(self):
    #     try:
    #         save = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save))
    #         time.sleep(.2)
    #         save.click()
    #         time.sleep(.2)
    #
    #         print("Click on save button successfully....!!")
    #     except Exception as e:
    #         print(f"Error on Click:{e}")
    #         time.sleep(.2)

    def Click_Save(self):
        try:
            save = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.save)
            )
            time.sleep(0.2)
            save.click()
            time.sleep(0.2)

            print("Click on save button successfully....!!")

            success_msg = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.success_message)
            )

            actual_message = success_msg.text.strip()
            expected_message = "Setting updated successfully"

            assert actual_message == expected_message, \
                f"Expected message: '{expected_message}', but got: '{actual_message}'"

            print(f"Assertion passed: '{actual_message}' message displayed successfully....!!")

        except Exception as e:
            print(f"Error on Click/Assertion: {e}")
            raise



    def Click_VAT_return(self):
        try:
            vat_return = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.vat_return))
            time.sleep(.2)
            vat_return.click()
            time.sleep(.2)

            print("Click on Vat return button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)





    def Click_Add_Vat(self):
        try:
            vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.add_vate))
            time.sleep(.2)
            vat.click()
            time.sleep(.2)

            print("Click on  vat return section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Select_Obligations(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            # Wait until element is clickable
            obligation = wait.until(
                EC.element_to_be_clickable(self.obligations)
            )
            time.sleep(0.2)

            # Scroll to center
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", obligation)
            time.sleep(0.2)

            # Try normal click
            try:
                obligation.click()
            except:
                # JS click fallback
                driver.execute_script("arguments[0].click();", obligation)

            time.sleep(0.3)

            # Press ENTER
            active = driver.switch_to.active_element
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Select Obligation successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)



    def Save_Vat(self):

        try:
            save_vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.save_vat))
            time.sleep(.2)
            save_vat.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Dividends created successfully')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Dividends created successfully"
            #
            print("Test Case 20 - Pass: Vat saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    def Edit_Vat_Return(self):
        try:
            edit_vat = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.edit_vat_return))
            time.sleep(.2)
            edit_vat.click()
            time.sleep(.2)

            print("Click on edit vat return section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Import(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            import_file = wait.until(
                EC.element_to_be_clickable(self.click_import)
            )
            import_file.click()
            time.sleep(2)

            pyautogui.write(r"C:\Users\CT_USER\Desktop\test\Sample.CSV.xlsx")
            time.sleep(1)
            pyautogui.press("enter")

            print("Import VAT return file uploaded successfully....!!")

        except Exception as e:
            print(f"Error on Import Click/File Upload: {e}")
            raise

    # def Click_Import(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 20)
    #
    #         import_file = wait.until(
    #             EC.element_to_be_clickable(self.click_import)
    #         )
    #         time.sleep(0.2)
    #         import_file.click()
    #         time.sleep(0.5)
    #
    #         file_path = r"C:\Users\CT_USER\Desktop\test\Sample.CSV.xlsx"
    #
    #         upload_input = wait.until(
    #             EC.presence_of_element_located(self.upload_input)
    #         )
    #
    #         # hidden input hai, isliye direct send_keys
    #         upload_input.send_keys(file_path)
    #         time.sleep(1)
    #
    #         print("Import VAT return file uploaded successfully....!!")
    #
    #     except Exception as e:
    #         print(f"Error on Import Click/File Upload: {e}")
    #         raise


    def Send_Button(self):
        try:
            send = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_send))
            time.sleep(.2)
            send.click()
            time.sleep(.2)

            print("Click on Send button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Enter_Reviewer(self):
        try:
            review = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.enter_reviewer)
            )
            time.sleep(0.2)

            review.send_keys('Domenic torato (vikram.singh@capsitech.com)')
            time.sleep(0.5)

            review.send_keys(Keys.ENTER)
            time.sleep(0.5)

            print("Reviewer selected successfully....!!")

        except Exception as e:
            print(f"Error on Enter Reviewer: {e}")
            raise

    def Enter_Remarks(self, remarks):
        try:
            wait = WebDriverWait(self.driver, 20)

            iframe = wait.until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]"))
            )
            self.driver.switch_to.frame(iframe)

            body = wait.until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )
            body.click()
            body.send_keys(Keys.CONTROL, "a")
            body.send_keys(Keys.DELETE)
            body.send_keys(remarks)

            print("Remarks entered successfully....!!")

        except Exception as e:
            print(f"Error while entering remarks: {e}")
            raise

        finally:
            self.driver.switch_to.default_content()



    def Add_Attachment(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            import_file = wait.until(
                EC.element_to_be_clickable(self.add_attachment)
            )
            import_file.click()
            time.sleep(2)

            pyautogui.write(r"C:\Users\CT_USER\Desktop\test\Sample.CSV.xlsx")
            time.sleep(1)
            pyautogui.press("enter")

            print("Attachment file added successfully....!!")

        except Exception as e:
            print(f"Error on Import Click/File Upload: {e}")
            raise


    def Save_Request(self):
        try:
            request = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_request))
            time.sleep(.2)
            request.click()
            time.sleep(.2)

            print("Click on save request successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Review(self):
        try:
            review = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_review))
            time.sleep(.2)
            review.click()
            time.sleep(.2)

            print("Click on Review request successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Click_Next(self):
        try:
            next = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_next))
            time.sleep(.2)
            next.click()
            time.sleep(.2)

            print("Click on Next button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Click_Approve(self):
        try:
            approve = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_approve))
            time.sleep(.2)
            approve.click()
            time.sleep(.2)

            print("Click on approve button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Click_Yes(self):
        try:
            yes = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_yes))
            time.sleep(.2)
            yes.click()
            time.sleep(.2)

            print("Click on Yes button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def E_Sign(self):
        try:
            sign = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.e_sign))
            time.sleep(.2)
            sign .click()
            time.sleep(.2)

            print("Click on E-Sign button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Send_mail(self):
        try:
            mail = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.send_mail))
            time.sleep(.2)
            mail .click()
            time.sleep(.2)

            print("Click on send mail button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Send(self):
        try:
            send = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.send))
            time.sleep(.2)
            send.click()
            time.sleep(.2)

            print("Click on send button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Recipient(self):
        try:
            rec = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.recipient))
            time.sleep(.2)
            rec.send_keys('kritika.v.nandlal@accenture.com')
            time.sleep(.2)
            rec.send_keys(Keys.ENTER)
            time.sleep(0.5)

            print("Enter on Recipient Mail id  successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Mail_Form(self):
        try:
            wait = WebDriverWait(self.driver, 10)

            mail = wait.until(EC.presence_of_element_located(self.from_mail))
            time.sleep(0.2)
            self.driver.execute_script("arguments[0].click();", mail)
            time.sleep(0.5)

            mail_input = wait.until(EC.visibility_of_element_located(self.from_mail_input))
            mail_input.send_keys("no-reply")
            time.sleep(0.5)
            mail_input.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Change mail from successfully....!!")

        except Exception as e:
            print(f"Error on Click:{e}")
            raise


    def Click_Mail_Icon(self):
        try:
            icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_mail_icon))
            time.sleep(.2)
            icon.click()
            time.sleep(.2)

            print("Click on mail icon successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Review_Mail_New_Tab(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            old_tabs = self.driver.window_handles

            review = wait.until(
                EC.element_to_be_clickable(self.review_mail)
            )

            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).click(review).key_up(Keys.CONTROL).perform()

            wait.until(lambda d: len(d.window_handles) > len(old_tabs))
            self.driver.switch_to.window(self.driver.window_handles[-1])

            print("Review mail link opened successfully in new tab....!!")
            print("Current URL:", self.driver.current_url)

        except Exception as e:
            print(f"Error on CTRL+Click Review mail: {e}")
            raise

    # def Click_Review_Mail(self):
    #     try:
    #         review = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(self.review_mail)
    #         )
    #         time.sleep(0.2)
    #
    #         actions = ActionChains(self.driver)
    #         actions.key_down(Keys.CONTROL)
    #         actions.move_to_element(review)
    #         actions.click()
    #         actions.key_up(Keys.CONTROL)
    #         actions.perform()
    #
    #         time.sleep(0.2)
    #         print("Click on Review mail icon successfully....!!")
    #
    #     except Exception as e:
    #         print(f"Error on Click: {e}")
    #         raise

    def Click_Get_OTP(self):
        try:
            otp = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_get_otp))
            time.sleep(.2)
            otp.click()
            time.sleep(.2)

            print("Click on Get OTP successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Enter_OTP(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            otp_inputs = wait.until(
                EC.visibility_of_all_elements_located(self.otp_boxes)
            )

            otp = "969696"

            if len(otp) != len(otp_inputs):
                raise Exception(f"OTP length mismatch. Expected {len(otp_inputs)} digits but got {len(otp)} digits.")

            for i in range(len(otp)):
                otp_inputs[i].click()
                otp_inputs[i].clear()
                otp_inputs[i].send_keys(otp[i])
                time.sleep(0.2)

            print("OTP entered successfully....!!")

        except Exception as e:
            print(f"Error while entering OTP: {e}")
            raise

    def Proceed_Securely(self):
        try:
            proceed = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.proceed_securely))
            time.sleep(.2)
            proceed.click()
            time.sleep(.2)

            print("Click on proceed securely successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Accept(self):
        try:
            accept = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_accept))
            time.sleep(.2)
            accept.click()
            time.sleep(.2)

            print("Click on Accept button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Enter_Name_Signature(self):
        try:
            sign = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.enter_name_signature))
            time.sleep(.2)
            sign.send_keys('Testing')
            time.sleep(.2)

            print("Enter Name for signature successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Click_Sing_Button(self):
        try:
            sign_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_sing_button))
            time.sleep(.2)
            sign_btn.click()
            time.sleep(.2)

            print("Click on Sign Button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    # def Click_Okay(self):
    #     try:
    #         okay = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_okay))
    #         time.sleep(.2)
    #         okay.click()
    #         time.sleep(.2)
    #
    #         print("Click on Okay Button successfully....!!")
    #     except Exception as e:
    #         print(f"Error on Click:{e}")
    #         time.sleep(.2)

    def Click_Okay_And_Return_To_Previous_Tab(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            # before close, get all tabs
            tabs_before_close = self.driver.window_handles
            current_tab = self.driver.current_window_handle

            # choose previous tab as tab other than current
            previous_tabs = [tab for tab in tabs_before_close if tab != current_tab]
            if not previous_tabs:
                raise Exception("No previous tab found.")

            previous_tab = previous_tabs[-1]

            # click Okay
            okay = wait.until(
                EC.element_to_be_clickable(self.click_okay)
            )
            okay.click()
            time.sleep(1)

            print("Click on Okay button successfully....!!")

            # close current tab
            self.driver.close()
            time.sleep(1)

            # switch to previous tab
            self.driver.switch_to.window(previous_tab)
            time.sleep(1)

            print("Switched back to previous tab successfully....!!")

            # click close/cross button
            cross = wait.until(
                EC.element_to_be_clickable(self.close_cross)
            )
            self.driver.execute_script("arguments[0].click();", cross)
            time.sleep(0.5)

            print("Clicked on cross button successfully....!!")

        except Exception as e:
            print(f"Error in Click_Okay_And_Return_To_Previous_Tab: {e}")
            raise

    def Three_dot(self):
        try:
            dot = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_three_dot))
            time.sleep(.2)
            dot.click()
            time.sleep(.2)

            print("Click on three dot Button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Submit_HMRC(self):
        try:
            hmrc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_hmrc))
            time.sleep(.2)
            hmrc.click()
            time.sleep(.2)

            print("Click on Submit HMRC Button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Submit_VAT_Return(self):
        try:
            submit_vat = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_vat_return_submit))
            time.sleep(.2)
            submit_vat.click()
            time.sleep(.2)

            print("Click on Submit VAT return Button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Click_Download(self):
        try:
            download = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.click_download))
            time.sleep(.2)
            download.click()
            time.sleep(.2)

            print("Click on Download icon  Button successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)



















































