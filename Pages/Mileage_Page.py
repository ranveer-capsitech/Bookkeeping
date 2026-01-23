
from faker import Faker
import time
from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
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


class Mileage:

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

#----------------------------------------------mileage_claims-----------------------------------------------------------

        self.mileages_section = (By.XPATH, "//button[@name='Mileage claims']")
        self.click_add_mileages = (By.XPATH, "//button[@aria-label='btnAddMileageClaim']")
        self.select_directors_mileages = (By.XPATH,
                                          "//label[normalize-space()='User']/following::div[contains(@class,'rs-placeholder')][1]")
        self.enter_remark_mileages = (By.XPATH, "//label[normalize-space()='Remarks']/following::input[1]")
        self.engine_type = (By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.enter_description_mileage = (By.XPATH,
                                          "//table[.//th[normalize-space()='Description']]   /tbody/tr[1]/td[     count(preceding-sibling::td) =     count(//th[normalize-space()='Description']/preceding-sibling::th)   ]//input[@type='text']")
        self.mileage = (By.XPATH, "//th[normalize-space()='Mileage (miles)']/following::input[@type='number'][1]")
        self.rate = (By.XPATH,
                     "//th[normalize-space()='Rate']/following::div[contains(@class,'rs-input-container')][2]//input")
        self.save_mileages = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        self.save_expense_click = (By.XPATH,
                                   "//div[@role='dialog']//button[@title='Claim expense with reimbursement']//span[normalize-space()='Save']")




        # -------------------------------------------------mileages_section---------------------------------------------

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


    def Mileages_Section(self):
            try:
                mileages_sec = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.mileages_section))
                time.sleep(.2)
                mileages_sec.click()
                time.sleep(.2)
                print("Click on Mileages Section successfully....!!")
            except Exception as e:
                print(f"Error on Click:{e}")

    def Click_Mileages(self):
            try:
                click_mileages = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.click_add_mileages))
                time.sleep(.2)
                click_mileages.click()
                time.sleep(.2)
                print("Click on Mileages successfully....!!")
            except Exception as e:
                print(f"Error on Click:{e}")

    def Select_Directors(self):

            driver = self.driver
            wait = WebDriverWait(driver, 35)

            for _ in range(3):
                try:
                    container = wait.until(
                        EC.element_to_be_clickable(self.select_directors_mileages)
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

    def Enter_Remark_Mileages(self):
            try:
                wait = WebDriverWait(self.driver, 30)

                remark = wait.until(EC.element_to_be_clickable(self.enter_remark_mileages))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", remark
                )

                time.sleep(0.3)

                remark.click()
                time.sleep(0.2)
                remark.send_keys(Keys.CONTROL, "a")
                time.sleep(0.1)
                remark.send_keys(Keys.BACK_SPACE)
                time.sleep(0.1)
                remark.send_keys("Mileage remark auto-test")
                time.sleep(0.2)

                print("Enter remark for mileage successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Engine_Type(self):

            driver = self.driver
            try:
                wait = WebDriverWait(driver, 30)

                container = wait.until(EC.element_to_be_clickable(self.engine_type))

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", container
                )
                time.sleep(0.2)

                try:
                    container.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", container)

                time.sleep(0.2)

                active = driver.switch_to.active_element
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ENTER)
                time.sleep(0.2)

                print("Engine type entered successfully....!!")

            except Exception as e:
                print(f"Error on click: {e}")

    def Enter_Description_Mileage(self):

            try:
                des = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.enter_description_mileage))
                time.sleep(.2)
                des.send_keys("Only for testing")
                time.sleep(.2)
                print("Enter Description successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Mileage(self):
            try:
                select = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.mileage))
                time.sleep(.2)
                select.send_keys("5")
                time.sleep(.2)
                print("Enter mileage successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Select_Rate(self):
            driver = self.driver

            try:
                wait = WebDriverWait(self.driver, 30)

                select_rate = wait.until(EC.element_to_be_clickable(self.rate))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", select_rate
                )
                time.sleep(0.2)

                select_rate.click()
                time.sleep(0.2)

                active = driver.switch_to.active_element
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ENTER)
                time.sleep(0.2)

                # select_rate.send_keys(Keys.CONTROL, "a")
                # time.sleep(0.2)
                # select_rate.send_keys(Keys.BACK_SPACE)
                # time.sleep(0.5)
                #
                # select_rate.send_keys("100")
                # time.sleep(0.2)

                print("Rate entered successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Save_Mileage(self):

            try:

                save_btn = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(self.save_mileages)
                )
                save_btn.click()
                time.sleep(2)

                print("Save button clicked!")

                try:
                    popup = WebDriverWait(self.driver, 30).until(
                        EC.visibility_of_element_located(self.save_expense_click)
                    )
                    popup.click()
                    print("Popup detected → Saved using popup button!")
                    time.sleep(3)

                except Exception:
                    print("No popup detected → Checking for success message...")

                    update_message = WebDriverWait(self.driver, 30).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//*[contains(normalize-space(), 'Mileage saved successfully with number')]")
                        )
                    )

                    assert update_message, "Mileage saved successfully"
                    print("Test Case : 12 - Pass: Mileage saved successfully.")

            except Exception as e:
                print(f"Error in Save_Expense: {e}")

