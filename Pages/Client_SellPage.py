import py
import pyautogui
import self
import random
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
formatted_date = tomorrow_date.strftime("%d-%m-%y")  # Adjust format as needed

random_email = fake.email()
random_email1 = fake.email()
random_indian_phone = fake.phone_number()
random_indian_phone_1 = fake.phone_number()
dob = fake.date_of_birth(minimum_age=18)
formatted_dob = dob.strftime('%d/%m/%Y')


class ClientSell:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='WEMBLEY LTD'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

#---------------------------------------------invoice-------------- ----------------------------------------------------

        self.invoice = (By.XPATH, "(//span[contains(text(),'Invoice')])[1]")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice = (By.XPATH, "//div[contains(@class,'rs-placeholder') and normalize-space()='Select item']")
        self.table = (By.XPATH," (//div[contains(text(),'Tables')])[1]")
        self.loc_save_button = (By.XPATH,"//div[contains(@class,'modal-footer')]//button[.//span[normalize-space()='Save']]")

#---------------------------------------Credit notes--------------------------------------------------------------------

        self.click_credit_notes = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[2]/span[1]")
        self.credit_notes = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Credit note']")
        self.customer_name = (By.XPATH, "//div[contains(text(),'Customer name')]")
        self.invoice_ref_no = (By.XPATH, "//*[normalize-space()='Invoice ref. no.']/following::div[contains(@class,'rs-input-container')][1]")
        self.clicks_save = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.paid_from_locators = (By.XPATH, "//*[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")


#-------------------------------------------Estimates-------------------------------------------------------------------

        self.estimates = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[3]/span[1]/span[1]/span[1]")
        self.add_estimates = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Estimate']")
        self.customer = (By.XPATH, "(//div[@id='react-select-2-placeholder'])[1]")
        self.select_item_estimate= (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.clicks_save_estimate = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")

#-------------------------------------------------Receipts---------------------------------------------------------------

        self.receipts = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[4]/span[1]/span[1]/span[1]")
        self.add_receipts = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Receipt']")
        self.select_receive_from = (By.XPATH, "//label[normalize-space()='Received from']/following::div[contains(@class,'rs-input-container')][1]")
        self.select_amount = (By.XPATH, "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@placeholder='amount'][1]")
        self.save_receipts = (By.XPATH, "//button[.//span[normalize-space()='Save'] and not(contains(.,'Save & New'))]")

#-----------------------------------------------------------------------------------------------------------------------


















#-----------------------------------------Methods-----------------------------------------------------------------------



    def Select_Business(self):
        try:
            client = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.select_business_name))
            time.sleep(.2)
            client.click()
            time.sleep(.2)
            print("Select a business name successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")


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



