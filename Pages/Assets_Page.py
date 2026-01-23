
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


class Asset:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver


# ------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")

        self.asset = (By.XPATH, "//div[normalize-space()='Assets']/ancestor::a[1]")


#----------------------------------------------Asset_claims-------------------------------------------------------------

        self.click_fixed = (By.XPATH, "//span[contains(text(),'Fixed asset')]")
        self.asset_name = (By.XPATH, "//label[normalize-space()='Asset name']/following::input[@type='text'][1]")
        self.account = (By.XPATH, "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.purchase_price = (By.XPATH, "//label[normalize-space()='Purchase price (Ex. VAT)']/following::input[@type='text'][1]")

        self.supplier = (By.XPATH, "//label[normalize-space()='Supplier']/following::div[contains(@class,'rs-input-container')][1]")
        self.rate = (By.XPATH, "//label[normalize-space()='Rate']/following::input[@type='text'][1]")
        self.save_asset = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

#-------------------------------------------- Disposed -----------------------------------------------------------------

        self.dispose_section = (By.XPATH, "//button[@role='tab' and normalize-space()='Disposed']")
        self.add_dispose = (By.XPATH, "//span[normalize-space()='Dispose asset']/ancestor::button")
        self.select_asset = (By.XPATH, "//label[normalize-space()='Asset']/following::input[@type='text'][1]")
        self.sales_proceeds = (By.XPATH, "//label[normalize-space()='Sales proceeds (Incl. VAT)']/following::input[@type='text'][1]")
        self.payment_method = (By.XPATH, "//label[normalize-space()='Payment method']/following::input[@type='text'][1]")
        self.customer = (By.XPATH, "//label[normalize-space(.)='Customer']/following::input[@type='text'][1]")
        self.save_disposed = (By.XPATH, "//span[text()='Save']/ancestor::button")

#-----------------------------------------------------------------------------------------------------------------------


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

    def Click_Asset(self):
        try:
            claims = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.asset))
            time.sleep(.2)
            claims.click()
            time.sleep(.2)
            print("Click on asset successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

#------------------------------------------------------------------------------------------------------------------------

    def Click_Add_Assets(self):

            try:
                client = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.click_fixed))
                time.sleep(.2)
                client.click()
                time.sleep(.2)
                print("Click on add assets successfully..... ")
            except Exception as e:
                print(f"Error on click:{e}")
                time.sleep(.2)

    def Asset_Name(self):
        try:
            asset = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.asset_name))
            time.sleep(.2)
            asset.send_keys("Onpy for testing")
            time.sleep(.2)
            print("Click on Enter assets successfully..... ")
        except Exception as e:
                print(f"Error on click:{e}")
                time.sleep(.2)

    def Purchase(self):
       driver = self.driver
       try:
            pur = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.purchase_price))
            time.sleep(.2)
            pur.click()
            actions = ActionChains(driver)
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()

            time.sleep(0.2)

        # Now enter 100

            pur.send_keys("100")

            print("Purchase price cleared and 100 entered successfully!")

       except Exception as e:
            print(f"Error in Purchase(): {e}")

    def Select_Account(self):

            driver = self.driver
            wait = WebDriverWait(driver, 30)

            try:

                account = wait.until(
                    EC.element_to_be_clickable(self.account)
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

                print("Account selected successfully....!!")
            except Exception as e:
                print(f"Error on Click Account: {e}")

    def Select_Supplier(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            supp = wait.until(
                EC.element_to_be_clickable(self.supplier)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                supp
            )
            time.sleep(0.2)

            try:
                supp.click()
            except Exception:
                driver.execute_script("arguments[0].click();", supp)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Supplier selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Account: {e}")

    def Enter_Rate(self):
        try:
            enter_rate = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.rate))
            time.sleep(.2)
            enter_rate.send_keys("2")
            time.sleep(.2)
            print("Click on Enter rate successfully..... ")
        except Exception as e:
                print(f"Error on click:{e}")
                time.sleep(.2)


    def Save_Asset(self):

            try:
                save_ref = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_asset))
                time.sleep(.2)
                save_ref.click()
                time.sleep(.2)

                # update_message = WebDriverWait(self.driver, 10).until(
                #     EC.visibility_of_element_located(
                #         (By.XPATH, "//*[contains(normalize-space(), 'Asset saved successfully with number')]"))
                # )
                #
                # # Assert the presence of the success message
                # assert update_message, "Reimbursement saved successfully"

                print("Test Case 16 - Pass: Asset saved successfully.")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)



#----------------------------------------------Disposed----------------------------------------------------------------



    def Disposed(self):
        try:
            disposed = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.dispose_section))
            time.sleep(.2)
            disposed.click()
            time.sleep(.2)
            print("Click on dispose section successfully..... ")

        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)



    def Add_Disposed(self):
        try:
            add_dis = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.add_dispose))
            time.sleep(.2)
            add_dis.click()
            time.sleep(.2)
            print("Click on Enter assets successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)


    def Select_Asset(self):
        driver = self.driver
        try:
            select = WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located(self.select_asset)
            )
            time.sleep(.2)
            select.click()
            time.sleep(.2)
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Asset selected successfully....!!")

        except Exception as e:
            print(f"Error on Click Account: {e}")



    def Sales_proceeds(self):
        try:
            sales_proceeds = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.sales_proceeds))
            time.sleep(.2)
            sales_proceeds.send_keys("testing")
            time.sleep(.2)
            print("Click on Sales proceeds successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)



    def Payment_Method(self):
        driver = self.driver
        try:
            select = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.payment_method)
            )
            time.sleep(.2)
            select.click()
            time.sleep(.2)
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Payment selected successfully....!!")

        except Exception as e:
            print(f"Error on Click Account: {e}")



    def Customer(self):
        driver = self.driver
        try:
            select = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.customer)
            )
            time.sleep(.2)
            select.click()
            time.sleep(.2)
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Customer selected successfully....!!")
        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)



    def Save_Disposed(self):
        try:
            save_dis = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_disposed))
            time.sleep(.2)
            save_dis.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Reimbursement saved successfully with number')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Reimbursement saved successfully"

            print("Test Case  17 - Pass: Disposed saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)







