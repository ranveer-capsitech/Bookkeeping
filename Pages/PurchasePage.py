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


class ClientPurchase:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")

#-----------------------------------------------------------------------------------------------------------------------

        self.invoice = (By.XPATH, "//button[@aria-label='btnInvoice']")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")

        self.click_item_for_invoice = (By.XPATH,
                                       "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

        #self.product_description = (By.XPATH,"//table[contains(@class, 'table')]//input[@name='productItems.0.description']")
        self.net_amount = (By.XPATH, "(//table[contains(@class,'table')]//input[contains(@name,'amount.net')])[1]")
        #self.purchase_save = (By.XPATH, "//span[normalize-space(text())='Save' and not(contains(text(),'&'))]")
        self.loc_save_button = (By.XPATH, "//div[contains(@class,'modal')]//span[normalize-space(text())='Save']")


    #--------------------------------------Method---------------------------------------------------------------------------



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
        print("Test Case - Pass: Invoice created successfully.")




