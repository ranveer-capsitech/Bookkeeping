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


class Purchase_Payment:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")

#--------------------------------------------Pyments--------------------------------------------------------------------

        self.payment = (By.XPATH,"//button[@role='tab' and .//span[normalize-space()='Payments']]")
        self.click_payment = (By.XPATH, "//button[.//span[normalize-space()='Payment']]")

        self.paid_to_supplier = (By.XPATH, "//label[normalize-space()='Paid to']/following::div[contains(@class,'rs-control')][1]")
        self.account = (By.XPATH, "//label[normalize-space(text())='Account']/following::div[contains(@class,'rs-input-container')]//input")
        #self.method = (By.XPATH, "//div[@id='react-select-17-placeholder']")
        self.enter_amount = (By.XPATH, "//input[@name='availableAmount']")
        self.save_payment = (By.XPATH, "//button[.//span[normalize-space(text())='Save']]")




#-----------------------------------------Payment-----------------------------------------------------------------------

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


    # def Click_Input(self):
    #      try:
    #         input = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_input_drop_down))
    #         time.sleep(.2)
    #         input.click()
    #         time.sleep(.2)
    #         print("Input drop down open successfully....!!")
    #      except Exception as e:
    #         print(f"Error on click:{e}")
    #
    #
    # def Click_Purchases(self):
    #     try:
    #         sales = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_purchases))
    #         time.sleep(.2)
    #         sales.click()
    #         time.sleep(.2)
    #         print("Click on purchases successfully....!!")
    #     except Exception as e:
    #         print(f"Error on Click:{e}")

    def Click_Input_Purchases(self):

        wait = WebDriverWait(
            self.driver,
            30,
            poll_frequency=0.2,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        try:
            # -----------------------------
            # STEP 1 : Open Inputs dropdown
            # -----------------------------
            input_arrow = wait.until(
                EC.presence_of_element_located(
                    self.click_input_drop_down
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                input_arrow
            )

            # Fresh locate before click
            input_arrow = wait.until(
                EC.presence_of_element_located(
                    self.click_input_drop_down
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                input_arrow
            )

            print("Inputs dropdown arrow clicked....!!")

            # -----------------------------
            # STEP 2 : Wait for Purchases
            # -----------------------------
            purchases = wait.until(
                EC.visibility_of_element_located(
                    self.click_purchases
                )
            )

            print("Purchases menu visible....!!")

            # -----------------------------
            # STEP 3 : Click immediately
            # -----------------------------
            purchases = wait.until(
                EC.visibility_of_element_located(
                    self.click_purchases
                )
            )

            self.driver.execute_script(
                """
                const element = arguments[0];

                const clickable =
                    element.closest('a') ||
                    element.closest('button') ||
                    element;

                clickable.click();
                """,
                purchases
            )

            print("Click on Purchases successfully....!!")

        except TimeoutException:
            print(
                "Timeout: Inputs opened but "
                "Purchases menu was not available."
            )
            raise

        except Exception as e:
            print(
                f"Error while opening Inputs/Purchases: "
                f"{type(e).__name__} - {e}"
            )
            raise


    def Payment_Section(self):

        try:
            payment_section = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.payment))
            time.sleep(.2)
            payment_section.click()
            time.sleep(.2)
            print("click on Payment section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_Payment(self):
        try:
            payment = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_payment))
            time.sleep(.2)
            payment.click()
            time.sleep(.2)

            print("Click on payment successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Paid_To_Supplier(self):
        d = self.driver
        w = WebDriverWait(d, 30)

        control = w.until(EC.element_to_be_clickable((
            By.XPATH,
            "//label[normalize-space()='Paid to']/following::div[contains(@class,'rs-control')][1]"
        )))
        d.execute_script("arguments[0].scrollIntoView({block:'center'});", control)
        control.click()
        time.sleep(0.2)

        rs_input = w.until(EC.element_to_be_clickable((
            By.XPATH,
            "//label[normalize-space()='Paid to']/following::div[contains(@class,'rs-input-container')]//input"
        )))
        rs_input.click()
        time.sleep(0.2)
        rs_input.send_keys(Keys.ARROW_DOWN)

        time.sleep(0.2)
        rs_input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        print("Select Supplier successfully!")

    def Paid_To_Supplier_Main(self):
        try:
            control = self.wait.until(
                EC.element_to_be_clickable(
                    self.paid_to_supplier
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                control
            )

            control.click()

            supplier_input = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//label[normalize-space()='Paid to']"
                        "/following::div[contains(@class,'rs-input-container')]"
                        "//input[1]"
                    )
                )
            )

            supplier_input.click()
            supplier_input.send_keys(
                Keys.ARROW_DOWN
            )
            supplier_input.send_keys(
                Keys.ENTER
            )

            print(
                "Supplier selected successfully."
            )

            return True

        except Exception as error:
            raise AssertionError(
                f"Could not select supplier: "
                f"{type(error).__name__}: {error}"
            ) from error


    def Select_Account(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            supplier_dropdown = wait.until(EC.element_to_be_clickable(self.account))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", supplier_dropdown )
            supplier_dropdown.click()
            time.sleep(0.5)
            active = driver.switch_to.active_element
            time.sleep(.2)
            active.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Select Account type successfully!")
        except Exception as e:
            print(f" Could not select Account type: {e}")

    def Enter_Amount(self):
        try:
            enter_amount = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_amount)
            )

            time.sleep(0.2)

            # Click the field
            enter_amount.click()
            time.sleep(0.2)

            # Select all and clear
            enter_amount.send_keys(Keys.CONTROL + "a")
            time.sleep(0.2)
            enter_amount.send_keys(Keys.DELETE)
            time.sleep(0.2)

            # Enter new amount
            enter_amount.send_keys("100")
            time.sleep(0.2)

            print("Amount entered successfully....!!")

        except Exception as e:
            print(f"Error while entering amount: {e}")

    def Save_payment(self):
        try:
          save_paymt = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_payment))
          time.sleep(.2)
          save_paymt.click()
          time.sleep(.2)

          print(" Test Case  :  Pass:  Payment saved successfully....!!")
        except Exception as e:
          print(f"Error on click:{e}")

    def wait_for_loader_to_disappear(
            self,
            timeout=8
    ):
        loader_locator = (
            By.XPATH,
            "//*["
            "contains(@class,'spinner') or "
            "contains(@class,'Spinner') or "
            "contains(@class,'loading') or "
            "contains(@class,'Loading') or "
            "contains(@class,'ms-Spinner') or "
            "contains(@class,'ms-Overlay') or "
            "contains(@class,'ant-spin-spinning')"
            "]"
        )

        try:
            WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=0.2
            ).until(
                EC.invisibility_of_element_located(
                    loader_locator
                )
            )

        except TimeoutException:
            pass

    def Refresh_Page(self):
        try:
            self.driver.refresh()

            WebDriverWait(self.driver, 30).until(
                lambda driver: driver.execute_script(
                    "return document.readyState"
                ) == "complete"
            )

            print("Page refreshed successfully.")

        except Exception as error:
            self.driver.save_screenshot(
                "page_refresh_failure.png"
            )

            print(
                f"Page refresh failed: "
                f"{type(error).__name__}: {error}"
            )
            raise

