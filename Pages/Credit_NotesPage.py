import os

from faker import Faker
import time
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
formatted_date = tomorrow_date.strftime("%d-%m-%y")  # Adjust format as needed

random_email = fake.email()
random_email1 = fake.email()
random_indian_phone = fake.phone_number()
random_indian_phone_1 = fake.phone_number()
dob = fake.date_of_birth(minimum_age=18)
formatted_dob = dob.strftime('%d/%m/%Y')


class Credit_Notes:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Credit notes---------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")


        self.click_input_drop_down = (By.XPATH,"//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

        self.click_credit_notes = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[2]/span[1]")
        self.credit_notes = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Credit note']")
        self.customer_name = (By.XPATH, "//div[contains(text(),'Customer name')]")
        self.invoice_ref_no = (By.XPATH, "//*[normalize-space()='Invoice ref. no.']/following::div[contains(@class,'rs-input-container')][1]")
        self.clicks_save = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.paid_from_locators = (By.XPATH, "//*[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.add_discount = (By.XPATH, "//input[@name='discount']")

        self.click_for_enter_note = (By.XPATH,
                                     "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note = (By.XPATH,
                          "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")


#-----------------------------------------Methods-----------------------------------------------------------------------

    def Select_Search(self):
        try:
            client = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
            time.sleep(.2)
            client.click()
            time.sleep(.5)
            print("Click on search field successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Company(self, company_name="1ST LIMITED", timeout= 30):

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

#------------------------------------------------------------------------------------------------------------------------


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


    def Click_Credit_Notes(self):
        try:
            click_credit_notes = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.click_credit_notes))
            time.sleep(.2)
            click_credit_notes.click()
            time.sleep(.2)
            print("click on credit section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Add_Credit_Note(self):
        try:
            credit = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.credit_notes))
            time.sleep(.2)
            credit.click()
            time.sleep(.2)

            print("Click for add credit  successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Customer_for_Credit_Note(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            #  Click on the dropdown field
            field = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[contains(@class,'rs-input-container')]"
            )))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
            field.click()
            time.sleep(0.5)

            # Use keyboard to select first option
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print(" Customer selected successfully for Credit Note......!!")

        except Exception as e:
            print(f" Could not select customer: {e}")

    def Invoice_ref(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        retries = 3  # maximum attempts

        for attempt in range(retries):
            try:
                # Locate dropdown
                dropdown = wait.until(EC.element_to_be_clickable(self.invoice_ref_no))
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
                dropdown.click()
                time.sleep(0.4)

                # Select next option
                active = driver.switch_to.active_element
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ENTER)
                time.sleep(0.5)

                # ✔ CHECK SAVE BUTTON ENABLED OR NOT
                save_button = wait.until(EC.presence_of_element_located(self.clicks_save))

                is_enabled = save_button.is_enabled()

                if is_enabled:
                    print("Invoice reference selected successfully......!!")
                    return True

                else:
                    print(f"Save button still disabled… retrying ({attempt + 1}/{retries})")
                    time.sleep(1)

            except Exception as e:
                print(f"Error selecting invoice reference (attempt {attempt + 1}): {e}")
                time.sleep(1)

        print(" Failed: Save button not enabled after retries.....!")
        return False

    # def Invoice_ref(self):
    #     try:
    #         driver = self.driver
    #         wait = WebDriverWait(driver, 15)
    #
    #
    #         dropdown = wait.until(EC.element_to_be_clickable((self.invoice_ref_no)))
    #         driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
    #         dropdown.click()
    #         time.sleep(0.5)
    #
    #         active = driver.switch_to.active_element
    #         active.send_keys(Keys.ARROW_DOWN)
    #         time.sleep(0.3)
    #         active.send_keys(Keys.ARROW_DOWN)
    #         time.sleep(0.3)
    #         active.send_keys(Keys.ENTER)
    #         time.sleep(0.5)
    #
    #         print("Invoice reference selected successfully!")
    #     except Exception as e:
    #         print(f" Could not select customer: {e}")

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




    def Save_Credit_Notes(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_credit_note = wait.until(
                EC.element_to_be_clickable(self.clicks_save)
            )
            time.sleep(.2)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_credit_note)
            time.sleep(0.4)
            save_credit_note.click()
            time.sleep(0.4)
            print("click on save credit note successfully....!!")
        except Exception as e:
            print(f" Could not select customer: {e}")



    def Paid_From(self):
        try:

            driver = self.driver
            wait = WebDriverWait(driver, 30)

            dropdown = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[normalize-space()='Paid from']/following::div[contains(@class,'rs-input-container')][1]"
            )))

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
            time.sleep(0.5)
            dropdown.click()
            time.sleep(0.5)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ENTER)

            print(" 'Paid from' selected successfully.....!")
        except Exception as e:
            print(f" Could not select customer: {e}")



    def Click_Save_Button(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)


        save_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@role='dialog']//button[@title='Save' and .//span[normalize-space()='Save']]"
        )))

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
        time.sleep(0.3)

        try:
            save_btn.click()
        except:
            driver.execute_script("arguments[0].click();", save_btn)

        time.sleep(1)
        print(" Test Case -4 : Pass :  Credit note saved successfully for Sales...!")



    #-------------------------------------------------------------------------------------------------------------------







