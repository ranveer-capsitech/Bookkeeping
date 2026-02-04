import py
from faker import Faker
import time
import pyautogui as py
from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
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


class Budget:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.--------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")


        self.account = (By.XPATH, "//span[normalize-space()='Account']")


#--------------------------------------------Add Budget-----------------------------------------------------------------

        self.click_add_budget = (By.XPATH, "//li[@title='Budget manager']//a[@id='budgetManager']")
        self.add_new_budget = (By.XPATH, "//button[.//span[normalize-space()='Budget'] and .//i[@data-icon-name='Add']]")
        self.enter_name = (By.XPATH, "//span[normalize-space()='Name']/following::input[@name='name'][1]")
        self.select_date = (By.XPATH, "//div[contains(text(),'Select')]")
        self.click_on_save = (By.XPATH, "//span[contains(text(),'Save')]")

        self.enter_amount_1st = (By.XPATH, "//input[@name='profitAndLoss.[1].[0].items[0].value']")
        self.enter_amount_2nd = (By.XPATH, "//input[@name='profitAndLoss.[1].[0].items[1].value']")
        self.enter_amount_3rd = (By.XPATH, "//input[@name='profitAndLoss.[1].[0].items[2].value']")
        self.save_button = (By.XPATH, "//button[.//span[normalize-space()='Save']]")


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

    def Click_Add_Budget(self):
        try:
            wait = WebDriverWait(self.driver, 30)


            btn = wait.until(EC.element_to_be_clickable(self.click_add_budget))


            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)


            try:
                btn.click()
            except Exception:
                # 4) Fallback: action chain click
                ActionChains(self.driver).move_to_element(btn).pause(0.1).click().perform()

            print("Click for add budget successfully.....!!")

        except TimeoutException:
            raise TimeoutException(
                f"'Add Budget' button not found/clickable in 30s. Locator: {self.click_add_budget}"
            )


    def Add_New_Budget(self):
        try:
            new_budget = WebDriverWait(self.driver,30).until(EC.presence_of_element_located(self.add_new_budget))
            time.sleep(.2)
            new_budget.click()
            time.sleep(.2)
            print("Click on new add butten successfully.....!")
        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(.5)



    def Enter_Name(self):
        try:
            name_el = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_name)
            )
            time.sleep(0.2)

            #  store the name in object
            self.entered_name = random_first_name

            name_el.clear()
            name_el.send_keys(self.entered_name)

            time.sleep(0.2)
            print(f"Name entered successfully: {self.entered_name}")

        except Exception as e:
            print(f"Enter on click: {e}")
            time.sleep(0.5)



    def Select_Date(self):
        wait = WebDriverWait(self.driver, 20)

        control = (By.XPATH, "//span[normalize-space()='Start date']/following::div[contains(@class,'rs-control')][1]")


        wait.until(EC.element_to_be_clickable(control)).click()


        options = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.rs-menu div.rs-option")
        ))
        options[1].click()



    def Click_Save(self):

        try:
            save = WebDriverWait(self.driver,30).until(
                EC.presence_of_element_located(self.click_on_save)
            )
            time.sleep(.2)
            save.click()
            print("Enter budget successfully....!!")
            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(normalize-space(), 'Budget saved successfully')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Budget saved successfully"

            print("Test Case 20  - Pass: Refund saved successfully.")

        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(.5)


    def Click_On_Saved_Name(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            #row_xpath = f"//tr[.//*[normalize-space()='{self.entered_name}']]"

            row_xpath = f"//div[.//*[normalize-space()='{self.entered_name}']]"

            row = wait.until(EC.element_to_be_clickable((By.XPATH, row_xpath)))
            time.sleep(.2)
            row.click()
            time.sleep(.2)
            print("Clicked row for:", self.entered_name)
        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(.5)

    def Enter_Amount_First(self):
        try:
            wait = WebDriverWait(self.driver, 30)


            self.entered_amount = "1000"

            amount_el = wait.until(EC.element_to_be_clickable(self.enter_amount_1st))
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", amount_el)


            amount_el.click()
            time.sleep(0.2)


            amount_el.send_keys(Keys.CONTROL, "a")
            amount_el.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)


            amount_el.send_keys(self.entered_amount)


            amount_el.send_keys(Keys.TAB)
            time.sleep(0.5)


            actual_value = amount_el.get_attribute("value")
            print(f"Amount typed: {self.entered_amount} | UI value now: {actual_value}")


        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(5)

    def Enter_Amount_Second(self):
        try:
            wait = WebDriverWait(self.driver, 30)


            self.entered_amount = "1000"

            amount_el = wait.until(EC.element_to_be_clickable(self.enter_amount_2nd))
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", amount_el)


            amount_el.click()
            time.sleep(0.2)


            amount_el.send_keys(Keys.CONTROL, "a")
            amount_el.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)


            amount_el.send_keys(self.entered_amount)


            amount_el.send_keys(Keys.TAB)
            time.sleep(0.5)


            actual_value = amount_el.get_attribute("value")
            print(f"Amount typed: {self.entered_amount} | UI value now: {actual_value}")


        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(5)

    def Enter_Amount_Third(self):
        try:
            wait = WebDriverWait(self.driver, 30)


            self.entered_amount = "1000"

            amount_el = wait.until(EC.element_to_be_clickable(self.enter_amount_3rd))
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", amount_el)


            amount_el.click()
            time.sleep(0.2)


            amount_el.send_keys(Keys.CONTROL, "a")
            amount_el.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)


            amount_el.send_keys(self.entered_amount)


            amount_el.send_keys(Keys.TAB)
            time.sleep(0.5)


            actual_value = amount_el.get_attribute("value")
            print(f"Amount typed: {self.entered_amount} | UI value now: {actual_value}")


        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(5)

    def Click_On_Saved(self):
        try:
            wait = WebDriverWait(self.driver, 30)


            save = wait.until(EC.element_to_be_clickable(self.save_button))
            time.sleep(.2)
            save.click()
            time.sleep(.2)
            print("Data saved successfully!")
            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(normalize-space(), 'Budget fields updated successfully.')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Budget fields updated successfully."

            print("Test Case 21  - Pass: Budget fields updated successfully.")

        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(.5)



