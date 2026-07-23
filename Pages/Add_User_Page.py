
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


class User:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Expense claims ------------------------------------------------------

# ------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='T.H. LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_expense_claims = (By.XPATH, "(//div[contains(text(),'Expense claims')])[1]")

        # --------------------------------------------User------------------------------------------------------------------

        self.click_expense_claims_button = (By.XPATH, "//button[.//span[normalize-space()='Expense']]")

        self.users_section = (By.XPATH, "//button[.//span[normalize-space()='Users']]")
        self.click_add_user = (By.XPATH, "//button[.//span[normalize-space()='User']]")
        self.click_name_field = (By.XPATH,
                                 "//label[normalize-space()='Name']/following::input[@type='text'][1]")
        self.enter_first_name = (By.XPATH,
                                 "//label[normalize-space()='First name']/following::input[@type='text'][1]")
        self.enter_name = (By.XPATH, "//label[normalize-space()='Last name']/following::input[@type='text'][2]")


        self.enter_ni_number = (By.XPATH, "//label[normalize-space()='NI Number']/following::input[@type='text'][1]")
        self.click_save_button = (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Save']]")
        self.click_expense_claims = (By.XPATH, "(//div[contains(text(),'Expense claims')])[1]")

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

    def Enter_Company(self, company_name="T.H. LIMITED", timeout=30, os=None):

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

# --------------------------------------------User----------------------------------------------------------------------

    def User_Section(self):
        try:
            user_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.users_section))
            time.sleep(.2)
            user_sec.click()
            time.sleep(.2)
            print("Click on User Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Add_User(self):
        try:
            click_user = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_add_user))
            time.sleep(.2)
            click_user.click()
            time.sleep(.2)
            print("Click on Add user icon successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Name_Field(self):
        # try:
            click_name = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_name_field))
            time.sleep(.2)
            click_name.click()
            time.sleep(.2)
            print("Click on  name icon successfully....!!")
        # except Exception as e:
        #     print(f"Error on Click:{e}")

    def Select_Title(self, title="Mr"):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        title_input = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[normalize-space()='First name']"
                    "/following::input[@role='combobox'][1]"
                )
            )
        )

        title_input.click()
        title_input.send_keys(title)
        title_input.send_keys(Keys.ARROW_DOWN)
        title_input.send_keys(Keys.ENTER)

        print(f"Title selected successfully: {title}")

    def Enter_name(self):

        for i in range(5):

            try:

                field = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(self.enter_name)
                )

                field.clear()
                field.send_keys(random_first_name)

                print("First Name entered successfully")
                return

            except StaleElementReferenceException:
                print(f"Retry {i + 1}")
                time.sleep(0.5)

        raise Exception("Unable to enter First Name.")



    def Enter_Ni_Number(self):
        # try:
            ni = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_ni_number))
            time.sleep(.2)
            ni.send_keys("AB123456C")
            time.sleep(.2)
            print("Enter first name successfully....!!")
        # except Exception as e:
        #     print(f"Error on Click:{e}")

    def Save_User(self):

            # try:
                user = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.click_save_button))
                time.sleep(.2)
                user.click()
                time.sleep(.2)
                print("Click on Save user successfully....!!")
            # except Exception as e:
            #     print(f"Error on Click:{e}")

    def Click_Expense_Claims(self):
        try:
            claims = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_expense_claims))
            time.sleep(.2)
            claims.click()
            time.sleep(.2)
            print("Click on Expense claims successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")






