import pyautogui
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


class Expenseclaims:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Expense claims ------------------------------------------------------

# ------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH,
                                      "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_expense_claims = (By.XPATH, "(//div[contains(text(),'Expense claims')])[1]")

#----------------------------------------------expense_claims-----------------------------------------------------------

        self.click_expense_claims_button = (By.XPATH, "//button[.//span[text()='Expense']]")
        self.select_directors = (By.XPATH, "//label[normalize-space()='User']/following::div[contains(@class,'rs-placeholder')][1]")
        self.enter_remark = (By.XPATH, "//label[normalize-space()='Remarks']/following::input[@name='description'][1]")
        self.bill_no = (By.XPATH, "(//table[contains(@class,'table')]//input[@type='text'])[1]")
        self.enter_description = (By.XPATH,"//table[.//th[normalize-space()='Description']]   /tbody/tr[1]/td[     count(preceding-sibling::td) =     count(//th[normalize-space()='Description']/preceding-sibling::th)   ]//input[@type='text']")
        self.account = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.base_amount = (By.XPATH, "(//table[.//th[normalize-space()='Base amount']]   //tbody/tr[1]   //td[count(//th[normalize-space()='Base amount']/preceding-sibling::th)+1]   //input[contains(@class,'ms-TextField-field')] )[1]")
        self.vat = (By.XPATH, "(//th[normalize-space()='VAT']/ancestor::table[1]//tbody/tr[1]//div[contains(@class,'rs-input-container')])[2]")
        self.save_expense = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

#-----------------------------------------------------mileages----------------------------------------------------------

        self.mileages_section = (By.XPATH,"//button[@name='Mileage claims']")
        self.click_add_mileages = (By.XPATH,"//button[@aria-label='btnAddMileageClaim']")
        self.select_directors_mileages = (By.XPATH, "//label[normalize-space()='User']/following::div[contains(@class,'rs-placeholder')][1]")
        self.enter_remark_mileages = (By.XPATH, "//label[normalize-space()='Remarks']/following::input[1]")
        self.engine_type = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.enter_description_mileage = (By.XPATH,
                                  "//table[.//th[normalize-space()='Description']]   /tbody/tr[1]/td[     count(preceding-sibling::td) =     count(//th[normalize-space()='Description']/preceding-sibling::th)   ]//input[@type='text']")
        self.mileage = (By.XPATH, "//th[normalize-space()='Mileage (miles)']/following::input[@type='number'][1]")
        self.rate = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[5]/div[1]/div[1]/div[1]/div[1]/div[1]")
        self.save_mileages = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

#------------------------------------------------------------------------------------------------------------------------


#------------------------------Method-----------------------------------------------------------------------------------

    def Select_Business(self):
        try:
            client = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.select_business_name))
            time.sleep(.2)
            client.click()
            time.sleep(.2)
            print("Select a business name successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Input(self):
        try:
            input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)
            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Expense_Claims(self):
        try:
            claims = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.click_expense_claims))
            time.sleep(.2)
            claims.click()
            time.sleep(.2)
            print("Click on Expense claims successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

#-----------------------------------------------------------------------------------------------------------------------


    def Click_Expense_Claims_Button(self):

            driver = self.driver
            wait = WebDriverWait(driver, 15)

            for _ in range(3):
                try:
                    control = wait.until(
                        EC.element_to_be_clickable(self.click_expense_claims_button)
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", control)
                    control.click()
                    break
                except StaleElementReferenceException:
                    continue
            else:
                raise TimeoutException("Could not click Expense Claims dropdown")


            for _ in range(3):
                try:
                    active = driver.switch_to.active_element
                    active.send_keys(Keys.ARROW_DOWN)
                    time.sleep(0.3)  # optional
                    active.send_keys(Keys.ENTER)
                    time.sleep(0.3)  # optional
                    print("Click on Expense Claims successfully....!!")
                    return
                except StaleElementReferenceException:

                    continue

            raise TimeoutException("Could not select value in Expense Claims dropdown")

    def Select_Directors(self):


            driver = self.driver
            wait = WebDriverWait(driver, 15)


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
            remark = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.enter_remark))
            time.sleep(.2)
            remark.send_keys("only for testing")
            time.sleep(.2)
            print("Enter remark successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")



    def Enter_Bill_No(self):
        try:
            bill = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.bill_no))
            time.sleep(.2)
            bill.send_keys("1000")
            time.sleep(.2)
            print("Enter bill number successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Description(self):
        try:
            des = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_description))
            time.sleep(.2)
            des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")




    def Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

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
            wait = WebDriverWait(self.driver, 15)


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
        wait = WebDriverWait(driver, 15)

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


    def Save_Expenseclaims(self):
        try:
            save_exp = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.save_expense))
            time.sleep(.2)
            save_exp.click()
            time.sleep(.2)


            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(normalize-space(), 'Expense saved successfully with number')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Expense saved successfully"

            print("Test Case  - Pass: Expense saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

#-------------------------------------------------mileages_section------------------------------------------------------

    def Mileages_Section(self):
        try:
            mileages_sec = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.mileages_section))
            time.sleep(.2)
            mileages_sec.click()
            time.sleep(.2)
            print("Click on Mileages Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")


    def Click_Mileages(self):
            try:
                click_mileages = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.click_add_mileages))
                time.sleep(.2)
                click_mileages.click()
                time.sleep(.2)
                print("Click on Mileages successfully....!!")
            except Exception as e:
                print(f"Error on Click:{e}")

    def Select_Directors(self):


            driver = self.driver
            wait = WebDriverWait(driver, 15)


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
            wait = WebDriverWait(self.driver, 20)

            # 1. Wait until the element is present & clickable
            remark = wait.until(EC.element_to_be_clickable(self.enter_remark_mileages))

            # 2. Scroll it into view (sometimes it’s technically visible but off-screen)
            self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", remark
            )

            # small pause
            time.sleep(0.3)

            # 3. Clear & type
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
                wait = WebDriverWait(driver, 15)

                # 1. Wait for the dropdown container (not the placeholder) to be clickable
                container = wait.until(EC.element_to_be_clickable(self.engine_type))

                # 2. Scroll into view
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", container
                )
                time.sleep(0.2)

                # 3. Try normal click; if intercepted, use JS click
                try:
                    container.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", container)

                time.sleep(0.2)

                # 4. Now the React-Select input should be the active element
                active = driver.switch_to.active_element
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ENTER)
                time.sleep(0.2)

                print("Engine type entered successfully....!!")

            except Exception as e:
                print(f"Error on click: {e}")


        # driver = self.driver
        #
        # try:
        #     wait = WebDriverWait(self.driver, 15)
        #
        #     type = wait.until(EC.element_to_be_clickable(self.engine_type))
        #
        #     self.driver.execute_script(
        #         "arguments[0].scrollIntoView({block:'center'});", type
        #     )
        #     time.sleep(0.2)
        #
        #     type.click()
        #     time.sleep(0.2)
        #
        #     active = driver.switch_to.active_element
        #     active.send_keys(Keys.ARROW_DOWN)
        #     time.sleep(0.2)
        #     active.send_keys(Keys.ENTER)
        #     time.sleep(0.2)
        #
        #     print("Engine type entered successfully....!!")
        # except Exception as e:
        #     print(f"Error on click:{e}")


    def Enter_Description_Mileage(self):

        try:
                des = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.enter_description_mileage))
                time.sleep(.2)
                des.send_keys("Only for testing")
                time.sleep(.2)
                print("Enter Description successfully....!!")
        except Exception as e:
                print(f"Error on click:{e}")


    def Mileage(self):
        try:
            select = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.mileage))
            time.sleep(.2)
            select.send_keys("5")
            time.sleep(.2)
            print("Enter mileage successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Select_Rate(self):
        try:
            wait = WebDriverWait(self.driver, 15)

            select_rate = wait.until(EC.element_to_be_clickable(self.rate))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", select_rate
            )
            time.sleep(0.2)

            select_rate.click()
            time.sleep(0.2)

            select_rate.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            select_rate.send_keys(Keys.BACK_SPACE)
            time.sleep(0.5)

            select_rate.send_keys("100")
            time.sleep(0.2)

            print("Engine type entered successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Save_Mileage(self):
        try:
            save_mil = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.save_mileages))
            time.sleep(.2)
            save_mil.click()
            time.sleep(.2)

            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(normalize-space(), 'Mileage saved successfully with number')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Mileage saved successfully"

            print("Test Case  - Pass: Mileage saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)















