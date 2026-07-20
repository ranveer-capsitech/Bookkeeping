
from faker import Faker
import time
from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime, timedelta
import re


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


class Expenseclaims:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Expense claims ------------------------------------------------------

# ------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_expense_claims = (By.XPATH, "(//div[contains(text(),'Expense claims')])[1]")

#----------------------------------------------expense_claims-----------------------------------------------------------

        self.click_expense_claims_button = (By.XPATH, "//button[.//span[normalize-space()='Expense']]")
        self.select_directors = (By.XPATH, "//label[normalize-space()='User']/following::div[contains(@class,'rs-placeholder')][1]")
        self.enter_remark = (By.XPATH, "//label[normalize-space()='Remarks']/following::input[@name='description'][1]")
        self.bill_no = (By.XPATH, "(//table[contains(@class,'table')]//input[@type='text'])[1]")
        self.enter_description = (By.XPATH,"//table[.//th[normalize-space()='Description']]   /tbody/tr[1]/td[     count(preceding-sibling::td) =     count(//th[normalize-space()='Description']/preceding-sibling::th)   ]//input[@type='text']")


        self.account = (By.XPATH, "//*[normalize-space()='Account']/following::input[@role='combobox'][1]")


        self.base_amount = (By.XPATH, "(//table[.//th[normalize-space()='Base amount']]   //tbody/tr[1]   //td[count(//th[normalize-space()='Base amount']/preceding-sibling::th)+1]   //input[contains(@class,'ms-TextField-field')] )[1]")
        self.vat = (By.XPATH, "(//th[normalize-space()='VAT']/ancestor::table[1]//tbody/tr[1]//div[contains(@class,'rs-input-container')])[2]")
        self.save_expense = (By.XPATH, "//button[.//span[normalize-space()='Save']]")
        self.save_expense_click = (By.XPATH, "//div[@role='dialog']//button[@title='Claim expense with reimbursement']//span[normalize-space()='Save']")





#------------------------------Method-----------------------------------------------------------------------------------

    def Select_Search(self):
            try:
                client = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.search))
                time.sleep(.2)
                client.click()
                time.sleep(.5)
                print("Click on search field successfully.....! ")
            except Exception as e:
                print(f"Error on click:{e}")

    def Enter_Company(self, company_name="1ST LIMITED", timeout=30, os=None):

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
            input = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)
            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Expense_Claims(self):
        try:
            claims = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_expense_claims))
            time.sleep(.2)
            claims.click()
            time.sleep(.2)
            print("Click on Expense claims successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

#-----------------------------------------------------------------------------------------------------------------------

    def Click_Expense_Claims_Button(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            # Click dropdown
            dropdown = wait.until(
                EC.presence_of_element_located(self.click_expense_claims_button)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dropdown
            )
            time.sleep(0.3)

            driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(0.5)


            print("Click on Expense Claims successfully....!!")

        except Exception as e:
            driver.save_screenshot("expense_claims_dropdown_error.png")
            print(f"Error while selecting Expense Claims: {e}")
            raise



    def Select_Directors(self):


            driver = self.driver
            wait = WebDriverWait(driver, 40)


            for _ in range(3):
                try:
                    container = wait.until(
                        EC.element_to_be_clickable(self.select_directors)
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

                    print("Select directors successfully....!!")
                    return
                except StaleElementReferenceException:

                    continue

            raise TimeoutException("Could not select a director from dropdown")

    def Enter_Remark(self):
        try:
            remark = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_remark))
            time.sleep(.2)
            remark.send_keys("only for testing")
            time.sleep(.2)
            print("Enter remark successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")


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





    def Enter_Bill_No(self):
        try:
            bill = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.bill_no))
            time.sleep(.2)
            bill.send_keys("1000")
            time.sleep(.2)
            print("Enter bill number successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Description(self):
        try:
            des = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_description))
            time.sleep(.2)
            des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")




    def Select_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            for _ in range(3):
                try:
                    account_container = wait.until(
                        EC.element_to_be_clickable(self.account)
                    )
                    driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        account_container
                    )
                    try:
                        account_container.click()
                    except ElementClickInterceptedException:

                        driver.execute_script("arguments[0].click();", account_container)
                    break
                except StaleElementReferenceException:
                    continue
            else:
                raise TimeoutException("Could not click Account dropdown")


            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)

            active.send_keys(Keys.ENTER)

            print("Select account successfully..... ")

        except TimeoutException:
            print("Timeout: Account dropdown not found / not visible.")


    def Base_Amount(self):

        try:
            wait = WebDriverWait(self.driver, 30)


            base = wait.until(EC.element_to_be_clickable(self.base_amount))


            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", base
            )
            time.sleep(0.2)


            base.click()
            time.sleep(0.2)


            base.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            base.send_keys(Keys.BACK_SPACE)
            time.sleep(0.5)


            base.send_keys("100")
            time.sleep(0.2)

            print("Base amount entered successfully....!!")

        except Exception as e:
            print(f"Error in Base_Amount: {e}")

    def Select_Vat(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            vat_cell = wait.until(
                EC.element_to_be_clickable(self.vat)
            )

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", vat_cell)
            time.sleep(0.3)

            vat_cell.click()
            time.sleep(0.3)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("VAT selected successfully!")

        except Exception as e:
            print(f"Error in Select_Vat: {e}")


    def Save_Expense(self):

        wait = WebDriverWait(self.driver, 30)

        # 1) Click Save
        save_btn = wait.until(EC.element_to_be_clickable(self.save_expense))
        save_btn.click()
        time.sleep(0.5)
        print("Expense Saved successfully............!!!")


        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.save_expense_click)
            )
            popup.click()
            print(" Expense Saved successfully............!!!")
        except Exception:
            print("No popup detected → continuing...")

