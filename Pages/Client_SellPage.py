from faker import Faker
import time
from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from datetime import datetime, timedelta
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

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


        self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

#---------------------------------------------invoice-------------- ----------------------------------------------------

        self.invoice = (By.XPATH, "(//span[contains(text(),'Invoice')])[1]")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.table = (By.XPATH," (//div[contains(text(),'Tables')])[1]")

        self.save_invoice = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")

        self.allocate_save_button = (By.XPATH,"//div[@role='dialog']//button[.//span[normalize-space()='Save']]")










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
            time.sleep(.2)



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




    def Select_Customer_Keyboard(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        control = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-control')][1]"
        )))
        control.click()

        input_el = wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-input-container')][1]//input"
        )))
        ActionChains(driver).move_to_element(input_el).click(input_el).perform()

        # ensure menu open
        wait.until(EC.visibility_of_element_located((
            By.XPATH, "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-menu')][1]"
        )))

        try:
            input_el.send_keys(Keys.ARROW_DOWN)
            time.sleep(.2)
            input_el.send_keys(Keys.ARROW_DOWN)
            time.sleep(.2)
            input_el.send_keys(Keys.ENTER)
        except ElementNotInteractableException:
            # fallback click first option if keyboard fails
            first_option = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-menu')][1]"
                "//div[contains(@class,'rs-option')][1]"
            )))
            first_option.click()

        selected = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//label[normalize-space()='Customer']/following::div[contains(@class,'rs-single-value')][1]"
        ))).text.strip()
        print("Customer selected successfully....!!")

        print("Selected Customer is :", selected)
        return selected





    # def Select_Customer(self):
    #         driver = self.driver
    #         wait = WebDriverWait(self.driver, 30)
    #
    #     #try:
    #
    #         control = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//div[contains(@class,'rs-control') and .//*[contains(text(),'Contact name')]]")
    #         ))
    #         control.click()
    #
    #         input_el = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//div[contains(@class,'rs-input-container')]//input")
    #         ))
    #
    #         input_el.send_keys(Keys.ARROW_DOWN)
    #         time.sleep(0.3)
    #         input_el.send_keys(Keys.ENTER)
    #         time.sleep(1)
    #         print("Customer selected successfully....!!")
    #     # except Exception as e:
    #     #     print(f"Error on Click : {e}")







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
            EC.element_to_be_clickable(self.save_invoice)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(0.4)
            save_button.click()
            time.sleep(0.4)
            print("Invoice created successfully")

            update_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(), 'Invoice created successfully')]"))
                )

            # Assert the presence of the success message
            assert update_message, "Invoice created successfully"

            print("Test Case  - Pass: Invoice created successfully")


            time.sleep(2)



    # def Save_Invoice(self):
    #     d = self.driver
    #     w = WebDriverWait(d, 20)
    #
    #     save_btn = w.until(
    #         EC.element_to_be_clickable(self.allocate_save_button)
    #     )
    #
    #     for attempt in range(2):
    #         try:
    #             save_btn.click()
    #             break
    #         except (ElementClickInterceptedException, StaleElementReferenceException):
    #             time.sleep(0.3)
    #             save_btn = w.until(
    #                 EC.element_to_be_clickable(self.allocate_save_button)
    #             )
    #
    #     time.sleep(0.2)
    #
    #     try:
    #         update_message = WebDriverWait(d, 10).until(
    #             EC.visibility_of_element_located(
    #                 (By.XPATH, "//*[contains(text(),'Invoice created successfully')]")
    #             )
    #         )
    #     except TimeoutException:
    #         raise AssertionError(
    #             "Expected 'Invoice created successfully' toast but did not see it."
    #         )
    #
    #     assert update_message.is_displayed(), "Invoice created successfully"
    #     print("Test Case -4 :  Pass: Invoice created successfully.")





























