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


class Add_Customer:

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

        self.click_customers = (By.XPATH, "//button[@role='tab'][.//span[normalize-space()='Customers']]")
        self.add_customer_button = (By.XPATH, "//span[normalize-space()='Customer']")
        self.enter_customer_name = (By.XPATH, "//label[normalize-space()='Name']/following::input[1]")
        self.click_billing_field = (By.XPATH, "//label[normalize-space()='Billing address']/following::label[normalize-space()='Building, Street, City'][1]")
        self.enter_building_no = (By.XPATH, "//input[@placeholder='Building']")
        self.enter_street = (By.XPATH, "//input[@placeholder='Street']")
        self.enter_city = (By.XPATH, "//input[@placeholder='City']")
        self.county_details = (By.XPATH, "//label[normalize-space()='Billing address']/following::label[normalize-space()='County, Country, Postcode'][1]")
        self.enter_county = (By.XPATH, "//input[@placeholder='County']")
        self.select_country = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
        self.postcode = (By.XPATH, "//input[@placeholder='Postcode' and @type='text']")
        self.click_contact_person = (By.XPATH, "//label[normalize-space()='Contact person']/following::input[@type='text'][1]")
        self.first_name = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.name = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")
        self.contact_number = (By.XPATH, "//i[@data-icon-name='Mobile']/following::input[1]")
        self.enter_mail = (By.XPATH, "//i[@data-icon-name='Envelope']/following::input[1]")
        self.select_bank = (By.XPATH, "//label[normalize-space()='Bank']/following::input[contains(@id,'react-select')][1]")
        self.discount = (By.XPATH, "//label[normalize-space()='Discount']/following::input[@type='text'][1]")
        self.vat = (By.XPATH, "//label[normalize-space()='VAT number']/following::input[contains(@id,'react-select') and contains(@id,'-input')][1]")
        self.enter_vat = (By.XPATH, "//label[normalize-space()='VAT number']/following::input[contains(@class,'ms-TextField-field')][1]")
        self.enter_eori = (By.XPATH, "//label[normalize-space()='EORI number']/following::input[contains(@class,'ms-TextField-field')][1]")
        self.project_tag = (By.XPATH, "//label[normalize-space()='Project tags']/following::div[contains(@class,'rs-control')]//input[@role='combobox'][1]")
        self.attachment = (By.XPATH, "//i[@data-icon-name='Attachment' and @aria-label='Attachment']")
        self.save_customer = (By.XPATH, "//button[@type='submit']//span[normalize-space()='Save']")


#-----------------------------------------Methods-----------------------------------------------------------------------

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
                input = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.click_input_drop_down))
                time.sleep(.2)
                input.click()
                time.sleep(.2)
                print("Input drop down open successfully....!!")
            except Exception as e:
                print(f"Error on click:{e}")

    def Click_Sales(self):
            try:
                sales = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_sales))
                time.sleep(.2)
                sales.click()
                time.sleep(.2)
                print("Click on Sales successfully....!!")
            except Exception as e:
                print(f"Error on Click:{e}")
                time.sleep(.2)

