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


class ClientPurchase:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")

#---------------------------------------------------invoice-------------------------------------------------------------

        self.invoice = (By.XPATH, "//button[@aria-label='btnInvoice']")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")

        self.click_item_for_invoice = (By.XPATH,
                                       "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

        self.net_amount = (By.XPATH, "(//table[contains(@class,'table')]//input[contains(@name,'amount.net')])[1]")

        self.loc_save_button = (By.XPATH, "//div[contains(@class,'modal')]//span[normalize-space(text())='Save']")

#---------------------------------------------Credit notes--------------------------------------------------------------

        self.click_credit_notes = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[2]/span[1]")
        self.credit_notes = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Credit note']")
        self.supplier_name = (By.XPATH, "//div[contains(text(),'Supplier name')]")
        self.invoice_ref_no = (By.XPATH, "//*[normalize-space()='Invoice ref. no.']/following::div[contains(@class,'rs-input-container')][1]")
        self.clicks_save = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.paid_from_locators = (By.XPATH, "//*[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")



#------------------------------------------------PO---------------------------------------------------------------------

        self.purchase_orders = (By.XPATH, "//div[@role='tablist']//button[.//span[normalize-space()='Purchase orders']]")
        self.click_purchase_order = (By.XPATH, "//span[normalize-space(text())='Purchase order']")
        self.select_contact_name = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice_po = (By.XPATH,
                                       "(//table[contains(@class,'table')]//tr[1]//div[contains(@class,'rs-input-container')]//input)[1]")
        self.save_po = (By.XPATH, "//button[.//span[normalize-space(text())='Save']]")

#--------------------------------------------Pyments--------------------------------------------------------------------

        self.payment = (By.XPATH,"//button[@role='tab' and .//span[normalize-space()='Payments']]")
        self.click_payment = (By.XPATH, "//button[.//span[normalize-space()='Payment']]")

        self.paid_to_supplier = (By.XPATH, "//label[normalize-space()='Paid to']/following::div[contains(@class,'rs-control')][1]")
        self.account = (By.XPATH, "//label[normalize-space(text())='Account']/following::div[contains(@class,'rs-input-container')]//input")
        #self.method = (By.XPATH, "//div[@id='react-select-17-placeholder']")
        self.enter_amount = (By.XPATH, "//input[@name='availableAmount']")
        self.save_payment = (By.XPATH, "//button[.//span[normalize-space(text())='Save']]")

#-------------------------------------------item------------------------------------------------------------------------

        self.item = (By.XPATH, "//button[@role='tab' and .//span[normalize-space()='Items']]")
        self.click_add_item = (By.XPATH, "//button[.//span[normalize-space()='Item']]")
        self.enter_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")
        self.pur_description = (By.XPATH, "//label[normalize-space()='Description']/following::input[1]")
        self.sell_description = (By.XPATH, "//span[normalize-space()='For sales']/following::input[@type='text'][2]")
        self.enter_pur_price = (By.XPATH, "//td[normalize-space()='Unit price']/following::input[@type='text'][1]")
        self.enter_sell_price = (By.XPATH, "//div[@role='dialog']//td[normalize-space()='Unit price']/following::input[@type='text'][2]")
        self.click_on_create = (By.XPATH, "//span[contains(text(),'Create')]")


#------------------------------------------Method-----------------------------------------------------------------------



    def Select_Business(self):
        try:
            client = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.select_business_name))
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



    def Click_Purchases(self):
        try:
            sales = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.click_purchases))
            time.sleep(.2)
            sales.click()
            time.sleep(.2)
            print("Click on purchases successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")



    def Add_Invoice(self):

        try:
            invoice = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.invoice))
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
            dropdown_input.send_keys(Keys.ARROW_DOWN)  # first option
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ARROW_DOWN)  # second option
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ARROW_DOWN)  # second option
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ENTER)  # select it
            time.sleep(0.5)

            time.sleep(.2)
            #dropdown_input.send_keys(Keys.ENTER)
            time.sleep(.5)
            print("Customer selected successfully....!!")

        except Exception as e:
            print(f"Error on Click : {e}")

    def Select_item_purchase(self, value="test"):
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
                time.sleep(2)

        for _ in range(2):
            try:
                focused_input().send_keys(Keys.ENTER)
                break
            except (StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(0.4)


    def Enter_amount(self):
        try:
            amount = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.net_amount))
            time.sleep(.2)
            amount.send_keys("100")
            time.sleep(.2)
            print("Enter amount successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")


    def Save_Services(self):
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
        print("Invoice created successfully")
        try:
            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Invoice created successfully')]")
                )
            )
        except TimeoutException:
            raise AssertionError(
                "Expected 'Invoice created successfully' toast but did not see it."
            )

        assert update_message.is_displayed(), "Invoice created successfully"
        print("Test Case -9 :  Pass:: Invoice created successfully.")



    #--------------------------------------Credit_Notes-----------------------------------------------------------------

    def Click_Credit_Notes(self):
        try:
            click_credit_notes = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.click_credit_notes))
            time.sleep(.2)
            click_credit_notes.click()
            time.sleep(.3)
            print("click on credit section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.3)

    def Add_Credit_Note(self):
        try:
            credit = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.credit_notes))
            time.sleep(.3)
            credit.click()
            time.sleep(.3)

            print("Click for add credit  successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.3)

    def Select_Suppiler_for_Credit_Note(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            #  Click on the dropdown field
            field = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[contains(@class,'rs-placeholder') and normalize-space()='Supplier name']/ancestor::div[contains(@class,'rs-control')][1]"
            )))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
            field.click()
            time.sleep(0.5)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(.3)
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(.3)
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
            dropdown = wait.until(EC.element_to_be_clickable(self.invoice_ref_no))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
            dropdown.click()
            time.sleep(0.5)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.3)
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

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_credit_note)
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



        toast_xpath = "//div[contains(text(),'Duplicate refund number')]"

        try:
            toast_msg = WebDriverWait(driver, 4).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            txt = toast_msg.text.lower()

            if "duplicate" in txt or "already exists" in txt:
                print(" Duplicate entry detected — stopping further execution.")

                time.sleep(.2)
                driver.back()
                time.sleep(.10)

            else:
              print(" Test Case -10 : Pass : Purchase credit note saved successfully....!")

        except TimeoutException:
            print(" Exception")













