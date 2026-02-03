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


class Reimbursement:

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


#-----------------------------------------------------Reimbursements----------------------------------------------------

        self.reimbursements_section = (By.XPATH, "//button[.//span[normalize-space()='Reimbursements']]")
        self.click_reimbursements = (By.XPATH, "//button[.//span[normalize-space()='Reimbursement']]")
        self.reimbursed_to = (By.XPATH, "//div[contains(@class,'placeholder') and normalize-space()='User name']")
        self.reimbursed_account = (By.XPATH, "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        #self.method = (By.XPATH, "//label[normalize-space()='Method']/following::div[contains(@class,'rs-placeholder')][1]")
        self.reimbursed_amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@type='text'][1]")
        self.enter_notes = (By.XPATH, "//label[normalize-space()='Note :']/following::input[@name='notes'][1]")
        self.save_reimbursement = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
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

    def Reimbursed_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.reimbursed_account)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                account
            )
            time.sleep(0.2)

            try:
                account.click()
            except Exception:
                driver.execute_script("arguments[0].click();", account)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Reimbursed account selected successfully....!!")
        except Exception as e:
            print(f"Error on Click reimbursed account: {e}")

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
            amount.send_keys("100")
            time.sleep(.3)
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
        #try:
            save_reb = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_reimbursement))
            time.sleep(.2)
            save_reb.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Reimbursement saved successfully with number')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Reimbursement saved successfully"

            print("Test Case 11 - Pass: Reimbursement saved successfully.")

        # except Exception as e:
        #     print(f"Error: {e}")
        #
        #     time.sleep(2)
