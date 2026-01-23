
from faker import Faker
import platform, time
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

CTRL = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL


class Items:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

# -------------------------------------------------Customers---------------------------------------------------------------
        self.loc_dialog = (By.XPATH, "//div[@role='dialog' or @role='alertdialog']")

        self.search = (By.XPATH,
                       "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH, "//a[@title='1ST LIMITED' and contains(@href,'/books/clients/')]")

        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

        self.item  =  (By.XPATH, "//div[@role='tablist']//button[@role='tab' and @name='Items']")
        self.add_item  =  (By.XPATH, "//button[.//span[normalize-space()='Item' and starts-with(@id,'id__')]]")
        self.enter_name  = (By.XPATH, "//label[normalize-space(text())='Name']/following::input[@type='text'][1]")
        self.unit_price_pur = (By.XPATH, "//td[normalize-space(text())='Unit price']/following::input[@type='text'][1]")
        self.unit_price_sell = (By.XPATH, "//td[normalize-space(text())='Unit price']/following::input[@type='text'][2]")
        self.purchases_description  =  (By.XPATH, "//label[normalize-space(text())='Description']/following::input[@type='text'][1]")
        self.sales_description  =  (By.XPATH, "//label[normalize-space(text())='Description']/following::input[@type='text'][2]")
        self.create = (By.XPATH, "//span[contains(text(),'Create')]")



#-------------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------


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

    def Item(self):
        try:
            click_item = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.item))
            time.sleep(.2)
            click_item.click()
            time.sleep(.2)
            print("click on item successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Add_Item(self):
        try:
            click_add_item = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.add_item))
            time.sleep(.2)
            click_add_item.click()
            time.sleep(.2)
            print("Click on add item icon successfully.....!!")
        except Exception as e:
            print(f"Error on Click:{e}")



    def Enter_Name(self):
        try:
            enter_name = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.enter_name))
            time.sleep(.2)
            enter_name.clear()
            time.sleep(0.2)
            # enter_name.send_keys("Only for testing")
            enter_name.send_keys(random_first_name)
            print(f" Entered Name: {random_first_name}")
            print("Enter name successfully.....!!")
            time.sleep(2)
        except Exception as e:
            print(f" Error on entering name: {e}")

    def Enter_Unit_Price_Pur(self):
        try:
            enter_pur = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.unit_price_pur))
            time.sleep(0.2)

            enter_pur.send_keys(Keys.CONTROL, "a")  # Select all
            time.sleep(0.2)
            enter_pur.send_keys(Keys.DELETE)  # Delete selected text
            time.sleep(0.2)

            time.sleep(0.2)

            enter_pur.send_keys("100")
            time.sleep(0.2)


            print("Enter Unit Price Successfully......!!")

        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Unit_Price_Sell(self):
        try:
            enter_pur = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.unit_price_sell))
            time.sleep(2)
            enter_pur.send_keys(Keys.CONTROL, "a")  # Select all
            time.sleep(0.2)
            enter_pur.send_keys(Keys.DELETE)  # Delete selected text

            time.sleep(.2)

            enter_pur.send_keys("100")
            time.sleep(.2)
            print("Enter Unit Price Sell Successfully.....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Purchases_Description(self):
        try:
            enter_description = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.purchases_description))
            time.sleep(.2)
            enter_description.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter purchases description successfully.....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Sales_Description(self):
        try:
            enter_description_for_sale = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.sales_description))
            time.sleep(.2)
            enter_description_for_sale.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter sale description successfully.....!!")

        except Exception as e:
            print(f"Error on click:{e}")

    def Create(self):
       # try:
            create_item = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(self.create))
            time.sleep(.2)
            create_item.click()
            time.sleep(.2)

            update_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Item created successfully')]"))
            )

            # Assert the presence of the success message
            assert update_message, "Items created successfully"

            print("Test Case -6 :  Pass: Items created successfully.")

        # except Exception as e:
        #     print(f"Error: {e}")
        #
        #     time.sleep(2)