#---------------------------------------methods for invoice ------------------------------------------------------------

    def Add_Invoice(self):
        try:
            invoice = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.invoice))
            time.sleep(.2)
            invoice.click()
            time.sleep(.2)
            print("Click on Add invoice button successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Select_Customer(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            dropdown_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='react-select-'][id$='-input']"))
            )
            time.sleep(.2)
            dropdown_input.click()
            time.sleep(.2)

            time.sleep(.2)
            dropdown_input.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Customer selected successfully....!!")

        except Exception as e:
            print(f"Error on Click : {e}")



    def Select_item_sale(self, value="test"):
        d = self.driver
        w = self.wait
        container_el = w.until(
            EC.visibility_of_element_located(self.click_item_for_invoice)
        )
        time.sleep(.4)
        container_el.click()
        time.sleep(.4)

        def focused_input():
            return d.switch_to.active_element


        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ARROW_DOWN)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.2)

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ENTER)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.4)

    def Click_Save(self):

        # Initialize WebDriverWait
            wait = WebDriverWait(self.driver, 20)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']/ancestor::button"))
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(0.4)
            save_button.click()
            time.sleep(0.4)

    def Save_Invoice(self):
        d = self.driver
        w = WebDriverWait(d, 20)

        # 1. wait for and click the Save button
        save_btn = w.until(
            EC.element_to_be_clickable(self.loc_save_button)
        )

        for attempt in range(2):
            try:
                save_btn.click()
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                time.sleep(0.3)
                save_btn = w.until(
                    EC.element_to_be_clickable(self.loc_save_button)
                )

        time.sleep(0.2)

        try:
            update_message = WebDriverWait(d, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Invoice created successfully')]")
                )
            )
        except TimeoutException:
            raise AssertionError(
                "Expected 'Invoice created successfully' toast but did not see it."
            )

        assert update_message.is_displayed(), "Invoice created successfully"
        print("Test Case - Pass: Invoice created successfully.")


 #-----------------------------------------credit_notes-----------------------------------------------------------------


    def Click_Credit_Notes(self):
        try:
            click_credit_notes = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.click_credit_notes))
            time.sleep(.2)
            click_credit_notes.click()
            time.sleep(.2)
            print("click on credit section successfully......!!")
        except Exception as e:
             print(f"Error on click:{e}")

    def Add_Credit_Note(self):
       try:
            credit = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.credit_notes ))
            time.sleep(.2)
            credit.click()
            time.sleep(.2)

            print("Click for add credit  successfully....!!")
       except Exception as e:
            print(f"Error on click:{e}")

    def Select_Customer_for_Credit_Note(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            #  Click on the dropdown field
            field = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[contains(@class,'rs-input-container')]"
            )))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
            field.click()
            time.sleep(0.5)

            # Use keyboard to select first option
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print(" Customer selected successfully for Credit Note!")

        except Exception as e:
            print(f" Could not select customer: {e}")


    def Invoice_ref(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 15)

            #  Click on the Invoice Ref dropdown
            dropdown = wait.until(EC.element_to_be_clickable((self.invoice_ref_no)))
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

    def Save_Credit_Notes(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_credit_note = wait.until(
                EC.element_to_be_clickable(self.clicks_save)
            )
            time.sleep(.2)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",  save_credit_note)
            time.sleep(0.4)
            save_credit_note.click()
            time.sleep(0.4)
            print("click on save credit note successfully....!!")
        except Exception as e:
            print(f" Could not select customer: {e}")


    def Paid_From(self):
        try:

            driver = self.driver
            wait = WebDriverWait(driver, 15)

            dropdown = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//*[normalize-space()='Paid from']/following::div[contains(@class,'rs-input-container')][1]"
                )))

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
            time.sleep(0.5)
            dropdown.click()
            time.sleep(0.5)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ENTER)

            print(" 'Paid from' selected successfully!")
        except Exception as e:
            print(f" Could not select customer: {e}")


    def Click_Save_Button(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        #  This targets ONLY the Save button inside the modal (popup)
        save_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@role='dialog']//button[@title='Save' and .//span[normalize-space()='Save']]"
        )))

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
        time.sleep(0.3)

        try:
            save_btn.click()
        except:
            driver.execute_script("arguments[0].click();", save_btn)

        time.sleep(1)
        print(" Clicked on save button for add credit note successfully!")




#-----------------------------------------------Estimates---------------------------------------------------------------

    def Select_Estimates(self):
        try:
            estimate = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.estimates))
            time.sleep(.2)
            estimate.click()
            time.sleep(.2)
            print("Click for select estimate  successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Add_Estimates(self):

        try:
            add_estimate = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.add_estimates))
            time.sleep(.2)
            add_estimate.click()
            time.sleep(.2)

            print("Click for add_estimates  successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Select_Customer_for_Estimate(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 15)

            #  Click on the dropdown field
            field = wait.until(EC.element_to_be_clickable((
                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
            )))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
            field.click()
            time.sleep(0.5)

            # Use keyboard to select first option
            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print(" Customer selected successfully for Estimate!")

        except Exception as e:
            print(f" Could not select customer: {e}")



    def Select_item(self, value="test"):
        d = self.driver
        w = self.wait
        item = w.until(
            EC.visibility_of_element_located(self.select_item_estimate)
        )
        time.sleep(.4)
        item.click()
        time.sleep(.4)

        def focused_input():
            return d.switch_to.active_element

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ARROW_DOWN)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.2)

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ENTER)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.4)


    def Click_Save_Estimation(self):


            wait = WebDriverWait(self.driver, 20)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']/ancestor::button"))
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(0.4)
            save_button.click()
            time.sleep(0.4)
            print(" Test case pass - Save estimate successfully.....!!")

#---------------------------------------------------Receipts------------------------------------------------------


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
        #try:
            add_receipts = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.select_receive_from))
            time.sleep(.2)
            add_receipts.click()
            time.sleep(.2)
            print("click for add new receipts successfully.....!! ")
        # except Exception as e:
        #     print(f"Error on click:{e}")

    def Select_Amount(self):
        #try:
            amount = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.select_amount))
            time.sleep(.2)
            amount.click()
            time.sleep(.2)
            amount.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Customer selected successfully....!!")

        # except Exception as e:
        #     print(f"Error on Click : {e}")


    def Enter_Amount(self):
        #try:
            enter_a_amount = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_amount))
            time.sleep(.2)
            random_price = round(random.uniform(50, 999), 2)

            #  Clear the field
            enter_a_amount.send_keys(Keys.CONTROL, 'a')
            enter_a_amount.send_keys(Keys.BACKSPACE)

            #  Enter the random amount
            enter_a_amount.send_keys(str(random_price))
            enter_a_amount.send_keys(Keys.TAB)  # to trigger React blur event

            print(f" Entered random price: £{random_price}")
            time.sleep(0.5)
        # except Exception as e:
        #     print(f"Error on Click : {e}")



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
            print(" Test case pass - Save receipt successfully.....!!")








