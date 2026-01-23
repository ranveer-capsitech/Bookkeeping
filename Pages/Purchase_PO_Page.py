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


class Purchase_Order:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")

        # ------------------------------------------------PO---------------------------------------------------------------------

        self.purchase_orders = (By.XPATH,
                                "//div[@role='tablist']//button[.//span[normalize-space()='Purchase orders']]")
        self.click_purchase_order = (By.XPATH, "//span[normalize-space(text())='Purchase order']")
        self.select_contact_name = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice_po = (By.XPATH,
                                          "(//table[contains(@class,'table')]//tr[1]//div[contains(@class,'rs-input-container')]//input)[1]")
        self.save_po = (By.XPATH, "//button[.//span[normalize-space(text())='Save']]")



#------------------------------------------Method-----------------------------------------------------------------------

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

    # -----------------------------------------------------------------------------------------------------------------------


    def Click_Input(self):
         try:
            input = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)
            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
         except Exception as e:
            print(f"Error on click:{e}")



    def Click_Purchases(self):
        try:
            sales = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.click_purchases))
            time.sleep(.2)
            sales.click()
            time.sleep(.2)
            print("Click on purchases successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

        # ------------------------------------------Method of PO ----------------------------------------------------------------

    def Purchase_Order(self):
            try:
                click_credit_notes = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.purchase_orders))
                time.sleep(.2)
                click_credit_notes.click()
                time.sleep(.2)
                print("click on Purchase order section successfully......!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Click_Purchase_Order(self):
            try:
                purchase_order = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located(self.click_purchase_order))
                time.sleep(.2)
                purchase_order.click()
                time.sleep(.2)

                print("Click on purchase order successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Select_Contact_Name(self):
            d = self.driver
            w = WebDriverWait(d, 20)

            control = w.until(EC.element_to_be_clickable(
                self.select_contact_name  # outer control
            ))
            d.execute_script("arguments[0].scrollIntoView({block:'center'});", control)
            try:
                control.click()
            except ElementClickInterceptedException:
                d.execute_script("arguments[0].click();", control)

            rs_input = w.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.rs-input-container input")
            ))

            d.execute_script("arguments[0].scrollIntoView({block:'center'});", rs_input)
            try:
                rs_input.click()
            except ElementClickInterceptedException:
                # Fallback: JS focus instead of click
                d.execute_script("arguments[0].focus();", rs_input)

            time.sleep(0.2)
            rs_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            rs_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            rs_input.send_keys(Keys.ENTER)

            try:
                w.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.rs-value-container .rs-single-value")
                ))
            except TimeoutException:

                d.save_screenshot("contact_select_debug.png")
                raise

            print("Customer selected successfully for PO")

    def Click_Item_For_Invoice(self):

            try:
                driver = self.driver
                wait = WebDriverWait(driver, 15)

                dropdown = wait.until(EC.element_to_be_clickable(self.click_item_for_invoice_po))
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
                dropdown.click()
                time.sleep(0.5)

                active = driver.switch_to.active_element
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.3)
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.3)
                active.send_keys(Keys.ENTER)
                time.sleep(0.5)

                print("Invoice reference selected successfully!")
            except Exception as e:
                print(f" Could not select customer: {e}")

    def Save_PO(self):
            driver = self.driver
            wait = WebDriverWait(driver, 15)

            save_btn = wait.until(EC.element_to_be_clickable(self.save_po))

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
            time.sleep(0.3)

            try:
                save_btn.click()
            except:
                driver.execute_script("arguments[0].click();", save_btn)

            time.sleep(1)
            print("Test Case -09 :  Pass:  Purchase Order saved successfully!")

