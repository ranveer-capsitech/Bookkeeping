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


class Add_Supplier:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH, "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH,"//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")


        # self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")


#---------------------------------------------invoice-------------- ----------------------------------------------------

        self.click_suppliers = (By.XPATH, "//button[@role='tab'][.//span[normalize-space()='Suppliers']]")
        self.add_suppliers_button = (By.XPATH, "//span[normalize-space()='Supplier']")
        self.enter_supplier_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")

        self.click_billing_field = (By.XPATH,
                                    "//label[normalize-space()='Billing address']/following::label[normalize-space()='Building, Street, City'][1]")

        self.enter_building_no = (By.XPATH, "//input[@placeholder='Building']")
        self.enter_street = (By.XPATH, "//input[@placeholder='Street']")
        self.enter_city = (By.XPATH, "//input[@placeholder='City']")
        # self.county_details = (By.XPATH,
        #                        "//label[normalize-space()='Billing address']/following::label[normalize-space()='County, Country, Postcode'][1]")
        self.enter_county = (By.XPATH, "//input[@placeholder='County']")
        self.select_country = (By.XPATH,
                               "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]")

        self.postcode = (By.XPATH, "//input[@placeholder='Postcode' and @type='text']")

        self.click_contact_person = (By.XPATH,
                                     "//label[normalize-space()='Contact person']/following::input[@type='text'][1]")

        self.first_name = (By.XPATH,
                           "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")

        self.name = (By.XPATH,
                     "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")

        self.contact_number = (By.XPATH, "//i[@data-icon-name='Mobile']/following::input[1]")

        self.enter_mail = (By.XPATH, "//i[@data-icon-name='Envelope']/following::input[1]")

        self.select_bank = (By.XPATH,
                            "//label[normalize-space()='Bank']/following::input[contains(@id,'react-select')][1]")

        self.discount = (By.XPATH, "//label[normalize-space()='Discount']/following::input[@type='text'][1]")

        self.vat = (By.XPATH,
                    "//label[normalize-space()='VAT number']/following::input[contains(@id,'react-select') and contains(@id,'-input')][1]")

        self.enter_vat = (By.XPATH,
                          "//label[normalize-space()='VAT number']/following::input[contains(@class,'ms-TextField-field')][1]")

        self.enter_eori = (By.XPATH,
                           "//label[normalize-space()='EORI number']/following::input[contains(@class,'ms-TextField-field')][1]")

        self.project_tag = (By.XPATH,
                            "//label[normalize-space()='Project tags']/following::div[contains(@class,'rs-control')]//input[@role='combobox'][1]")

        self.attachment = (By.XPATH, "//i[@data-icon-name='Attachment' and @aria-label='Attachment']")

        self.save_customer = (By.XPATH, "//button[@type='submit']//span[normalize-space()='Save']")



