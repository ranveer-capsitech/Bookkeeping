
import random
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
formatted_date = tomorrow_date.strftime("%d-%m-%y")

random_email = fake.email()
random_email1 = fake.email()
random_indian_phone = fake.phone_number()
random_indian_phone_1 = fake.phone_number()
dob = fake.date_of_birth(minimum_age=18)
formatted_dob = dob.strftime('%d/%m/%Y')


class Receipts:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

# -------------------------------------------------Receipts---------------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

        self.receipts = (By.XPATH,
                         "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[4]/span[1]/span[1]/span[1]")

        self.add_receipts = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Receipt']")
        self.select_receive_from = (By.XPATH,
                                    "//label[normalize-space()='Received from']/following::div[contains(@class,'rs-input-container')][1]")
        self.select_amount = (By.XPATH,
                              "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@placeholder='amount'][1]")
        self.save_receipts = (By.XPATH, "//button[.//span[normalize-space()='Save'] and not(contains(.,'Save & New'))]")




#---------------------------------------------------Receipts-------------------------------------------------------------

    def Select_Search(self):
        try:
            client = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search))
            time.sleep(.2)
            client.click()
            time.sleep(.5)
            print("Click on search field successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Company(self, company_name="1ST LIMITED", timeout=12, os=None):

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
            click_on_selected_company = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.click_company))
            time.sleep(.3)
            click_on_selected_company.click()
            time.sleep(.2)
            print("Click on company successfully....!!")
        except Exception as e:
            print(f"Enter on click: {e}")
            time.sleep(.5)

    #--------------------------------------------------------------------------------------------------------------------


    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)
            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_Sales(self):
        try:
            sales = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.click_sales))
            time.sleep(.2)
            sales.click()
            time.sleep(.2)
            print("Click on Sales successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")


    def Receipts(self):
        try:
            click_receipts = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.receipts))
            time.sleep(.2)
            click_receipts.click()
            time.sleep(.2)
            print("click on credit section successfully......!!")
        except Exception as e:
             print(f"Error on click:{e}")

    def Add_Receipts(self):
        try:
            add_receipts = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.add_receipts))
            time.sleep(.2)
            add_receipts.click()
            time.sleep(.2)
            print("click for add new receipts successfully.....!! ")
        except Exception as e:
            print(f"Error on click:{e}")


    def Select_Receipts_from(self):
        driver = self.driver
        try:
            receipts = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.select_receive_from))
            time.sleep(.2)
            receipts.click()
            time.sleep(.2)
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print(" Customer selected successfully for Estimate!")

        except Exception as e:
            print(f" Could not select customer: {e}")

    def Select_Amount(self):
        try:
            amount = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.select_amount))
            time.sleep(.2)
            amount.click()
            time.sleep(.2)
            amount.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Customer selected successfully....!!")

        except Exception as e:
            print(f"Error on Click : {e}")


    def Enter_Amount(self):
        try:
            enter_a_amount = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_amount))
            time.sleep(.2)
            random_price = round(random.uniform(50, 999), 2)


            enter_a_amount.send_keys(Keys.CONTROL, 'a')
            enter_a_amount.send_keys(Keys.BACKSPACE)


            enter_a_amount.send_keys(str(random_price))
            enter_a_amount.send_keys(Keys.TAB)

            print(f" Entered random price: £{random_price}")
            time.sleep(0.5)
        except Exception as e:
             print(f"Error on Click : {e}")



    def Save_Receipt(self):


            wait = WebDriverWait(self.driver, 20)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_button = wait.until(
            EC.element_to_be_clickable(self.save_receipts)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(0.4)
            save_button.click()
            time.sleep(0.4)
            print(" Test Case -5 :  Pass: -  Receipt saved successfully.....!!")










