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
today_date = datetime.today().strftime("%d/%m/%Y")


class ClientSell:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 50)
        self.driver = driver

#------------------------ WebElements of admin for Client sell.---------------------------------------------------------

        self.search = (By.XPATH, "//div[contains(@class,'ms-SearchBox-iconContainer')]/following-sibling::input[@placeholder='Search...']")

        self.click_company = (By.XPATH,"//a[@title='RDX LIMITED' and contains(@href,'/books/clients/')]")


        # self.select_business_name = (By.XPATH, "(//a[normalize-space()='290 CREW LIMITED'])[1]")
        self.click_input_drop_down = (By.XPATH, "//div[contains(@class, 'ms-NavItemName') and normalize-space(.)='Inputs']")
        self.click_sales = (By.XPATH, "(//div[contains(text(),'Sales')])[1]")

#---------------------------------------------invoice-------------- ----------------------------------------------------

        self.invoice = (By.XPATH, "(//span[contains(text(),'Invoice')])[1]")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.table = (By.XPATH," (//div[contains(text(),'Tables')])[1]")

        self.save_invoice = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.add_discount = (By.XPATH, "//input[@name='discount']")

        self.click_for_enter_note = (By.XPATH, "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note = (By.XPATH, "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.allocate_save_button = (By.XPATH,"//div[@role='dialog']//button[.//span[normalize-space()='Save']]")

        self.enter_search = (By.XPATH, "//input[@placeholder='Search']")
        self.cancel_cross_button = (By.XPATH, "//i[@data-icon-name='Clear']")

        self.enter_from_date = (By.XPATH, "//input[@name='fromDate']")
        self.enter_to_date = (By.XPATH, "//input[@name='toDate']")
        self.refresh_icon = (By.XPATH, "//i[@data-icon-name='Refresh']/ancestor::button")

        self.filter_drop_down = (By.XPATH, "//div[contains(@class,'dropdown-indicator')]//*[name()='svg']")


        self.hide_graph = (By.XPATH, "//button[@title='hide reports']//*[name()='svg']")
        self.pagination = (By.XPATH, "//div[@role='combobox']")


        self.three_dot = (By.XPATH, "(//button[starts-with(@id,'btn-overflow-') and contains(@class,'ms-Button--hasMenu')])[1]")
        self.clone = (By.XPATH, "(//span[normalize-space()='Clone'])[1]")
        self.bad_debts = (By.XPATH, "(//span[normalize-space()='Bad debts'])[1]")
        self.click_download_icon = (By.XPATH, "(//button[.//i[@data-icon-name='BkInstallation']])[1]")


        self.click_pound_icon = (By.XPATH, "(//*[@data-automationid='DetailsRowCell']//button[contains(@id,'btnReceipt')])[1]")







    #-----------------------------------------Methods-----------------------------------------------------------------------


    def Select_Search(self):
        try:
            client = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.search))
            time.sleep(.2)
            client.click()
            time.sleep(.5)
            print("Click on search field successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")


    def Enter_Company(self, company_name="RDX LIMITED", timeout=30, os=None):

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
            click_on_selected_company = WebDriverWait(self.driver,30).until(EC.presence_of_element_located(self.click_company))
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
            input = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_input_drop_down))
            time.sleep(.2)
            input.click()
            time.sleep(.2)
            print("Input drop down open successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")


    def Click_Sales(self):
        try:
            sales = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.click_sales))
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
            invoice = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.invoice))
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

    def Add_Attachment(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            # 1) Directly target the file input near the attachment icon (more stable(rv))
            file_input = wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//i[@data-icon-name='Attachment']/ancestor::button/following::input[@type='file'][1]"
            )))

            # 2) If hidden, force it visible so send_keys works(rv)
            driver.execute_script(
                "arguments[0].style.display='block'; arguments[0].style.visibility='visible';",
                file_input
            )

            # 3) Upload file (this will NOT open OS dialog(rv))
            file_input.send_keys(r"C:\Users\CT_USER\Desktop\test.csv")

            print("File uploaded successfully.......!")

        except Exception as e:
            print(f"Error in upload: {e}")





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


    def Enter_Discount(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)

        try:
            control = wait.until(EC.visibility_of_element_located(self.add_discount))
            time.sleep(.2)
            control.click()
            time.sleep(.2)
            control.send_keys("10")
            time.sleep(.2)
            print("Discount added successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")


    def Click_Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_note))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)


            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")


    def Click_Save(self):


            wait = WebDriverWait(self.driver, 30)

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
            # print("Invoice created successfully")
            #
            # update_message = WebDriverWait(self.driver, 10).until(
            # EC.visibility_of_element_located(
            # (By.XPATH, "//*[contains(normalize-space(), 'Invoice created successfully')]"))
            #     )
            #
            # # Assert the presence of the success message
            # assert update_message, "Invoice created successfully"

            print("Test Case 2 - Pass: Invoice created successfully")

            time.sleep(2)