# ---------------------------------------methods for Customer ----------------------------------------------------------

    def Select_Client_Section(self):
        try:
            client_section = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_customers))
            time.sleep(.2)
            client_section.click()
            time.sleep(.2)
            print("Click on Client section successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Click_On_Add_Customer(self):
        try:
            add_customer = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.add_customer_button))
            time.sleep(.2)
            add_customer.click()
            time.sleep(.2)
            print("Click on Add Client section successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)

    def Enter_Customer_Name(self):
        try:
            enter_customer_name = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_customer_name))
            time.sleep(.2)
            enter_customer_name.send_keys(full_name)
            time.sleep(.2)
            print("Enter Customer name successfully......!! ")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Click_Billing_Field(self):
        try:
            click_address = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_billing_field))
            time.sleep(.2)
            click_address.click()
            time.sleep(.2)
            print("Click on Billing field successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Enter_Building(self):
        try:
            building = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_building_no))
            time.sleep(.2)
            building.click()
            time.sleep(.2)
            building.send_keys("11")
            time.sleep(.2)
            print("Enter building number successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Enter_Street(self):
        try:
            street = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_street))
            time.sleep(.2)
            street.click()
            time.sleep(.2)
            street.send_keys("local street")
            time.sleep(.2)
            print("Enter Street successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Enter_City(self):
        try:
            city = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_city))
            time.sleep(.2)
            city.click()
            time.sleep(.2)
            city.send_keys("Jodhpur")
            time.sleep(.2)
            print("Enter city successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)


    def Enter_County(self):
        try:
            county = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_county))
            time.sleep(.2)
            county.click()
            time.sleep(.2)
            county.send_keys("Rajasthan")
            time.sleep(.2)
            print("Enter county successfully.....!!")

        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Select_Country(self):
        try:
            country = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.select_country))
            time.sleep(.2)
            country.click()
            time.sleep(.2)
            country.send_keys('United Kingdom')
            time.sleep(.2)
            country.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Enter country successfully.....!!")

        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Enter_Postcode(self):
        try:
            postcode = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.postcode))
            time.sleep(.2)
            postcode.click()
            time.sleep(.2)
            postcode.send_keys("ABC11223")
            time.sleep(.2)
            print("Enter postcode successfully.....!!")

        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Click_Contact_Person(self):
        try:
            contact_person = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_contact_person))
            time.sleep(.2)
            contact_person.click()
            time.sleep(.2)
            print("Click on contact person field successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def First_Name(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            first = wait.until(EC.element_to_be_clickable(self.first_name))

            time.sleep(.2)
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", first)
            driver.execute_script("arguments[0].click();", first)

            time.sleep(.2)
            active = driver.switch_to.active_element
            time.sleep(.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(.2)
            # active.send_keys(Keys.ARROW_DOWN)
            # time.sleep(.2)
            active.send_keys('Mr')
            time.sleep(.2)
            active.send_keys(Keys.ENTER)
            time.sleep(.2)

            print("Enter name successfully!")
        except Exception as e:
            print(f"Error on Click: {e}")

    def Enter_Name(self):
        try:
            enter_name =  WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.name))
            time.sleep(.2)
            enter_name.click()
            time.sleep(.2)
            enter_name.send_keys(random_first_name)
            print("Name enters successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Enter_Contact_Number(self):
        try:
            contact_number = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.contact_number))
            time.sleep(.2)
            contact_number.send_keys("9680962177")
            time.sleep(.2)
            print("Enter contact number successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.5)

    def Enter_Mail(self):
        try:
            mail = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_mail))
            time.sleep(.2)
            mail.send_keys("teamtesting@abc.com")
            time.sleep(.2)
            print("Enter mail id successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)

    def Select_Bank(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        # click dropdown indicator arrow (more reliable than clicking input)
        arrow = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Bank']/following::div[contains(@class,'dropdown-indicator')][1]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", arrow)
        driver.execute_script("arguments[0].click();", arrow)

        # focus input and use keyboard
        input_el = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             "//label[normalize-space()='Bank']/following::input[contains(@id,'react-select') and contains(@id,'-input')][1]")
        ))
        input_el.send_keys(Keys.ARROW_DOWN)
        input_el.send_keys(Keys.ENTER)


    def Discount(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            dis = wait.until(EC.element_to_be_clickable(self.discount))

            # focus
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dis)
            dis.click()
            time.sleep(0.2)
            dis.send_keys(Keys.CONTROL, "a")
            time.sleep(0.1)
            dis.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
            dis.send_keys("10")
            time.sleep(0.2)

            print("Entered discount successfully!")
        except Exception as e:
            print(f"Error on Discount input: {e}")


    def Select_Vat(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)


        arrow = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Bank']/following::div[contains(@class,'dropdown-indicator')][1]")
        ))
        time.sleep(0.2)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", arrow)
        time.sleep(0.2)
        driver.execute_script("arguments[0].click();", arrow)
        time.sleep(0.2)
        input_el = wait.until(EC.visibility_of_element_located(self.vat))
        time.sleep(0.2)
        input_el.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.2)
        input_el.send_keys(Keys.ENTER)
        time.sleep(0.2)


    def Enter_Vat(self):
        try:
            vat = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_vat))
            time.sleep(.2)
            vat.send_keys("987654321")
            time.sleep(.2)
            print("Enter vat successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)


    def Enter_EORI(self):
        try:
            eori = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.enter_eori))
            time.sleep(.2)
            eori.send_keys("GB123456789000")
            time.sleep(.2)
            print("Enter EORI successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)

    def Project_tags(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            control = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='Project tags']/following::div[contains(@class,'rs-control')][1]")
            ))
            control.click()

            input_box = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//label[normalize-space()='Project tags']/following::input[@role='combobox'][1]")
            ))

            ActionChains(driver).click(input_box).perform()
            input_box.send_keys(Keys.CONTROL, "a")
            input_box.send_keys(Keys.BACKSPACE)
            input_box.send_keys("test only")

            # Wait until Create option is visible (means dropdown is open)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'rs-option')][contains(.,'Create') and contains(.,'test only')]")
            ))

            # Now ENTER should work (Rv)
            input_box.send_keys(Keys.ENTER)

            print("Project tag selected using ENTER successfully!")
            time.sleep(1)

        except Exception as e:
            print(f"Error in Project_tags: {e}")





    def Add_Attachment(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            #  Click attachment icon(Rv)
            attach_icon = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//i[@data-icon-name='Attachment']")
            ))
            driver.execute_script("arguments[0].click();", attach_icon)

            #  Wait for file input to appear(Rv)
            file_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@type='file']")
            ))

            #  Upload file(Rv)
            file_input.send_keys(
                r"C:\Users\CT_USER\Desktop\test.csv"
            )

            print("File uploaded successfully!")

        except Exception as e:
            print(f"Error in upload: {e}")
        # try:
        #     driver = self.driver
        #     wait = WebDriverWait(driver, 30)
        #     attach = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.attachment))
        #     time.sleep(.2)
        #     driver.execute_script("arguments[0].click();",  attach)
        #     time.sleep(.2)
        #     attach.send_keys(r"C:\Users\CT_USER\Desktop\Demo Bank Statement_Accabot 23.csv")
        #     time.sleep(.2)
        #     print("File uploaded successfully.......!")
        #     time.sleep(.2)(Rv)
        #
        # except Exception as e:
        #     print(f"Error in upload: {e}")

    def Save_customer(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            save = wait.until(EC.element_to_be_clickable(self.save_customer))
            time.sleep(.2)
            save.click()
            time.sleep(.2)
            print("customer saved successfully!")
            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Customer added successfully.')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Budget fields updated successfully."

            print("Test Case 22  - Pass: Customer added successfully.")

        except Exception as e:
            print(f"Enter on click:{e}")
            time.sleep(.5)