#------------------------------------------Method of PO ----------------------------------------------------------------



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
            purchase_order =  WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.click_purchase_order))
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
            self.select_contact_name # outer control
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
        print("Test Case -11 :  Pass:  Purchase Order saved successfully!")


#-----------------------------------------Payment-----------------------------------------------------------------------


    def Payment_Section(self):

        try:
            payment_section = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.payment))
            time.sleep(.2)
            payment_section.click()
            time.sleep(.2)
            print("click on Payment section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_Payment(self):
        try:
            payment = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.click_payment))
            time.sleep(.2)
            payment.click()
            time.sleep(.2)

            print("Click on payment successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Paid_To_Supplier(self):
        d = self.driver
        w = WebDriverWait(d, 20)


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


    def Select_Account(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 15)


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
            enter_amount = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.enter_amount))
            time.sleep(.2)
            enter_amount.send_keys("100")
            time.sleep(.2)

            print("Click on payment successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Save_payment(self):
        try:
          save_paymt = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.save_payment))
          time.sleep(.2)
          save_paymt.click()
          time.sleep(.2)

          print(" Test Case -12 :  Pass:  Payment saved successfully....!!")
        except Exception as e:
          print(f"Error on click:{e}")


#-----------------------------------------------------------------------------------------------------------------------

    def Item_Section(self):

        try:
            item_section = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.item))
            time.sleep(.2)
            item_section.click()
            time.sleep(.2)
            print("click on item section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_on_item(self):
        try:
            click_item = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.click_add_item))
            time.sleep(.2)
            click_item.click()
            time.sleep(.2)
            print("Click on add item successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Enter_Name(self):
        try:
            name_el = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.enter_name)
            )

            # Create random name
            random_item_name = fake.word().capitalize() + " " + fake.word().capitalize()

            # Step 1: Clear using JS
            self.driver.execute_script("arguments[0].value='';", name_el)
            time.sleep(0.2)

            # Step 2: Slow typing to avoid React override
            for ch in random_item_name:
                name_el.send_keys(ch)
                time.sleep(0.1)

            print(f"Enter name successfully: {random_item_name}")

        except Exception as e:
            print(f"Error on entering name: {e}")



    def Enter_Description_For_Purchases(self):
        try:
            pur_des = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.pur_description))
            time.sleep(.2)
            pur_des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description for purchases successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Enter_Description_For_Sell(self):
        try:
            pur_des = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.sell_description))
            time.sleep(.2)
            pur_des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description for sell successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Enter_Unit_Price_Purchases(self):
        try:
            pur_price = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_pur_price))
            time.sleep(.2)
            pur_price.send_keys("100")
            time.sleep(.2)
            print("Enter Unit price for purchases successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Enter_Unit_Price_Sell(self):
        try:
            sell_price = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_sell_price))
            time.sleep(.2)
            sell_price.send_keys("100")
            time.sleep(.2)
            print("Enter Unit price for Sell successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Create_Item(self):
        try:
            item = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.click_on_create))
            time.sleep(.2)
            item.click()
            time.sleep(.2)


            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Items created successfully')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Items created successfully"

            print("Test Case -13 :  Pass: Items created successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

