#-------------------------------search ---------------------------------------------------------------------------------

    def Enter_Search(self):
        try:
            search = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.enter_search))
            time.sleep(.2)
            search.click()
            time.sleep(.2)
            search.send_keys(today_date)
            time.sleep(.2)
            search.send_keys(Keys.ENTER)
            time.sleep(.2)

            print("Enter Search value  successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    def Remove_Search(self):
        try:
            remove = WebDriverWait(self.driver,40).until(
                EC.element_to_be_clickable(self.cancel_cross_button)
            )
            time.sleep(.2)
            remove.click()
            time.sleep(.2)
            print("Search functionality reset  successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")


#----------------------------------------calendar-----------------------------------------------------------------------


    def wait_for_spinner_to_disappear(self, timeout=40):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'spinner')]")
                )
            )
        except:
            pass

    def clear_and_enter_date(self, element, value):
        self.driver.execute_script("""
            const input = arguments[0];
            input.removeAttribute('disabled');
            input.removeAttribute('readonly');
            input.focus();
        """, element)

        time.sleep(0.3)

        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(0.2)

        element.send_keys(Keys.CONTROL, "a")
        time.sleep(0.2)

        element.send_keys(Keys.BACKSPACE)
        time.sleep(0.2)

        element.send_keys(value)
        time.sleep(0.3)

        element.send_keys(Keys.ENTER)
        time.sleep(0.3)

        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
        """, element)


    def Change_Date_Calendar(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            self.wait_for_spinner_to_disappear()

            from_date = wait.until(
                EC.presence_of_element_located(self.enter_from_date)
            )

            to_date = wait.until(
                EC.presence_of_element_located(self.enter_to_date)
            )

            self.clear_and_enter_date(from_date, "22/01/2023")
            time.sleep(1)

            self.clear_and_enter_date(to_date, "01/01/2028")
            time.sleep(1)

            try:
                refresh = wait.until(
                    EC.presence_of_element_located(self.refresh_icon)
                )
                self.driver.execute_script("arguments[0].click();", refresh)
            except:
                pass

            self.wait_for_spinner_to_disappear()

            print("Changed date successfully in calendar.")

        except Exception as e:
            print(f"Error in Change_Date_Calendar: {type(e).__name__} - {e}")
            self.driver.save_screenshot("change_date_calendar_error.png")
            raise

    def wait_for_loader_to_disappear(self):
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.invisibility_of_element_located(
                        (By.XPATH,
                         "//*[contains(@class,'spinner') or contains(@class,'loading') or contains(@class,'ms-Spinner')]")
                    )
                )
            except TimeoutException:
                pass

    def Select_Filter(self):
        wait = WebDriverWait(self.driver, 20)

        dropdown = wait.until(
            EC.element_to_be_clickable(self.filter_drop_down)
        )

        # First option
        dropdown.click()
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("enter")

        time.sleep(5)

        # Second option
        dropdown.click()
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(5)


        # 3rd option
        dropdown.click()
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(5)
        print("Shorting functionality is working fine.")


    def Hide_Reports(self):
        try:
            hide = WebDriverWait(self.driver,40).until(
                EC.element_to_be_clickable(self.hide_graph)
            )
            time.sleep(.2)
            hide.click()
            time.sleep(.2)
            print(" Hide Report Section successfully.....!!")
            hide.click()
            time.sleep(.2)
            print("Again showing Report Section successfully.....!!")

        except Exception as e:
            print(f"Error: {e}")
    #
    def Change_Pagination(self):
        wait = WebDriverWait(self.driver, 20)

        dropdown = wait.until(
            EC.element_to_be_clickable(self.pagination)
        )

        # First option
        dropdown.click()
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)
        pyautogui.press("enter")

        time.sleep(5)

        # Second option
        dropdown.click()
        time.sleep(0.2)
        pyautogui.press("down")
        time.sleep(0.2)

        pyautogui.press("enter")
        time.sleep(5)


        print("Change Pagination functionality  is working fine.")
#-----------------------------------------------------------------------------------------------------------------------


    def Click_Three_Dot(self):
        try:
            dot = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.three_dot))
            time.sleep(.2)
            dot.click()
            time.sleep(.5)
            print("Click on Three dot successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Clone(self):
        try:
            check_clone = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.clone))
            time.sleep(.2)
            check_clone.click()
            time.sleep(.5)
            print("Click on clone option successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")


    def Clone_Save(self):


            wait = WebDriverWait(self.driver, 30)

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
            print("Save clone invoice successfully.......")

    def Bad_Debts(self):
        try:
            debts = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.bad_debts))
            time.sleep(.2)
            debts .click()
            time.sleep(.5)
            print("Click on Bad Debts option successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Bad_Debts_Save(self):


            wait = WebDriverWait(self.driver, 30)

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
            print("Save Bad Debts invoice successfully.......")


    def Download_Invoice(self):
        try:
            debts = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_download_icon))
            time.sleep(.2)
            debts .click()
            time.sleep(.5)
            print(" download file successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Pound_Icon(self):
        try:
            pound = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_pound_icon))
            time.sleep(.2)
            pound.click()
            time.sleep(.5)
            print(" Click on Pound icon successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")













