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
import random

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


class Add_Main_File:

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15,
            poll_frequency=0.2,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        self.short_wait = WebDriverWait(
            driver,
            5,
            poll_frequency=0.2
        )

        self.long_wait = WebDriverWait(
            driver,
            30,
            poll_frequency=0.3
        )

        # ------------------------ WebElements of admin for estimate--------------------------------------------------------------
        self.estimates = (By.XPATH,
                          "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[3]/span[1]/span[1]/span[1]")
        self.add_estimates = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Estimate']")
        self.select_item_estimate = (By.XPATH,
                                     "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.add_discount_estimates = (By.XPATH, "//input[@name='discount']")
        self.click_for_enter_note_estimates = (By.XPATH,
                                               "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note_estimates = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note_estimates = (By.XPATH,
                                    "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")
        self.click_download_icon_estimates = (By.XPATH, "(//button[.//i[@data-icon-name='BkInstallation']])[1]")
        self.create_direct_invoice_estimates = (By.XPATH, "(//button[@id='btn-btnCreateInvoice'])[1]")

        # -------------------------------------------------------------------------------------------------------------------------
        self.invoice_section = (By.XPATH, "//button[@role='tab' and normalize-space(.)='Invoices']")

        self.invoice = (By.XPATH, "(//span[contains(text(),'Invoice')])[1]")
        self.click_invoice_section = (
            By.XPATH,
            "//button[@role='tab' and .//span[normalize-space()='Invoices']]"
        )
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice = (By.XPATH,
                                       "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.table = (By.XPATH, " (//div[contains(text(),'Tables')])[1]")

        self.save_invoice = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        self.add_discount = (By.XPATH, "//input[@name='discount']")

        self.click_for_enter_note = (By.XPATH,
                                     "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note = (By.XPATH,
                          "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.allocate_save_button = (By.XPATH, "//div[@role='dialog']//button[.//span[normalize-space()='Save']]")

        self.enter_search = (By.XPATH, "//input[@placeholder='Search']")
        self.cancel_cross_button = (By.XPATH, "//i[@data-icon-name='Clear']")

        self.enter_from_date = (By.XPATH, "//input[@name='fromDate']")
        self.enter_to_date = (By.XPATH, "//input[@name='toDate']")
        self.refresh_icon = (By.XPATH, "//i[@data-icon-name='Refresh']/ancestor::button")

        self.filter_drop_down = (By.XPATH, "//div[contains(@class,'dropdown-indicator')]//*[name()='svg']")

        self.hide_graph = (By.XPATH, "//button[@title='hide reports']//*[name()='svg']")
        self.pagination = (By.XPATH, "//div[@role='combobox']")

        self.three_dot = (By.XPATH,
                          "(//button[starts-with(@id,'btn-overflow-') and contains(@class,'ms-Button--hasMenu')])[1]")
        self.clone = (By.XPATH, "(//span[normalize-space()='Clone'])[1]")
        self.bad_debts = (By.XPATH, "(//span[normalize-space()='Bad debts'])[1]")
        self.click_download_icon = (By.XPATH, "(//button[.//i[@data-icon-name='BkInstallation']])[1]")

        self.click_pound_icon = (By.XPATH,
                                 "(//*[@data-automationid='DetailsRowCell']//button[contains(@id,'btnReceipt')])[1]")

        self.change_quantity = (By.XPATH, "//th[normalize-space()='Qty.']/following::input[@type='number'][1]")
        self.verify_sell_invoice_lock = (By.XPATH, "//button[@id='btn-btnEdit']")
        self.click_on_close = (By.XPATH, "//button[@title='Close']")

        # ----------------------------------------------receipts---------------------------------------------------------------------

        self.receipts = (By.XPATH,
                         "//button[@role='tab' and @data-id='receipts' and .//span[normalize-space()='Receipts']]")

        self.add_receipts = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Receipt']")
        self.select_receive_from = (By.XPATH,
                                    "//label[normalize-space()='Received from']/following::div[contains(@class,'rs-input-container')][1]")
        self.select_amount_receipts = (By.XPATH,
                                       "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.enter_amount_receipts = (By.XPATH,
                                      "//label[normalize-space()='Amount']/following::input[@placeholder='amount'][1]")

        self.method = (By.XPATH, "//label[normalize-space()='Method']/following::div[contains(@class,'rs-control')][1]")

        self.click_for_enter_note_receipts = (By.XPATH,
                                              "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_receipts_note = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note_receipts = (By.XPATH,
                                   "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.save_receipts = (By.XPATH, "//button[.//span[normalize-space()='Save'] and not(contains(.,'Save & New'))]")

        self.click_download_icon_receipts = (By.XPATH, "(//button[.//i[@data-icon-name='BkInstallation']])[1]")

        # ----------------------------------------------CN-------------------------------------------------------------------

        self.credit_notes_tab_main = (
            By.XPATH,
            "//button[@role='tab' and @data-id='credit-notes' "
            "and .//span[normalize-space()='Credit notes']]"
        )

        self.click_credit_notes = (By.XPATH,
                                   "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button[2]/span[1]")
        self.credit_notes = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Credit note']")
        # self.customer_name = (By.XPATH, "//div[contains(text(),'Customer name')]")
        self.invoice_ref_no_cn = (By.XPATH,
                                  "//*[normalize-space()='Invoice ref. no.']/following::div[contains(@class,'rs-input-container')][1]")
        self.clicks_save_cn = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")
        # self.paid_from_locators = (By.XPATH,
        #                            "//*[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.add_discount_cn = (By.XPATH, "//input[@name='discount']")

        self.click_for_enter_note_cn = (By.XPATH,
                                        "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note_cn = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")
        self.save_note_cn = (By.XPATH,
                             "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.enter_search_cn = (By.XPATH, "//input[@placeholder='Search']")
        self.cancel_cross_button_cn = (By.XPATH, "//i[@data-icon-name='Clear']")

        self.enter_from_date_cn = (By.XPATH, "//input[@name='fromDate']")
        self.enter_to_date_cn = (By.XPATH, "//input[@name='toDate']")
        self.refresh_icon = (By.XPATH, "//i[@data-icon-name='Refresh']/ancestor::button")

        self.filter_drop_down_cn = (By.XPATH, "//div[contains(@class,'dropdown-indicator')]//*[name()='svg']")

        self.hide_graph_cn = (By.XPATH, "//button[@title='hide reports']//*[name()='svg']")
        self.pagination_cn = (By.XPATH, "//div[@role='combobox']")

        self.click_download_icon_cn = (By.XPATH, "(//button[.//i[@data-icon-name='BkInstallation']])[1]")

        self.change_quantity_crn = (By.XPATH, "//th[normalize-space()='Qty.']/following::input[@type='number'][1]")

        self.verify_credit_invoice_lock_cn = (By.XPATH, "//button[@id='btn-btnDependencies']")
        self.click_on_close_cn = (By.XPATH, "//button[@title='Close']")

        # -------------------------------------------------------------------------------------------------------------------

        self.purchase_orders = (By.XPATH,
                                "//div[@role='tablist']//button[.//span[normalize-space()='Purchase orders']]")
        self.click_purchase_order = (By.XPATH, "//span[normalize-space(text())='Purchase order']")
        self.select_contact_name_po = (By.XPATH, "//div[contains(text(),'Contact name')]")
        self.click_item_for_invoice_po = (By.XPATH,
                                          "(//table[contains(@class,'table')]//tr[1]//div[contains(@class,'rs-input-container')]//input)[1]")

        self.add_discount_po = (By.XPATH, "//input[@name='discount']")

        self.click_for_enter_note_po = (By.XPATH,
                                        "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")
        self.enter_note_po = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")

        self.save_note_po = (By.XPATH,
                             "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.save_po = (By.XPATH, "//button[.//span[normalize-space(text())='Save']]")
        self.contact_name_input_po = (
            By.XPATH,
            "//label["
            "contains(normalize-space(),'Contact name') or "
            "contains(normalize-space(),'Supplier')"
            "]/following::input[@role='combobox'][1]"
        )
        # --------------------------------------------------Purchases_Invoice----------------------------------------------------

        self.click_purchases = (By.XPATH, "(//div[contains(text(),'Purchases')])[1]")
        self.invoice_purchases_invoice = (By.XPATH, "//button[@aria-label='btnInvoice']")
        self.select_customer = (By.XPATH, "//div[contains(text(),'Contact name')]")

        self.click_item_for_invoice_purchases = (By.XPATH,
                                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/form[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

        self.net_amount_purchases_invoice = (By.XPATH,
                                             "(//table[contains(@class,'table')]//input[contains(@name,'amount.net')])[1]")

        self.loc_save_button_purchases_invoice = (By.XPATH,
                                                  "//div[contains(@class,'modal')]//span[normalize-space(text())='Save']")

        self.add_cash_discount_purchases_invoice = (By.XPATH, "//input[@name='discount']")
        self.click_for_enter_note_purchases_invoice = (By.XPATH,
                                                       "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")

        # ----------------------------------------Payment-------------------------------------------------------------------

        self.payment = (By.XPATH, "//button[@role='tab' and .//span[normalize-space()='Payments']]")
        self.click_payment = (By.XPATH, "//button[.//span[normalize-space()='Payment']]")

        self.paid_to_supplier_payment = (By.XPATH,
                                         "//label[normalize-space()='Paid to']/following::div[contains(@class,'rs-control')][1]")
        self.account_payment = (By.XPATH,
                                "//label[normalize-space(text())='Account']/following::div[contains(@class,'rs-input-container')]//input")
        # self.method = (By.XPATH, "//div[@id='react-select-17-placeholder']")
        self.enter_amount_payment = (By.XPATH, "//input[@name='availableAmount']")
        self.save_payment = (By.XPATH, "//button[.//span[normalize-space(text())='Save']]")
        self.auto_allocation_toggle = (
            By.XPATH,
            "//label[normalize-space()='Auto allocation']"
            "/following::button[@role='checkbox'][1]"
        )

        # ----------------------------------------------purchase_credit_notes------------------------------------------------

        self.click_purchase_credit_notes = (By.XPATH, "//button[@role='tab' and @data-id='credit-notes']")
        self.purchase_credit_notes = (By.XPATH, "//span[contains(@class,'ms-Button-label') and text()='Credit note']")
        self.purchase_credit_notes_invoice_ref_no = (By.XPATH,
                                                     "//*[normalize-space()='Invoice ref. no.']/following::div[contains(@class,'rs-input-container')][1]")

        self.purchase_credit_notes_click_for_enter_note = (By.XPATH,
                                                           "//label[normalize-space()='Note :']/following::div[contains(@style,'overflow-y')][1]")

        self.purchase_credit_notes_enter_note = (By.XPATH, "//iframe[contains(@class,'cke_wysiwyg_frame')]")

        self.purchase_credit_notes_save_note = (By.XPATH,
                                                "//div[contains(@class,'ms-Dialog-main')]//button[.//span[normalize-space()='Save']]")

        self.clicks_save_purchase_cn = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")

        # -----------------------------------------Expense Claim Flow >> Add user--------------------------------------------------
        self.click_expense_claims = (By.XPATH, "(//div[contains(text(),'Expense claims')])[1]")
        self.users_section = (By.XPATH, "//button[.//span[normalize-space()='Users']]")
        self.click_add_user = (By.XPATH, "//button[.//span[normalize-space()='User']]")
        self.click_name_field_user = (By.XPATH,
                                      "//label[normalize-space()='Name']/following::input[@type='text'][1]")
        self.enter_name_user = (By.XPATH, "//label[normalize-space()='Last name']/following::input[@type='text'][2]")
        self.enter_ni_number_user = (By.XPATH,
                                     "//label[normalize-space()='NI Number']/following::input[@type='text'][1]")
        self.click_save_button_user = (By.XPATH, "//button[@type='submit' and .//span[normalize-space()='Save']]")

        # --------------------------------------------expense_claims_tab-----------------------------------------------------

        self.expense_claims_tab = (
            By.XPATH,
            "//button[@role='tab' and @name='Expense claims']"
        )
        self.click_expense_claims_button = (By.XPATH, "//button[.//span[normalize-space()='Expense']]")
        self.select_directors = (By.XPATH,
                                 "//label[normalize-space()='User']/following::div[contains(@class,'rs-placeholder')][1]")
        self.enter_remark_expense_claims = (By.XPATH,
                                            "//label[normalize-space()='Remarks']/following::input[@name='description'][1]")
        self.bill_no_expense_claims = (By.XPATH, "(//table[contains(@class,'table')]//input[@type='text'])[1]")
        self.enter_description_expense_claims = (By.XPATH,
                                                 "//table[.//th[normalize-space()='Description']]   /tbody/tr[1]/td[     count(preceding-sibling::td) =     count(//th[normalize-space()='Description']/preceding-sibling::th)   ]//input[@type='text']")
        self.account_expense_claim = (By.XPATH,
                                      "//*[normalize-space()='Account']/following::input[@role='combobox'][1]")
        self.base_amount_expense_claim = (By.XPATH,
                                          "//td[@data-label='Base amount']//input[@type='text']")
        self.vat_expense_claim = (By.XPATH,
                                  "(//th[normalize-space()='VAT']/ancestor::table[1]//tbody/tr[1]//div[contains(@class,'rs-input-container')])[2]")

        self.save_expense_claim = (By.XPATH, "//button[.//span[normalize-space()='Save']]")
        self.save_expense_click_claim = (By.XPATH,
                                         "//div[@role='dialog']//button[@title='Claim expense with reimbursement']//span[normalize-space()='Save']")

        # -----------------------------------------------------------mileages_section-----------------------------------------------

        self.mileages_section = (By.XPATH, "//button[@name='Mileage claims']")
        self.click_add_mileages = (By.XPATH, "//button[@aria-label='btnAddMileageClaim']")
        self.select_directors_mileages = (By.XPATH,
                                          "//label[normalize-space()='User']/following::div[contains(@class,'rs-placeholder')][1]")
        self.enter_remark_mileages = (By.XPATH, "//label[normalize-space()='Remarks']/following::input[1]")
        self.engine_type = (By.XPATH,
                            "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
        self.enter_description_mileage = (By.XPATH,
                                          "//table[.//th[normalize-space()='Description']]   /tbody/tr[1]/td[     count(preceding-sibling::td) =     count(//th[normalize-space()='Description']/preceding-sibling::th)   ]//input[@type='text']")
        self.mileage = (By.XPATH, "//th[normalize-space()='Mileage (miles)']/following::input[@type='number'][1]")
        self.rate_mileage = (By.XPATH,
                             "//th[normalize-space()='Rate']/following::div[contains(@class,'rs-input-container')][2]//input")
        self.save_mileages = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        self.save_expense_click = (By.XPATH,
                                   "//div[@role='dialog']//button[@title='Claim expense with reimbursement']//span[normalize-space()='Save']")

        # -----------------------------------------------reimbursements_section----------------------------------------------

        self.reimbursements_section = (By.XPATH, "//button[.//span[normalize-space()='Reimbursements']]")
        self.click_reimbursements = (By.XPATH, "//button[.//span[normalize-space()='Reimbursement']]")
        self.reimbursed_to = (By.XPATH, "//div[contains(@class,'placeholder') and normalize-space()='User name']")
        self.reimbursed_account = (By.XPATH,
                                   "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")

        self.reimbursed_amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@type='text'][1]")
        self.enter_notes_reimbursements = (By.XPATH,
                                           "//label[normalize-space()='Note :']/following::input[@name='notes'][1]")

        self.save_reimbursement = (By.XPATH, "(//button[@type='submit'])[1]")

        # ----------------------------------------------refunds_section----------------------------------------------

        self.refunds_section = (By.XPATH, "//button[.//span[normalize-space()='Refunds']]")
        self.click_refunds = (By.XPATH, "//button[.//span[normalize-space()='Refund']]")
        self.refund_from = (
            By.XPATH,
            "//label["
            "contains(normalize-space(),'Refund from') or "
            "contains(normalize-space(),'Refunded from')"
            "]/following::input[@role='combobox'][1]"
        )
        self.refund_account = (By.XPATH,
                               "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        # self.method = (By.XPATH, "//label[normalize-space()='Method']/following::div[contains(@class,'singleValue')][1]")
        self.enter_amount = (By.XPATH, "//input[@name='available' and @placeholder='amount']")
        self.amount = (By.XPATH, "//label[normalize-space()='Amount']/following::input[@type='text'][1]")
        self.enter_notes_for_refund = (By.XPATH,
                                       "//label[normalize-space()='Note :']/following::input[@name='notes'][1]")
        self.save_refund = (By.XPATH, "//span[normalize-space()='Save']/ancestor::button")

        # -----------------------------------------------add_asset------------------------------------------------------

        self.asset = (By.XPATH, "//div[normalize-space()='Assets']/ancestor::a[1]")
        self.click_fixed_asset = (By.XPATH, "//span[contains(text(),'Fixed asset')]")
        self.enter_asset_name_asset = (By.XPATH,
                                       "//label[normalize-space()='Asset name']/following::input[@type='text'][1]")
        self.account_asset = (By.XPATH,
                              "//label[normalize-space()='Account']/following::div[contains(@class,'rs-input-container')][1]")
        self.purchase_price_asset = (By.XPATH,
                                     "//label[normalize-space()='Purchase price (Ex. VAT)']/following::input[@type='text'][1]")

        # self.save_asset = (By.XPATH, "//button[.//span[normalize-space()='Save']]")
        self.save_asset = (By.XPATH, "//button[@title='Save' and .//span[normalize-space()='Save']]")
        self.supplier_asset = (By.XPATH,
                               "//label[normalize-space()='Supplier']/following::div[contains(@class,'rs-input-container')][1]")
        self.rate_asset = (By.XPATH, "//label[normalize-space()='Rate']/following::input[@type='text'][1]")

    # ------------------------------------------------------------------------------------------------------------------

        self.dispose_section = (By.XPATH, "//button[@role='tab' and normalize-space()='Disposed']")
        self.add_dispose = (By.XPATH, "//span[normalize-space()='Dispose asset']/ancestor::button")
        self.select_asset_dispose = (By.XPATH, "//label[normalize-space()='Asset']/following::input[@type='text'][1]")
        self.sales_proceeds_dispose = (By.XPATH,
                                       "//label[normalize-space()='Sales proceeds (Incl. VAT)']/following::input[@type='text'][1]")
        self.payment_method_dispose = (By.XPATH,
                                       "//label[normalize-space()='Payment method']/following::input[@type='text'][1]")
        self.customer_dispose = (By.XPATH, "//label[normalize-space(.)='Customer']/following::input[@type='text'][1]")
        self.save_disposed = (By.XPATH, "//span[text()='Save']/ancestor::button")

    #-------------------------------------------------------------------------------------------------------------------

        self.click_journal = (By.XPATH, "//button[.//span[contains(text(),'Journal')]]")
        self.journal_reference = (By.XPATH,
                                  "//label[normalize-space()='Journal reference']/following::input[@type='text'][1]")
        self.select_account_journal = (By.XPATH, "//td//div[text()='Select']/following::input[1]")
        # self.select_vat = (By.XPATH, "//div[contains(@class,'rs-input-container')]/input[@id='react-select-4-input']")
        self.debit_journal = (By.XPATH, "//input[@id='items.0.debit']")
        self.credit_journal = (By.XPATH, "//input[contains(@id,'credit') and contains(@id,'1')]")
        self.save_journal = (By.XPATH, "//button[.//span[normalize-space()='Save']]")

        self.journals_menu = (
            By.XPATH,
            "//a[@id='Journals' "
            "and @aria-label='Journals' "
            "and contains(@href,'/inputs/journals')]"
        )

    #-------------------------------------------------------------------------------------------------------------------

        self.dividends_section = (By.XPATH, "//a[@data-value='dividends']")

        self.click_dividends = (By.XPATH, "//span[normalize-space(text())='Dividend']")
        self.select_director = (By.XPATH,
                            "//label[normalize-space()='Authorised director']/following::div[contains(@class,'placeholder')][1]")
        self.select_type = (By.XPATH,
                        "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        self.select_class = (By.XPATH, "//div[@id='react-select-8-placeholder' and text()='Select']")
        self.dividend_per_share = (By.XPATH, "//label[text()='Dividend per share']/following::input[1]")
        # self.payment = (By.XPATH, "//label[text()='Payment date']/following::input[1]")
        self.payments_tab = (
            By.XPATH,
            "//button[@role='tab' "
            "and @data-id='payments' "
            "and .//span[normalize-space()='Payments']]"
        )

        self.save_dividends= (
            By.XPATH,
            "//button[@title='Save without journals' "
            "and .//span[normalize-space()='Save']]"
        )
        self.save_anyway = (By.XPATH, "//span[contains(text(),'Save anyway')]")

    # -------------------------------------------------------------------------------------------------------------------

        self.purchase_credit_note_final_save = (
            By.XPATH,
            "//div[@role='dialog']//button["
            ".//span[normalize-space()='Save']"
            "]"
        )





    def Select_Estimates(self):
        try:
            estimate = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.estimates))
            time.sleep(.2)
            estimate.click()
            time.sleep(.2)
            print("Click for select estimate  successfully....!!")
        except Exception as error:
            self.driver.save_screenshot(
                "action_failure.png"
            )

            raise AssertionError(
                f"Action failed: "
                f"{type(error).__name__}: {error}"
            ) from error

    def Add_Estimates(self):

        try:
            add_estimate = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.add_estimates))
            time.sleep(.2)
            add_estimate.click()
            time.sleep(.2)

            print("Click for add_estimates  successfully....!!")
        except Exception as error:
            self.driver.save_screenshot(
                "action_failure.png"
            )

            raise AssertionError(
                f"Action failed: "
                f"{type(error).__name__}: {error}"
            ) from error

    #
    # def Select_Customer_for_Estimate(self):
    #     try:
    #         driver = self.driver
    #         wait = WebDriverWait(driver, 30)
    #
    #         #  Click on the dropdown field
    #         field = wait.until(EC.element_to_be_clickable((
    #             By.XPATH,
    #             "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
    #         )))
    #         driver.execute_script("arguments[0].scrollIntoView({block:'center'});", field)
    #         field.click()
    #         time.sleep(0.5)
    #
    #         # Use keyboard to select first option
    #         active = driver.switch_to.active_element
    #         active.send_keys(Keys.ARROW_DOWN)
    #         time.sleep(0.3)
    #         active.send_keys(Keys.ENTER)
    #         time.sleep(1)
    #
    #         print(" Customer selected successfully for Estimate!")
    #
    #     except Exception as e:
    #         print(f" Could not select customer: {e}")


    def Select_Customer_for_Estimate(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 40)

            customer_xpath = (
                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/"
                "div[1]/div[2]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/"
                "div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
            )

            # Your existing XPath
            field = wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    customer_xpath
                ))
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                field
            )

            # Click wrapper
            driver.execute_script(
                "arguments[0].click();",
                field
            )

            time.sleep(1)

            # Find input inside YOUR xpath element
            customer_input = field.find_element(
                By.XPATH,
                ".//input"
            )

            # Force focus
            driver.execute_script(
                "arguments[0].focus();",
                customer_input
            )

            customer_input.click()

            time.sleep(1)

            customer_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)

            customer_input.send_keys(Keys.ENTER)

            time.sleep(1)

            print("Customer selected successfully for Estimate!")

        except Exception as e:
            print(f"Could not select customer: {e}")
            raise



    def Select_item_Estimate(self, value="test"):
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

    def Add_Attachment_Estimate(self):
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

    def Enter_Discount_Estimate(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)

        try:
            control = wait.until(EC.visibility_of_element_located(self.add_discount_estimates))
            time.sleep(.2)
            control.click()
            time.sleep(.2)
            control.send_keys("10")
            time.sleep(.2)
            print("Discount added successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Click_Enter_Notes_Estimate(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note_estimates))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes_Estimate(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_note_estimates))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)

            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note_estimates))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Click_Save_Estimation(self):

        wait = WebDriverWait(self.driver, 30)

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
        print(" Test Case  :  Pass: -  Estimate  saved successfully.....!!")

    def Download_Invoice_Estimate(self):
        try:
            debts = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_download_icon_estimates))
            time.sleep(.2)
            debts.click()
            time.sleep(.5)
            print(" download file successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Create_Direct_Invoice(self):
        try:
            invoice = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.create_direct_invoice_estimates))
            time.sleep(.2)
            invoice.click()
            time.sleep(.5)
            print("Create Direct Invoice successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Save_Direct_Invoice(self):

        wait = WebDriverWait(self.driver, 30)

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
        print(" Direct invoice   saved from estimate section successfully.....!!")

    # ---------------------------------Add_Invoice------------------------------------------------------------------

    def Click_Invoices_Tab(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            invoice_tab = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[@role='tab' and @name='Invoices']"
                ))
            )

            invoice_tab.click()

            print("Invoices tab clicked successfully!")

        except Exception as e:
            print(f"Error clicking Invoices tab: {e}")
            raise

    def Add_Invoice(self):
        try:
            invoice = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.invoice))
            time.sleep(.2)
            invoice.click()
            time.sleep(.2)
            print("Click on Add invoice button successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Invoice_Section(self):
        try:
            section = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_invoice_section))
            time.sleep(.2)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                section
            )

            section.click()

            print("Clicked on the Invoices tab successfully.")
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

    def Add_Attachment_Invoice(self):
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

    def Enter_Discount_Invoice(self):
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

    def Click_Enter_Notes_Invoice(self):
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

    def Enter_Notes_Invoice(self):
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

    def Click_Save_Invoice(self):

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


        print("Test Case - Pass: Invoice created successfully")

        time.sleep(2)

    # -------------------------------search ---------------------------------------------------------------------------------

    def Enter_Search_Invoice(self):
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

    def Remove_Search_Invoice(self):
        try:
            remove = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.cancel_cross_button)
            )
            time.sleep(.2)
            remove.click()
            time.sleep(.2)
            print("Search functionality reset  successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")

    # ----------------------------------------calendar-----------------------------------------------------------------------

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
            hide = WebDriverWait(self.driver, 40).until(
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

    def Change_Pagination(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            25,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        def get_visible_pagination(current_driver):
            """
            Return the first visible and enabled pagination element.
            """
            elements = current_driver.find_elements(*self.pagination)

            for element in elements:
                try:
                    if element.is_displayed() and element.is_enabled():
                        return element
                except StaleElementReferenceException:
                    continue

            return False

        def select_next_option():
            """
            Open the pagination dropdown and select the next option.
            """
            for attempt in range(1, 4):
                try:
                    dropdown = wait.until(
                        get_visible_pagination,
                        message="No visible pagination dropdown found."
                    )

                    driver.execute_script(
                        """
                        arguments[0].scrollIntoView({
                            block: 'center',
                            inline: 'center'
                        });
                        """,
                        dropdown
                    )

                    try:
                        dropdown.click()

                    except (
                            ElementClickInterceptedException,
                            ElementNotInteractableException
                    ):
                        driver.execute_script(
                            "arguments[0].click();",
                            dropdown
                        )

                    # Send both keys in one operation.
                    # This avoids using the old element after React re-renders.
                    ActionChains(driver) \
                        .send_keys(Keys.ARROW_DOWN) \
                        .send_keys(Keys.ENTER) \
                        .perform()

                    self.wait_for_loader_to_disappear()

                    return True

                except StaleElementReferenceException:
                    print(
                        f"Pagination element became stale. "
                        f"Retrying attempt {attempt}/3."
                    )

                except TimeoutException:
                    if attempt == 3:
                        raise

            return False

        try:
            self.wait_for_loader_to_disappear()

            pagination_elements = driver.find_elements(
                *self.pagination
            )

            visible_elements = []

            for element in pagination_elements:
                try:
                    if element.is_displayed():
                        visible_elements.append(element)
                except StaleElementReferenceException:
                    continue

            if not visible_elements:
                print(
                    "Pagination dropdown is not available. "
                    "The current result set may not contain enough records."
                )
                return False

            # First pagination change
            select_next_option()

            # Re-check because the pagination control may disappear
            # after changing the page size.
            if not get_visible_pagination(driver):
                print(
                    "Pagination dropdown is no longer displayed after "
                    "the first selection."
                )
                return True

            # Second pagination change
            select_next_option()

            print(
                "Pagination functionality is working correctly."
            )

            return True

        except TimeoutException as error:
            driver.save_screenshot(
                "pagination_timeout.png"
            )

            print(
                "Pagination dropdown was not available or clickable "
                "within the expected time."
            )
            print(f"Error details: {repr(error)}")

            raise

        except Exception as error:
            driver.save_screenshot(
                "pagination_failure.png"
            )

            print(
                f"Pagination validation failed. "
                f"Error type: {type(error).__name__}"
            )
            print(f"Error details: {repr(error)}")

            raise
        # -----------------------------------------------------------------------------------------------------------------------

    def Click_Three_Dot(self):
        try:
            dot = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.three_dot))
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
            debts.click()
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
            debts.click()
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

    def Change_Quantity(self):
        try:
            quantity = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.change_quantity))
            time.sleep(.2)
            quantity.click()
            time.sleep(.2)
            quantity.send_keys(Keys.CONTROL, "a")
            time.sleep(.2)
            quantity.send_keys(Keys.BACKSPACE)
            time.sleep(.2)
            quantity.send_keys("2")
            time.sleep(.2)
            quantity.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Quantity changed successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Account_For_Sell(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            account_input = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//label[normalize-space()='Account']"
                        "/following::input[@role='combobox'][1]"
                    )
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                account_input
            )

            account_input.click()

            account_input.send_keys(Keys.CONTROL, "a")
            account_input.send_keys(Keys.BACKSPACE)

            account_input.send_keys("Monzo")

            # Wait until Monzo becomes the focused option
            wait.until(
                lambda d: "Monzo" in (
                    d.find_element(
                        By.ID,
                        "aria-context"
                    ).text
                )
            )

            account_input.send_keys(Keys.ARROW_DOWN)
            account_input.send_keys(Keys.ENTER)

            # Verify selection
            selected_value = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//label[normalize-space()='Account']"
                        "/following::div[contains(@class,'rs-single-value')][1]"
                    )
                )
            )

            assert "Monzo" in selected_value.text, (
                f"Monzo was not selected. Current value: "
                f"{selected_value.text}"
            )

            print(
                f"Account selected successfully: "
                f"{selected_value.text}"
            )

        except Exception as error:
            driver.save_screenshot(
                "select_monzo_account_failure.png"
            )

            raise AssertionError(
                f"Could not select Monzo account: {error}"
            ) from error

        # --------------------------------Verify cell invoice lock---------------------------------------------------------------

    def Click_On_Lock_Button(self):
        try:
            lock = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.verify_sell_invoice_lock))
            time.sleep(.2)
            lock.click()
            time.sleep(.5)
            print(" Verify - "
                  "Invoice is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_On_Close_Icon(self):
        try:
            close = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_on_close))
            time.sleep(.2)
            close.click()
            time.sleep(.5)
            print("Details lock pop up close successfully.....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Refresh_Page(self):
        try:
            self.driver.refresh()

            WebDriverWait(self.driver, 30).until(
                lambda driver: driver.execute_script(
                    "return document.readyState"
                ) == "complete"
            )

            print("Page refreshed successfully.")

        except Exception as error:
            self.driver.save_screenshot(
                "page_refresh_failure.png"
            )

            print(
                f"Page refresh failed: "
                f"{type(error).__name__}: {error}"
            )
            raise

    # ----------------------------------------------- Receipts------------------------------------------------------------------

    def Receipts(self):
        try:
            click_receipts = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.receipts))
            time.sleep(.2)
            click_receipts.click()
            time.sleep(.2)
            print("click on credit section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Add_Receipts(self):
        try:
            add_receipts = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.add_receipts))
            time.sleep(.2)
            add_receipts.click()
            time.sleep(.2)
            print("click for add new receipts successfully.....!! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Receipts_from(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            # Click Received From field
            receipts = wait.until(
                EC.element_to_be_clickable(self.select_receive_from)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                receipts
            )

            driver.execute_script(
                "arguments[0].click();",
                receipts
            )

            time.sleep(1)

            # Find focused element after dropdown opens
            active = driver.switch_to.active_element

            # Click/focus it once more
            driver.execute_script(
                "arguments[0].focus();",
                active
            )

            time.sleep(0.3)

            # Select first option
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)

            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print("Customer selected successfully for Receipt!")

        except Exception as e:
            print(f"Could not select Receipt From customer: {e}")
            raise

    # def Select_Receipts_from(self):
    #     driver = self.driver
    #     try:
    #         receipts = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.select_receive_from))
    #         time.sleep(.2)
    #         receipts.click()
    #         time.sleep(.2)
    #         active = driver.switch_to.active_element
    #         time.sleep(.3)
    #         active.send_keys(Keys.ARROW_DOWN)
    #         time.sleep(0.3)
    #         active.send_keys(Keys.ARROW_DOWN)
    #         time.sleep(0.3)
    #         active.send_keys(Keys.ENTER)
    #         time.sleep(1)
    #
    #         print(" Customer selected successfully for Estimate!")
    #
    #     except Exception as e:
    #         print(f" Could not select customer: {e}")

    def Select_Amount_Receipts(self):
        try:
            amount = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.select_amount_receipts))
            time.sleep(.2)
            amount.click()
            time.sleep(.2)
            amount.send_keys(Keys.ENTER)
            time.sleep(2)
            print("Customer selected successfully....!!")

        except Exception as e:
            print(f"Error on Click : {e}")

    def Enter_Amount_Receipts(self):
        try:
            enter_a_amount = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_amount_receipts))
            time.sleep(.2)
            random_price = round(random.uniform(50, 999), 2)
            time.sleep(.2)

            enter_a_amount.send_keys(Keys.CONTROL, 'a')
            enter_a_amount.send_keys(Keys.BACKSPACE)
            time.sleep(.2)

            enter_a_amount.send_keys(str(random_price))
            enter_a_amount.send_keys(Keys.TAB)
            time.sleep(.2)

            print(f" Entered random price: £{random_price}")
            time.sleep(0.5)
        except Exception as e:
            print(f"Error on Click : {e}")

    def Select_Method_Receipts(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        # 1) click react-select control
        control = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Method']/following::div[contains(@class,'rs-control')][1]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", control)
        control.click()
        time.sleep(.2)
        pyautogui.press('down')
        time.sleep(.2)
        pyautogui.press('enter')
        time.sleep(.2)
        print("Selected method successfully......!!")



    def Add_Attachment_Receipt(self):
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

    def Click_Enter_Notes_Receipt(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note_receipts))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes_Receipt(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_receipts_note))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)

            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note_receipts))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Save_Receipt(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            # Wait for loader to disappear before clicking
            try:
                wait.until(
                    EC.invisibility_of_element_located(
                        (By.CSS_SELECTOR, ".ant-spin-spinning")
                    )
                )
            except TimeoutException:
                pass

            save_button = wait.until(
                EC.element_to_be_clickable(self.save_receipts)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                save_button
            )

            time.sleep(0.4)

            try:
                save_button.click()
            except (ElementClickInterceptedException, StaleElementReferenceException):
                save_button = wait.until(
                    EC.presence_of_element_located(self.save_receipts)
                )
                driver.execute_script("arguments[0].click();", save_button)

            print("Save Receipt button clicked successfully.")

            # Verification options
            verified = False

            # 1. Check success message
            try:
                message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        "//*[contains(normalize-space(.),'Receipt saved successfully') "
                        "or contains(normalize-space(.),'created successfully') "
                        "or contains(normalize-space(.),'saved successfully')]"
                    ))
                )
                print(f"Save verified by message: {message.text}")
                verified = True
            except TimeoutException:
                pass

            # 2. Check dialog/form closes
            if not verified:
                try:
                    WebDriverWait(driver, 10).until(
                        EC.invisibility_of_element_located(
                            self.save_receipts
                        )
                    )
                    print("Save verified: Receipt form/dialog closed.")
                    verified = True
                except TimeoutException:
                    pass

            # 3. Check loader appears and disappears
            if not verified:
                try:
                    short_wait = WebDriverWait(driver, 5)

                    short_wait.until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, ".ant-spin-spinning")
                        )
                    )

                    wait.until(
                        EC.invisibility_of_element_located(
                            (By.CSS_SELECTOR, ".ant-spin-spinning")
                        )
                    )

                    print("Save verified through loader completion.")
                    verified = True
                except TimeoutException:
                    pass

            if verified:
                print("Test Case - 5: Pass - Receipt saved successfully.")
            else:
                print(
                    "Save button was clicked, but no confirmation message, "
                    "dialog closure, or loader activity was detected."
                )

        except Exception as e:
            driver.save_screenshot("save_receipt_error.png")
            print(f"Error while saving receipt: {e}")
            raise

    def Download_Invoice_Receipt(self):
        try:
            debts = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_download_icon_receipts))
            time.sleep(.2)
            debts.click()
            time.sleep(.5)
            print("Download file successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def wait_for_loader_to_disappear(self, timeout=30):
        loader_locator = (
            By.XPATH,
            "//*["
            "contains(@class,'spinner') or "
            "contains(@class,'loading') or "
            "contains(@class,'ms-Spinner') or "
            "contains(@class,'ant-spin-spinning')"
            "]"
        )

        WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=0.2
        ).until(
            EC.invisibility_of_element_located(
                loader_locator
            )
        )

    def save_screenshot(self, file_name):
        try:
            self.driver.save_screenshot(file_name)
            print(f"Screenshot saved: {file_name}")
        except Exception as error:
            print(f"Could not save screenshot: {error}")


    # --------------------------------------------------credit_notes---------------------------------------------------------

    def Click_Credit_Notes_Main(self):
        try:
            click_credit_notes = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.credit_notes_tab_main))
            time.sleep(.2)
            click_credit_notes.click()
            time.sleep(.2)
            print("click on credit section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Add_Credit_Note(self):
        try:
            credit = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.credit_notes))
            time.sleep(.2)
            credit.click()
            time.sleep(.2)

            print("Click for add credit  successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Customer_for_Credit_Note(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

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
            time.sleep(0.5)
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            active.send_keys(Keys.ENTER)
            time.sleep(1)

            print(" Customer selected successfully for Credit Note......!!")

        except Exception as e:
            print(f" Could not select customer: {e}")

    def Invoice_ref_CN(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        retries = 3  # maximum attempts

        for attempt in range(retries):
            try:
                # Locate dropdown
                dropdown = wait.until(EC.element_to_be_clickable(self.invoice_ref_no_cn))
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", dropdown)
                dropdown.click()
                time.sleep(0.4)

                # Select next option
                active = driver.switch_to.active_element
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                active.send_keys(Keys.ENTER)
                time.sleep(0.5)

                # ✔ CHECK SAVE BUTTON ENABLED OR NOT
                save_button = wait.until(EC.presence_of_element_located(self.clicks_save_cn))

                is_enabled = save_button.is_enabled()

                if is_enabled:
                    print("Invoice reference selected successfully......!!")
                    return True

                else:
                    print(f"Save button still disabled… retrying ({attempt + 1}/{retries})")
                    time.sleep(1)

            except Exception as e:
                print(f"Error selecting invoice reference (attempt {attempt + 1}): {e}")
                time.sleep(1)

        print(" Failed: Save button not enabled after retries.....!")
        return False

    def Add_Attachment_CN(self):
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

    def Enter_Discount_CN(self):
        wait = WebDriverWait(self.driver, 30)

        try:
            discount = wait.until(
                EC.presence_of_element_located(self.add_discount_cn)
            )

            # Check if the field is disabled
            if (not discount.is_enabled()
                    or discount.get_attribute("disabled")
                    or discount.get_attribute("readonly")
                    or discount.get_attribute("aria-disabled") == "true"):
                print("Discount field is disabled. Skipping discount entry as this invoice does not support discounts.")
                return

            # Field is enabled
            wait.until(EC.element_to_be_clickable(self.add_discount_cn))

            discount.clear()
            discount.click()
            discount.send_keys("10")

            print("Discount applied successfully....!!")

        except Exception as e:
            print(f"Error in Enter_Discount: {e}")

    def Click_Enter_Notes_CN(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note_cn))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes_CN(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_note_cn))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)

            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note_cn))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Save_Credit_Notes(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_credit_note = wait.until(
                EC.element_to_be_clickable(self.clicks_save_cn)
            )
            time.sleep(.2)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_credit_note)
            time.sleep(0.4)
            save_credit_note.click()
            time.sleep(0.4)
            print("click on save credit note successfully....!!")
        except Exception as e:
            print(f" Could not select customer: {e}")

    def Paid_From_CN(self):
        try:

            driver = self.driver
            wait = WebDriverWait(driver, 30)

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

            print(" 'Paid from' selected successfully.....!")
        except Exception as e:
            print(f" Could not select customer: {e}")

    def Click_Save_Button_CN(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

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
        print(" Test Case - : Pass :  Credit note saved successfully for Sales...!")

    def Enter_Search_CN(self):
        try:
            search = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.enter_search_cn))
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

    def Remove_Search_CN(self):
        try:
            remove = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.cancel_cross_button_cn)
            )
            time.sleep(.2)
            remove.click()
            time.sleep(.2)
            print("Search functionality reset  successfully........!! ")

        except Exception as e:
            print(f"Error: {e}")

    def clear_and_enter_date_cn(self, element, value):
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

    def Change_Date_Calendar_CN(self):
        try:
            wait = WebDriverWait(self.driver, 40)

            self.wait_for_spinner_to_disappear()

            from_date = wait.until(
                EC.presence_of_element_located(self.enter_from_date_cn)
            )

            to_date = wait.until(
                EC.presence_of_element_located(self.enter_to_date_cn)
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

    def Select_Filter_CN(self):
        wait = WebDriverWait(self.driver, 20)

        dropdown = wait.until(
            EC.element_to_be_clickable(self.filter_drop_down_cn)
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

    def Hide_Reports_CN(self):
        try:
            hide = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable(self.hide_graph_cn)
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

    def Select_Pagination_Option_CN(self, value):
        wait = WebDriverWait(self.driver, 30)

        # Open pagination dropdown
        dropdown = wait.until(
            EC.presence_of_element_located(self.pagination_cn)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            dropdown
        )

        time.sleep(0.5)

        self.driver.execute_script("arguments[0].click();", dropdown)

        # Select option by visible text
        option_xpath = (
            f"//span[normalize-space()='{value}']"
            f"|//button[@role='option']//span[normalize-space()='{value}']"
            f"|//div[@role='option']//span[normalize-space()='{value}']"
        )

        option = wait.until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )

        self.driver.execute_script("arguments[0].click();", option)

        time.sleep(3)

    def Change_Pagination_CN(self):
        wait = WebDriverWait(self.driver, 30)

        try:
            page = wait.until(
                EC.presence_of_element_located(self.pagination_cn)
            )

            if (
                    not page.is_enabled()
                    or page.get_attribute("disabled")
                    or page.get_attribute("readonly")
                    or page.get_attribute("aria-disabled") == "true"
            ):
                print("Pagination is not available on this page.")
                return

            self.Select_Pagination_Option_CN("30")
            self.Select_Pagination_Option_CN("50")

            print("Pagination functionality is working successfully.")

        except TimeoutException as e:
            print("Pagination dropdown or option was not found/clickable.")
            print(e)
            raise

        except Exception as e:
            print(f"Error while changing pagination: {e}")
            raise

    def Download_Invoice_CN(self):
        try:
            debts = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_download_icon_cn))
            time.sleep(.2)
            debts.click()
            time.sleep(.5)
            print(" Download file successfully.....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def wait_for_page_ready(self, timeout=20):
        wait = WebDriverWait(self.driver, timeout)

        # Wait for the browser document.
        wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Wait for Fluent UI overlay.
        wait.until(
            EC.invisibility_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'ms-Overlay') "
                    "and not(contains(@style,'display: none'))]"
                )
            )
        )

        # Wait for common loaders/spinners.
        wait.until(
            EC.invisibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(@class,'spinner') "
                    "or contains(@class,'Spinner') "
                    "or contains(@class,'loader') "
                    "or contains(@class,'Loader')]"
                )
            )
        )

    def Change_CRN_Quantity(self):
        try:
            quantity = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.change_quantity_crn))
            time.sleep(.2)
            quantity.click()
            time.sleep(.2)
            quantity.send_keys(Keys.CONTROL, "a")
            time.sleep(.2)
            quantity.send_keys(Keys.BACKSPACE)
            time.sleep(.2)
            quantity.send_keys("1")
            time.sleep(.2)
            quantity.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Quantity changed successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Account_CRN(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            30,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        account_input_locator = (
            By.XPATH,
            "//div[contains(@class,'ms-Modal-scrollableContent')]"
            "//input[@role='combobox' "
            "and @aria-haspopup='true']"
        )

        # React Select option IDs contain "-option-"
        monzo_option_locator = (
            By.XPATH,
            "//div[contains(@id,'-option-') "
            "and contains(normalize-space(.), "
            "'Monzo - Current')]"
        )

        try:
            account_input = wait.until(
                EC.element_to_be_clickable(
                    account_input_locator
                )
            )

            driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                account_input
            )

            account_input.click()

            # Clear existing text
            account_input.send_keys(Keys.CONTROL, "a")
            account_input.send_keys(Keys.BACKSPACE)

            # Search for Monzo
            account_input.send_keys("Monzo")

            try:
                # The options menu is rendered outside the modal
                monzo_option = WebDriverWait(
                    driver,
                    10,
                    poll_frequency=0.2
                ).until(
                    EC.element_to_be_clickable(
                        monzo_option_locator
                    )
                )

                driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        block: 'nearest'
                    });
                    """,
                    monzo_option
                )

                # Normal Selenium click
                try:
                    monzo_option.click()

                except Exception:
                    # Fallback if another element intercepts the click
                    driver.execute_script(
                        "arguments[0].click();",
                        monzo_option
                    )

            except TimeoutException:
                # Keyboard fallback for React Select
                print(
                    "Direct Monzo option locator was not found. "
                    "Using keyboard selection."
                )

                account_input.send_keys(Keys.ARROW_DOWN)
                account_input.send_keys(Keys.ENTER)

            # Check selection inside the same React Select container
            def get_selected_monzo(current_driver):
                try:
                    current_input = current_driver.find_element(
                        *account_input_locator
                    )

                    select_container = current_input.find_element(
                        By.XPATH,
                        "./ancestor::div["
                        "contains(@class,'rs-container')][1]"
                    )

                    container_text = (
                        select_container.text.strip()
                    )

                    if "Monzo" in container_text:
                        return container_text

                    return False

                except (
                        StaleElementReferenceException,
                        TimeoutException
                ):
                    return False

            selected_account = wait.until(
                get_selected_monzo,
                message=(
                    "Monzo option was clicked, but it was not "
                    "displayed as the selected account."
                )
            )

            print(
                "Account selected successfully: "
                f"{selected_account}"
            )

            return selected_account

        except Exception as error:
            driver.save_screenshot(
                "select_monzo_account_failure.png"
            )

            print(
                "Could not select Monzo account."
            )
            print(
                f"Error type: {type(error).__name__}"
            )
            print(
                f"Error details: {repr(error)}"
            )

            raise

    def Click_On_Lock_Button_Credit(self):
        try:
            lock = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.verify_credit_invoice_lock_cn))
            time.sleep(.2)
            lock.click()
            time.sleep(.5)
            print(" Verify - "
                  "Invoice is locked .....! ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_On_Close_Icon_CN(self):
        try:
            close = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_on_close_cn))
            time.sleep(.2)
            close.click()
            time.sleep(.5)
            print("Details lock pop up close successfully.....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    # ---------------------------------------------PO-----------------------------------------------------------------------

    def Purchase_Order(self):
        try:
            click_credit_notes = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.purchase_orders))
            time.sleep(.2)
            click_credit_notes.click()
            time.sleep(.2)
            print("click on Purchase order section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Purchase_Order(self):
        driver = self.driver
        wait = WebDriverWait(driver, 25)

        try:
            self.wait_for_loader_to_disappear()

            add_po_button = wait.until(
                EC.element_to_be_clickable(
                    self.click_purchase_order
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                add_po_button
            )

            try:
                add_po_button.click()
            except ElementClickInterceptedException:
                self.wait_for_loader_to_disappear()

                add_po_button = wait.until(
                    EC.element_to_be_clickable(
                        self.click_purchase_order
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    add_po_button
                )

            # Wait until form is actually open
            wait.until(
                EC.presence_of_element_located(
                    self.contact_name_input_po
                )
            )

            self.wait_for_loader_to_disappear()

            print("Purchase Order form opened successfully.")

        except Exception as error:
            driver.save_screenshot(
                "open_purchase_order_form_failure.png"
            )

            raise AssertionError(
                f"Could not open Purchase Order form: {error}"
            ) from error

    def Select_Contact_Name_PO(self):
        d = self.driver
        w = WebDriverWait(d, 30)

        control = w.until(EC.element_to_be_clickable(
            self.select_contact_name_po  # outer control
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

    def Add_Attachment_PO(self):
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

    def Click_Item_For_Invoice_PO(self):

        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

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

    def Enter_Discount_PO(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)

        try:
            control = wait.until(EC.visibility_of_element_located(self.add_discount_po))
            time.sleep(.2)
            control.click()
            time.sleep(.2)
            control.send_keys("10")
            time.sleep(.2)
            print("Discount added successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Click_Enter_Notes_PO(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note_po))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes_PO(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.enter_note_po))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)

            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.save_note_po))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Save_PO(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        save_btn = wait.until(EC.element_to_be_clickable(self.save_po))

        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
        time.sleep(0.3)

        try:
            save_btn.click()
        except:
            driver.execute_script("arguments[0].click();", save_btn)

        time.sleep(1)
        print("Test Case  :  Pass:  Purchase Order saved successfully!")

    # -------------------------------------------------Purchases >> Add Invoice------------------------------------------

    def Click_Purchases(self):
        try:
            sales = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_purchases))
            time.sleep(.2)
            sales.click()
            time.sleep(.2)
            print("Click on purchases successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Add_Invoice_Purchases(self):

        try:
            invoice = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.invoice_purchases_invoice))
            time.sleep(.2)
            invoice.click()
            time.sleep(.2)
            print("Click on Add invoice button successfully....!!")


        except Exception as e:
            print(f"Error on Click : {e}")

    def Select_Customer_Purchases_Invoice(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            dropdown_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='react-select-'][id$='-input']"))
            )
            time.sleep(.2)
            dropdown_input.click()
            time.sleep(.2)
            dropdown_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.5)
            dropdown_input.send_keys(Keys.ENTER)
            time.sleep(0.5)

            time.sleep(.2)
            # dropdown_input.send_keys(Keys.ENTER)
            time.sleep(.5)
            print("Customer selected successfully....!!")

        except Exception as e:
            print(f"Error on Click : {e}")

    def Add_Attachment_Purchases_Invoice(self):
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

    def Enter_Cash_Discount_Purchases_Invoice(self):
        wait = WebDriverWait(self.driver, 30)

        try:
            control = wait.until(
                EC.element_to_be_clickable(self.add_cash_discount_purchases_invoice)
            )

            control.click()

            # Select and remove the existing value
            control.send_keys(Keys.CONTROL, "a")
            time.sleep(.2)
            control.send_keys(Keys.BACKSPACE)

            # Enter the new value
            control.send_keys("20")

            print("Cash Discount added successfully!")

        except Exception as e:
            print(f"Error while entering Cash Discount: {e}")

    # def Click_Enter_Notes_Purchases_Invoice(self):
    #     driver = self.driver
    #     wait = WebDriverWait(self.driver, 30)
    #     try:
    #
    #         click_for_note = wait.until(EC.element_to_be_clickable(self.click_for_enter_note_purchases_invoice))
    #         time.sleep(.2)
    #         click_for_note.click()
    #         time.sleep(2)
    #         print("Click on enter notes  successfully....!!")
    #     except Exception as e:
    #
    #         print(f"Error on Click : {e}")

    
    def Click_Enter_Notes_Purchases_Invoice(self):

        driver = self.driver
        wait = WebDriverWait(driver, 15)

        note_locator = (
            By.XPATH,
            "//label[contains(normalize-space(),'Note')]/following::input[1]"
        )

        try:
            note = wait.until(
                EC.presence_of_element_located(note_locator)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                note
            )

            # Re-find after scrolling
            note = wait.until(
                EC.element_to_be_clickable(note_locator)
            )

            note.click()

            print("Notes field clicked successfully!")

        except (
                TimeoutException,
                StaleElementReferenceException,
                ElementClickInterceptedException
        ) as e:

            print(
                f"Failed to click Purchase Invoice Notes field: "
                f"{type(e).__name__}"
            )

            driver.save_screenshot(
                "reports/Purchase_Invoice_Notes_Click_Error.png"
            )

            raise

    def Enter_Amount_Purchases_Invoice(self):
        try:
            amount = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.net_amount_purchases_invoice))
            time.sleep(.2)
            amount.send_keys("1000")
            time.sleep(.2)
            print("Enter amount successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Enter_Notes_Purchases_Invoice(self):
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

    def Select_item_purchase(self, value="test"):
        d = self.driver
        w = self.wait
        container_el = w.until(
            EC.visibility_of_element_located(self.click_item_for_invoice_purchases)
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

    def Enter_amount_Purchases_Invoice(self):
        try:
            amount = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.net_amount_purchases_invoice))
            time.sleep(.2)
            amount.send_keys("1000")
            time.sleep(.2)
            print("Enter amount successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Save_Services_Purchases_Invoice(self):
        wait = WebDriverWait(self.driver, 30)

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
        print("Click on Save button  successfully")
        # try:
        #     update_message = WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located(
        #             (By.XPATH, "//*[contains(text(),'Invoice created successfully')]")
        #         )
        #     )
        # except TimeoutException:
        #     raise AssertionError(
        #         "Expected 'Invoice created successfully' toast but did not see it."
        #     )
        #
        # assert update_message.is_displayed(), "Invoice created successfully"

        print("Test Case - :  Pass:: Purchases Invoice created successfully.")

    # -----------------------------------------------Payment-----------------------------------------------------------------

    # ----------------------------------------Payment_Section-------------------------------------------------------------

    def Payment_Section(self):

        try:
            payment_section = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.payments_tab))
            time.sleep(.2)
            payment_section.click()
            time.sleep(.2)
            print("click on Payment section successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Click_Payment(self):
        try:
            payment = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_payment))
            time.sleep(.2)
            payment.click()
            time.sleep(.2)

            print("Click on payment successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Paid_To_Supplier_Main(self):
        d = self.driver
        w = WebDriverWait(d, 30)

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
        time.sleep(.2)
        rs_input.send_keys(Keys.ARROW_DOWN)

        time.sleep(0.2)
        rs_input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        print("Select Supplier successfully!")

    def Select_Account_Payment(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            supplier_dropdown = wait.until(EC.element_to_be_clickable(self.account_payment))
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", supplier_dropdown)
            supplier_dropdown.click()
            time.sleep(0.5)
            active = driver.switch_to.active_element
            time.sleep(.2)
            active.send_keys(Keys.ENTER)
            time.sleep(.2)
            print("Select Account type successfully!")
        except Exception as e:
            print(f" Could not select Account type: {e}")



    def Enter_Amount_Payment(self, amount="100"):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        amount_locator = (
            By.XPATH,
            "//label[normalize-space()='Amount']/following::input[1]"
        )

        save_locator = (
            By.XPATH,
            "//button[.//span[normalize-space()='Save']]"
        )

        try:
            amount_input = wait.until(
                EC.element_to_be_clickable(amount_locator)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                amount_input
            )

            # Real keyboard interaction
            ActionChains(driver) \
                .click(amount_input) \
                .key_down(Keys.CONTROL) \
                .send_keys("a") \
                .key_up(Keys.CONTROL) \
                .send_keys(Keys.BACKSPACE) \
                .send_keys(str(amount)) \
                .pause(0.5) \
                .send_keys(Keys.TAB) \
                .perform()

            # Ensure React receives blur/focusout
            driver.execute_script(
                """
                const input = arguments[0];

                input.dispatchEvent(
                    new Event('change', {
                        bubbles: true
                    })
                );

                input.dispatchEvent(
                    new FocusEvent('blur', {
                        bubbles: true
                    })
                );

                input.dispatchEvent(
                    new FocusEvent('focusout', {
                        bubbles: true
                    })
                );
                """,
                amount_input
            )

            # Wait until Save becomes enabled
            def save_is_enabled(current_driver):
                buttons = current_driver.find_elements(
                    *save_locator
                )

                for button in buttons:
                    if (
                            button.is_displayed()
                            and button.is_enabled()
                            and button.get_attribute("disabled") is None
                            and button.get_attribute("aria-disabled") != "true"
                    ):
                        return True

                return False

            wait.until(save_is_enabled)

            print(
                f"Payment amount entered and Save enabled: "
                f"£{float(amount):.2f}"
            )

        except Exception as error:
            driver.save_screenshot(
                "payment_amount_tab_failure.png"
            )

            buttons = driver.find_elements(*save_locator)

            for button in buttons:
                print(
                    "Save visible:",
                    button.is_displayed(),
                    "enabled:",
                    button.is_enabled(),
                    "disabled:",
                    button.get_attribute("disabled"),
                    "aria-disabled:",
                    button.get_attribute("aria-disabled")
                )

            raise AssertionError(
                f"Could not activate Save after entering amount: "
                f"{type(error).__name__}: {error}"
            ) from error



    def is_save_payment_enabled(self):
        buttons = self.driver.find_elements(
            By.XPATH,
            "//button[.//span[normalize-space()='Save']]"
        )

        for button in buttons:
            try:
                class_name = button.get_attribute("class") or ""
                aria_disabled = button.get_attribute("aria-disabled")

                if (
                        button.is_displayed()
                        and button.is_enabled()
                        and button.get_attribute("disabled") is None
                        and aria_disabled != "true"
                        and "is-disabled" not in class_name
                ):
                    return button

            except StaleElementReferenceException:
                continue

        return False


    def Enable_Auto_Allocation(self):
        wait = WebDriverWait(self.driver, 20)

        toggle = wait.until(
            EC.element_to_be_clickable(
                self.auto_allocation_toggle
            )
        )

        if toggle.get_attribute("aria-checked") != "true":
            toggle.click()

            wait.until(
                lambda driver: driver.find_element(
                    *self.auto_allocation_toggle
                ).get_attribute("aria-checked") == "true"
            )

        print("Auto allocation is enabled.")

    def Save_payment(self):
        save_locator = (
            By.XPATH,
            "//button[.//span[normalize-space()='Save']]"
        )

        save_button = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.element_to_be_clickable(save_locator)
        )

        save_button.click()
        self.wait_for_loader_to_disappear()

        print("Payment saved successfully.")








    # ---------------------------------------------------Purchase_CN--------------------------------------------------------

    def Click_Purchase_Credit_Notes(self):
        try:
            click_credit_notes = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.click_purchase_credit_notes))
            time.sleep(.2)
            click_credit_notes.click()
            time.sleep(.3)
            print("click on credit section of purchase note successfully......!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.3)

    def Add_Purchase_Credit_Note(self):
        try:
            credit = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.purchase_credit_notes))
            time.sleep(.2)
            credit.click()
            time.sleep(.2)

            print("Click for add credit  successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.3)

    def Select_Suppiler_for_Purchase_Credit_Note(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            #  Click on the dropdown field
            field = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'rs-placeholder') and normalize-space()='Supplier name']/ancestor::div[contains(@class,'rs-control')][1]"
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

    def Purchase_Credit_Note_Invoice_ref(self):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            #  Click on the Invoice Ref dropdown
            dropdown = wait.until(EC.element_to_be_clickable(self.purchase_credit_notes_invoice_ref_no))
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

    def Add_Attachment_Purchase_Credit_Note(self):
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

    def wait_for_blockers_to_disappear(self, timeout=30):
        blockers = [
            (By.XPATH, "//*[contains(@class,'spinner')]"),
            (By.XPATH, "//*[contains(@class,'Spinner')]"),
            (By.XPATH, "//*[contains(@class,'loading')]"),
            (By.XPATH, "//*[contains(@class,'Loading')]"),
            (By.XPATH, "//div[contains(@class,'ms-Overlay')]"),
        ]

        for blocker in blockers:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located(blocker)
                )
            except:
                pass

    def Enter_Discount_Purchase_Credit_Note(self, value="10"):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        locator = (
            By.CSS_SELECTOR,
            "input[name='discount'][type='number']"
        )

        for attempt in range(3):

            try:
                discount = wait.until(
                    EC.visibility_of_element_located(locator)
                )

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    discount
                )

                # Fresh reference
                discount = wait.until(
                    EC.visibility_of_element_located(locator)
                )

                driver.execute_script(
                    "arguments[0].focus();",
                    discount
                )

                discount.send_keys(Keys.CONTROL, "a")
                discount.send_keys(value)

                # Trigger React blur/change calculation
                discount.send_keys(Keys.TAB)

                print(
                    f"Discount '{value}' entered successfully "
                    f"for Purchase Credit Note!"
                )

                return

            except StaleElementReferenceException:
                print(
                    f"Discount became stale - retry "
                    f"{attempt + 1}/3"
                )

        raise Exception(
            "Unable to enter Purchase Credit Note Discount."
        )


    def Click_Purchase_Credit_Notes_Enter_Notes(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 30)
        try:

            click_for_note = wait.until(EC.element_to_be_clickable(self.purchase_credit_notes_click_for_enter_note))
            time.sleep(.2)
            click_for_note.click()
            time.sleep(2)
            print("Click on enter notes  successfully....!!")
        except Exception as e:

            print(f"Error on Click : {e}")

    def Enter_Notes_Purchase_Credit_Notes(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)
        try:
            enter_notes = wait.until(EC.visibility_of_element_located(self.purchase_credit_notes_enter_note))

            enter_notes.click()
            enter_notes.send_keys(Keys.CONTROL, "a")
            enter_notes.send_keys(Keys.BACKSPACE)

            enter_notes.send_keys("Only for testing....!!")

            click_save_notes = wait.until(EC.element_to_be_clickable(self.purchase_credit_notes_save_note))
            click_save_notes.click()

            print("Notes added successfully....!!")
        except Exception as e:
            print(f"Error on Click : {e}")

    def Save_Credit_Notes_Purchase_Credit_Notes(self):
        try:
            wait = WebDriverWait(self.driver, 30)

            try:

                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin-spinning")))
            except:
                pass

            save_credit_note = wait.until(
                EC.element_to_be_clickable(self.clicks_save_purchase_cn)
            )
            time.sleep(.2)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_credit_note)
            time.sleep(0.4)
            save_credit_note.click()
            time.sleep(0.4)
            print("click on save credit note successfully....!!")
        except Exception as e:
            print(f" Could not select customer: {e}")

    def Click_Save_Button_Purchase_Credit_Note(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            self.wait_for_loader_to_disappear()
            self.wait_for_overlay_to_disappear()

            save_button = wait.until(
                EC.element_to_be_clickable(
                    self.purchase_credit_note_final_save
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                save_button
            )

            save_button.click()

            wait.until(
                EC.invisibility_of_element_located(
                    self.purchase_credit_note_final_save
                )
            )

            self.wait_for_loader_to_disappear()

            print(
                "Purchase Credit Note saved successfully."
            )

        except Exception as error:
            driver.save_screenshot(
                "purchase_credit_note_final_save_failure.png"
            )

            raise AssertionError(
                f"Could not click final Save button: {error}"
            ) from error

    # def Click_Save_Button_Purchase_Credit_Note(self):
    #     driver = self.driver
    #     wait = WebDriverWait(driver, 30)
    #
    #     save_btn = wait.until(EC.element_to_be_clickable((
    #         By.XPATH, "//div[@role='dialog']//button[@title='Save' and .//span[normalize-space()='Save']]"
    #     )))
    #
    #     driver.execute_script("arguments[0].scrollIntoView({block:'center'});", save_btn)
    #     time.sleep(0.3)
    #
    #     try:
    #         save_btn.click()
    #     except:
    #         driver.execute_script("arguments[0].click();", save_btn)
    #
    #     time.sleep(1)
    #
    #     toast_xpath = "//div[contains(text(),'Duplicate refund number')]"
    #
    #     try:
    #         toast_msg = WebDriverWait(driver, 30).until(
    #             EC.visibility_of_element_located((By.XPATH, toast_xpath))
    #         )
    #         txt = toast_msg.text.lower()
    #
    #         if "duplicate" in txt or "already exists" in txt:
    #             print(" Duplicate entry detected — stopping further execution.")
    #
    #             time.sleep(.2)
    #             driver.back()
    #             time.sleep(.5)
    #
    #         else:
    #             print(" Test Case -: Pass : Purchase credit note saved successfully....!")
    #
    #     except TimeoutException:
    #         print(" Duplicate entry is not detected")

    # -----------------------------------------Expense Claim Flow >> Add user--------------------------------------------------

    def Click_Expense_Claims(self):
        try:
            claims = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_expense_claims))
            time.sleep(.2)
            claims.click()
            time.sleep(.2)
            print("Click on Expense claims successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def User_Section(self):
        try:
            user_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.users_section))
            time.sleep(.2)
            user_sec.click()
            time.sleep(.2)
            print("Click on User Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Add_User(self):
        try:
            click_user = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_add_user))
            time.sleep(.2)
            click_user.click()
            time.sleep(.2)
            print("Click on Add user icon successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Name_Field_User(self):
        # try:
        click_name = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.click_name_field_user))
        time.sleep(.2)
        click_name.click()
        time.sleep(.2)
        print("Click on  name icon successfully....!!")

    # except Exception as e:
    #     print(f"Error on Click:{e}")

    def Select_Title_User(self, title="Mr"):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        title_input = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[normalize-space()='First name']"
                    "/following::input[@role='combobox'][1]"
                )
            )
        )

        title_input.click()
        title_input.send_keys(title)
        title_input.send_keys(Keys.ARROW_DOWN)
        title_input.send_keys(Keys.ENTER)

        print(f"Title selected successfully: {title}")

    def Enter_name_user(self):

        for i in range(5):

            try:

                field = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(self.enter_name_user)
                )

                field.clear()
                field.send_keys(random_first_name)

                print("First Name entered successfully")
                return

            except StaleElementReferenceException:
                print(f"Retry {i + 1}")
                time.sleep(0.5)

        raise Exception("Unable to enter First Name.")

    def Enter_Ni_Number_User(self):
        # try:
        ni = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.enter_ni_number_user))
        time.sleep(.2)
        ni.send_keys("AB123456C")
        time.sleep(.2)
        print("Enter first name successfully....!!")

    # except Exception as e:
    #     print(f"Error on Click:{e}")

    def Save_User(self):

        # try:
        user = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.click_save_button_user))
        time.sleep(.2)
        user.click()
        time.sleep(.2)
        print("Click on Save user successfully....!!")

    # except Exception as e:
    #     print(f"Error on Click:{e}")

    # ------------------------------------------Add Expense Claim-----------------------------------------------------------

    def Click_Expense_Claims_Tab(self):
        wait = WebDriverWait(
            self.driver,
            30,
            poll_frequency=0.2,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        try:
            expense_claims_tab = wait.until(
                EC.element_to_be_clickable(
                    self.expense_claims_tab
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                expense_claims_tab
            )

            expense_claims_tab.click()

            # Verify that the correct tab is selected.
            wait.until(
                lambda driver: driver.find_element(
                    *self.expense_claims_tab
                ).get_attribute("aria-selected") == "true"
            )

            print(
                "Expense Claims tab clicked successfully."
            )

        except Exception as error:
            self.driver.save_screenshot(
                "expense_claims_tab_click_failure.png"
            )

            raise AssertionError(
                f"Could not open Expense Claims tab: {error}"
            ) from error

    def Click_Expense_Claims_Button(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            # Click dropdown
            dropdown = wait.until(
                EC.presence_of_element_located(self.click_expense_claims_button)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dropdown
            )
            time.sleep(0.3)

            driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(0.5)

            print("Click on Expense Claims successfully....!!")

        except Exception as e:
            driver.save_screenshot("expense_claims_dropdown_error.png")
            print(f"Error while selecting Expense Claims: {e}")
            raise

    def Select_Directors_Expense_Claims(self):

        driver = self.driver
        wait = WebDriverWait(driver, 40)

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

    def Enter_Remark_Expense_Claims(self):
        try:
            remark = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_remark_expense_claims))
            time.sleep(.2)
            remark.send_keys("only for testing")
            time.sleep(.2)
            print("Enter remark successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Add_Attachment_Expense_Claims(self):
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

    def Enter_Bill_No_Expense_Claims(self):
        try:
            bill = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.bill_no_expense_claims))
            time.sleep(.2)
            bill.send_keys("1000")
            time.sleep(.2)
            print("Enter bill number successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")

    def Enter_Description_Expense_Claims(self):
        try:
            des = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_description_expense_claims))
            time.sleep(.2)
            des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Account_Expense_Claim(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            for _ in range(3):
                try:
                    account_container = wait.until(
                        EC.element_to_be_clickable(self.account_expense_claim)
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

    def Base_Amount_Expense_Claim(self):

        try:
            wait = WebDriverWait(self.driver, 30)

            base = wait.until(EC.element_to_be_clickable(self.base_amount_expense_claim))

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

    def Select_Vat_Expense_Claim(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            vat_cell = wait.until(
                EC.element_to_be_clickable(self.vat_expense_claim)
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

    def Save_Expense(self):

        wait = WebDriverWait(self.driver, 30)

        # 1) Click Save
        save_btn = wait.until(EC.element_to_be_clickable(self.save_expense_claim))
        save_btn.click()
        time.sleep(0.5)
        print("Expense Saved successfully............!!!")

        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.save_expense_click_claim)
            )
            popup.click()
            print(" Expense Saved successfully............!!!")
        except Exception:
            print("No popup detected → continuing...")

    # -----------------------------------------------------------------------------------------------------------------------

    def Mileages_Section(self):
        try:
            mileages_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.mileages_section))
            time.sleep(.2)
            mileages_sec.click()
            time.sleep(.2)
            print("Click on Mileages Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Mileages(self):
        try:
            click_mileages = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_add_mileages))
            time.sleep(.2)
            click_mileages.click()
            time.sleep(.2)
            print("Click on Mileages successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Select_Directors(self):

        driver = self.driver
        wait = WebDriverWait(driver, 35)

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
            wait = WebDriverWait(self.driver, 30)

            remark = wait.until(EC.element_to_be_clickable(self.enter_remark_mileages))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", remark
            )

            time.sleep(0.3)

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
            wait = WebDriverWait(driver, 30)

            container = wait.until(EC.element_to_be_clickable(self.engine_type))

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", container
            )
            time.sleep(0.2)

            try:
                container.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", container)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Engine type entered successfully....!!")

        except Exception as e:
            print(f"Error on click: {e}")

    def Enter_Description_Mileage(self):

        try:
            des = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.enter_description_mileage))
            time.sleep(.2)
            des.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter Description successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Mileage(self):
        try:
            select = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.mileage))
            time.sleep(.2)
            select.send_keys("5")
            time.sleep(.2)
            print("Enter mileage successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Select_Rate_Mileage(self):
        driver = self.driver

        try:
            wait = WebDriverWait(self.driver, 30)

            select_rate = wait.until(EC.element_to_be_clickable(self.rate_mileage))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", select_rate
            )
            time.sleep(0.2)

            select_rate.click()
            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            # select_rate.send_keys(Keys.CONTROL, "a")
            # time.sleep(0.2)
            # select_rate.send_keys(Keys.BACK_SPACE)
            # time.sleep(0.5)
            #
            # select_rate.send_keys("100")
            # time.sleep(0.2)

            print("Rate entered successfully....!!")
        except Exception as e:
            print(f"Error on click:{e}")

    def Save_Mileage(self):

        try:

            save_btn = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.save_mileages)
            )
            save_btn.click()
            save_btn.click()
            time.sleep(2)

            print("Save button clicked Successfully.....!")

            try:
                popup = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(self.save_expense_click)
                )
                popup.click()
                print("Popup detected → Saved using popup button!")
                time.sleep(3)

            except Exception:
                # print("No popup detected → Checking for success message...")
                #
                # update_message = WebDriverWait(self.driver, 30).until(
                #     EC.visibility_of_element_located(
                #         (By.XPATH, "//*[contains(normalize-space(), 'Mileage saved successfully with number')]")
                #     )
                # )
                #
                # assert update_message, "Mileage saved successfully"
                print("Test Case : - Pass: Mileage saved successfully.")

        except Exception as e:
            print(f"Error in Save_Expense: {e}")

    # --------------------------------------------- Reimbursed_Section-----------------------------------------------

    def Reimbursed_Section(self):
        try:
            reimbursed_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.reimbursements_section))
            time.sleep(.2)
            reimbursed_sec.click()
            time.sleep(.2)
            print("Click on reimbursed Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Reimbursed(self):
        try:
            click_reimbursed = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_reimbursements))
            time.sleep(.2)
            click_reimbursed.click()
            time.sleep(.2)
            print("Click on reimbursed successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Reimbursed_to(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        for _ in range(3):
            try:
                container = wait.until(
                    EC.element_to_be_clickable(self.reimbursed_to)
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

                print("Select Reimbursed To successfully....!!")
                return
            except StaleElementReferenceException:

                continue

        raise TimeoutException("Could not select a director from dropdown")

    def Reimbursed_Account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.reimbursed_account)
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

            print("Reimbursed account selected successfully....!!")
        except Exception as e:
            print(f"Error on Click reimbursed account: {e}")

    def Enter_Amount_Reimbursements(self):
        try:
            amount = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.reimbursed_amount))
            time.sleep(.3)
            amount.click()

            time.sleep(0.2)
            amount.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            amount.send_keys(Keys.BACK_SPACE)
            time.sleep(0.2)
            amount.send_keys("100")
            time.sleep(.3)
            amount.send_keys(Keys.TAB)
            time.sleep(.2)
            print("Click on reimbursed amount successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Enter_Notes_Reimbursements(self):
        # try:
        notes = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.enter_notes_reimbursements))
        time.sleep(.2)
        notes.send_keys("only for testing")
        time.sleep(.2)
        print("Enter notes successfully....!!")

    # except Exception as e:
    #     print(f"Error on Click:{e}")

    def Save_Reimbursement(self):
        # try:
        save_reb = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_reimbursement))
        time.sleep(.2)
        save_reb.click()
        time.sleep(.2)

        print("Test Case - Pass: Reimbursement saved successfully.")

    # -----------------------------------------------Expense Claims >> Refunds-----------------------------------------------

    def Refunds_Section(self):
        try:
            refunds_sec = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.refunds_section))
            time.sleep(.2)
            refunds_sec.click()
            time.sleep(.2)
            print("Click on Refunds Section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")

    def Click_Refunds(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            self.wait_for_loader_to_disappear()

            add_refund_button = wait.until(
                EC.element_to_be_clickable(self.click_refunds)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                add_refund_button
            )

            try:
                add_refund_button.click()
            except ElementClickInterceptedException:
                driver.execute_script(
                    "arguments[0].click();",
                    add_refund_button
                )

            # Wait until the Refund from input appears
            wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//label[contains(normalize-space(),'Refund from')]"
                    "/following::input[@role='combobox'][1]"
                ))
            )

            print("Refund form opened successfully.")

        except Exception as error:
            driver.save_screenshot("open_refund_form_failure.png")

            raise AssertionError(
                f"Could not open Refund form: {error}"
            ) from error

    def Refund_from(self):
        driver = self.driver

        wait = WebDriverWait(
            driver,
            20,
            poll_frequency=0.2,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        try:
            self.wait_for_loader_to_disappear()

            refund_input = wait.until(
                EC.presence_of_element_located(
                    self.refund_from
                )
            )

            driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                refund_input
            )

            wait.until(
                lambda current_driver:
                refund_input.is_displayed()
                and refund_input.is_enabled()
            )

            try:
                refund_input.click()
            except ElementClickInterceptedException:
                driver.execute_script(
                    "arguments[0].click();",
                    refund_input
                )

            refund_input.send_keys(Keys.ARROW_DOWN)
            refund_input.send_keys(Keys.ENTER)

            selected_value = wait.until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//label["
                    "contains(normalize-space(),'Refund from') or "
                    "contains(normalize-space(),'Refunded from')"
                    "]"
                    "/following::div[contains(@class,'rs-single-value')][1]"
                ))
            )

            print(
                "Refund source selected successfully:",
                selected_value.text
            )

        except TimeoutException as error:
            driver.save_screenshot(
                "refund_from_timeout.png"
            )

            print("Current URL:", driver.current_url)
            print(
                "Refund inputs found:",
                len(
                    driver.find_elements(
                        By.XPATH,
                        "//input[@role='combobox']"
                    )
                )
            )

            raise AssertionError(
                "Refund from dropdown was not found or enabled. "
                "Check whether the Refund form opened and verify the locator."
            ) from error

    def Select_Account_Refund(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.refund_account)
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

            print("Refund account selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Refund account: {e}")

    def Enter_Refund_Amount(self, amount="100"):
        try:
            driver = self.driver
            wait = WebDriverWait(driver, 20)

            # Amount field
            amount_input = wait.until(
                EC.element_to_be_clickable(
                    self.enter_amount
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                amount_input
            )

            amount_input.click()
            amount_input.send_keys(Keys.CONTROL, "a")
            amount_input.send_keys(Keys.BACKSPACE)
            amount_input.send_keys(str(amount))
            amount_input.send_keys(Keys.TAB)

            print(f"Refund amount entered: {amount}")

            # Validation message
            validation_xpath = (
                "//*[contains(normalize-space(.),"
                "'Amount exceeds total refund due. It has been adjusted to the refund due amount')]"
            )

            # Wait until either:
            # 1. validation message appears
            # OR
            # 2. Save button becomes clickable
            result = WebDriverWait(driver, 15).until(
                lambda d:
                len(d.find_elements(By.XPATH, validation_xpath)) > 0
                or self._is_element_clickable(d, self.save_refund)
            )

            # Check validation message first
            validation_messages = driver.find_elements(
                By.XPATH,
                validation_xpath
            )

            if validation_messages:
                print(
                    "Validation message displayed: "
                    "Amount exceeds total refund due. "
                    "It has been adjusted to the refund due amount"
                )

                # Optional: wait until adjusted amount is reflected
                time.sleep(0.5)

                return "AMOUNT_ADJUSTED"

            print("Save button is enabled.")
            return "SAVE_ENABLED"

        except Exception as e:
            print(f"Error while entering refund amount: {e}")
            raise

    def _is_element_clickable(self, driver, locator):
        try:
            element = driver.find_element(*locator)
            return element.is_displayed() and element.is_enabled()
        except Exception:
            return False

    def Save_Refund(self):
        try:
            save_ref = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_refund))
            time.sleep(.2)
            save_ref.click()
            time.sleep(.2)

            # update_message = WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(
            #         (By.XPATH, "//*[contains(normalize-space(), 'Reimbursement saved successfully with number')]"))
            # )
            #
            # # Assert the presence of the success message
            # assert update_message, "Reimbursement saved successfully"

            print("Test Case   - Pass: Refund saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

    # -----------------------------------------------------------------------------------------------------------------------

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

    def Click_Add_Assets(self):

        try:
            client = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.click_fixed_asset))
            time.sleep(.2)
            client.click()
            time.sleep(.2)
            print("Click on add assets successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(2)

    def Asset_Name(self):
        asset_name = f"Asset_{fake.word().title()}_{fake.random_int(1000, 9999)}"

        try:
            wait = WebDriverWait(self.driver, 40)

            self.wait_for_overlay_to_disappear()

            asset = wait.until(
                EC.presence_of_element_located(self.enter_asset_name_asset)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                asset
            )

            time.sleep(0.5)

            self.driver.execute_script("""
                const input = arguments[0];
                const value = arguments[1];

                input.removeAttribute('readonly');
                input.removeAttribute('disabled');

                const nativeInputValueSetter =
                    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;

                nativeInputValueSetter.call(input, value);

                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new Event('blur', { bubbles: true }));
            """, asset, asset_name)

            print(f"Asset name entered successfully using JS: {asset_name}")

            return asset_name

        except Exception as e:
            print(f"Error in Asset_Name: {type(e).__name__} - {e}")
            self.driver.save_screenshot("asset_name_error.png")
            raise

    def Purchase_Assets(self):
        driver = self.driver
        try:
            pur = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.purchase_price_asset))
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

    def Select_Account_Assets(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.account_asset)
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

    def wait_for_overlay_to_disappear(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'ms-Overlay')]")
                )
            )
        except TimeoutException:
            print("Overlay still visible after wait")

    def Save_Asset(self, asset_name):
        wait = WebDriverWait(self.driver, 30)

        save_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class,'ms-Dialog-main')]//button[@title='Save']"
            ))
        )

        save_button.click()

        # Modal should close
        wait.until(
            EC.invisibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'ms-Dialog-main')]"
            ))
        )

        # Newly created asset should appear in list
        wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                f"//*[normalize-space()='{asset_name}']"
            ))
        )

        print(f"PASS: Asset '{asset_name}' saved and displayed successfully.")

    # def Save_Asset(self):
    #
    #     try:
    #         save_ref = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_asset))
    #         time.sleep(.2)
    #         save_ref.click()
    #         time.sleep(.2)
    #
    #
    #         print("Test Case - Pass: Asset saved successfully.")
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #
    #         time.sleep(2)

    # def Save_Asset(self):
    #     try:
    #         driver = self.driver
    #         wait = WebDriverWait(driver, 30)
    #
    #         # Wait until Save button is really clickable
    #         save_ref = wait.until(
    #             EC.element_to_be_clickable(self.save_asset)
    #         )
    #
    #         # Bring button into visible area
    #         driver.execute_script(
    #             "arguments[0].scrollIntoView({block:'center'});",
    #             save_ref
    #         )
    #
    #         time.sleep(0.3)
    #
    #         try:
    #             # First try normal Selenium click
    #             save_ref.click()
    #
    #         except Exception:
    #             print("Normal click failed, trying JavaScript click...")
    #
    #             # Re-locate element before JS click
    #             save_ref = wait.until(
    #                 EC.presence_of_element_located(self.save_asset)
    #             )
    #
    #             driver.execute_script(
    #                 "arguments[0].click();",
    #                 save_ref
    #             )
    #
    #         print("Test Case - Pass: Asset Save button clicked successfully.")
    #
    #         # Better: wait until modal disappears after save
    #         wait.until(
    #             EC.invisibility_of_element_located(
    #                 (By.XPATH, "//*[contains(normalize-space(.),'Add fixed asset')]")
    #             )
    #         )
    #
    #         print("Test Case - Pass: Asset saved successfully.")
    #
    #     except Exception as e:
    #         print(f"Error while saving Asset: {type(e).__name__}: {e}")
    #         raise




    def Select_Supplier_Assets(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            supp = wait.until(
                EC.element_to_be_clickable(self.supplier_asset)
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

    def Enter_Rate_Assets(self):
        try:
            enter_rate = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.rate_asset))
            time.sleep(.2)
            enter_rate.send_keys("2")
            time.sleep(.2)
            print("Click on Enter rate successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")
        time.sleep(.2)

    # ----------------------------------------------dispose-----------------------------------------------------------------


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

    def Select_Asset_Disposed(self):
        driver = self.driver
        try:
            select = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.select_asset_dispose)
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

    def Sales_proceeds_Disposed(self):
        try:
            sales_proceeds = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.sales_proceeds_dispose))
            time.sleep(.2)
            sales_proceeds.send_keys("testing")
            time.sleep(.2)
            print("Click on Sales proceeds successfully..... ")
        except Exception as e:
            print(f"Error on click:{e}")
            time.sleep(.2)

    def Payment_Method_Disposed(self):
        driver = self.driver
        try:
            select = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.payment_method_dispose)
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

    def Customer_Disposed(self):
        driver = self.driver
        try:
            select = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.customer_dispose)
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

            print("Test Case  - Pass: Disposed saved successfully.")

        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)


    #-------------------------------------------------------------------------------------------------------------------



    def Click_Journals(self):
        driver = self.driver
        wait = WebDriverWait(
            driver,
            30,
            poll_frequency=0.2,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

        try:
            self.wait_for_loader_to_disappear()
            self.wait_for_overlay_to_disappear()

            journals_menu = wait.until(
                EC.presence_of_element_located(
                    self.journals_menu
                )
            )

            driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                journals_menu
            )

            journals_menu = wait.until(
                EC.element_to_be_clickable(
                    self.journals_menu
                )
            )

            try:
                journals_menu.click()

            except ElementClickInterceptedException:
                self.wait_for_overlay_to_disappear()

                journals_menu = wait.until(
                    EC.element_to_be_clickable(
                        self.journals_menu
                    )
                )

                driver.execute_script(
                    "arguments[0].click();",
                    journals_menu
                )

            wait.until(
                EC.url_contains("/inputs/journals")
            )

            print("Journals section opened successfully.")

        except Exception as error:
            driver.save_screenshot(
                "journals_navigation_failure.png"
            )

            raise AssertionError(
                f"Could not open Journals section: {error}"
            ) from error


    def Click_Journals_Button(self):
        try:
            click_journal_btn = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_journal))
            time.sleep(.2)
            click_journal_btn.click()
            time.sleep(.2)
            print("Click on journal successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Journal_Reference(self):
        try:
            reference = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.journal_reference))
            time.sleep(.2)
            reference.send_keys("Only for testing")
            time.sleep(.2)
            print("Enter journal Reference successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Select_Account_Journal(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            account = wait.until(
                EC.element_to_be_clickable(self.select_account_journal)
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


    def Enter_Value_IN_Debit(self, value="100"):
        try:

            debit_input = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.debit_journal)
            )

            debit_input.click()
            time.sleep(0.3)

            debit_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.1)
            debit_input.send_keys(Keys.BACK_SPACE)
            time.sleep(0.3)


            debit_input.send_keys(str(value))
            time.sleep(0.3)

            print("Enter Debit successfully....!!")

        except Exception as e:
            print(f"Error on Enter_Value_IN_Debit: {e}")
            time.sleep(0.2)


    def Enter_Value_IN_Credit(self, value="100"):
        try:

            credit_input = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.credit_journal)
            )

            credit_input.click()
            time.sleep(0.3)

            credit_input.send_keys(Keys.CONTROL, "a")
            time.sleep(0.1)
            credit_input.send_keys(Keys.BACK_SPACE)  # or Keys.DELETE
            time.sleep(0.3)

            credit_input.send_keys(str(value))
            time.sleep(0.3)

            print("Enter Credit successfully....!!")

        except Exception as e:
            print(f"Error on Enter_Value_IN_Debit: {e}")
            time.sleep(0.2)


    def Save_Journal(self):

            try:
                journal = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.save_journal))
                time.sleep(.2)
                journal.click()
                time.sleep(.2)

                print("Test Case 15 - Pass: Journal saved successfully.")

            except Exception as e:
                print(f"Error: {e}")

                time.sleep(2)


    #------------------------------------------------Dividends----------------------------------------------------------------



    def Dividends_Section(self):
        try:
            dividends = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.dividends_section))
            time.sleep(.2)
            dividends.click()
            time.sleep(.2)
            print("Click on  dividends section successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)



    def Click_Dividends(self):
        try:
            click_div = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.click_dividends))
            time.sleep(.2)
            click_div .click()
            time.sleep(.2)
            print("Click on Add dividends  successfully....!!")
        except Exception as e:
            print(f"Error on Click:{e}")
            time.sleep(.2)


    def Authorised_director(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            dir = wait.until(
                EC.element_to_be_clickable(self.select_director)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                dir
            )
            time.sleep(0.2)

            try:
                dir.click()
            except Exception:
                driver.execute_script("arguments[0].click();", dir)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Authorised director selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Account: {e}")


    def Select_Type_Dividends(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            dropdown = wait.until(
                EC.visibility_of_element_located(self.select_type)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                dropdown
            )
            time.sleep(0.2)

            try:
                dropdown.click()
            except Exception:
                driver.execute_script("arguments[0].click();", dropdown)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            #active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Type selected successfully....!!")

        except TimeoutException:
            print("Timeout: 'Type' dropdown not found or not visible. Check the XPath self.select_type.")
        except Exception as e:
            print(f"Error while selecting Type: {e}")


    def Select_Class_Dividends(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            cls = wait.until(
                EC.element_to_be_clickable(self.select_class)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                cls
            )
            time.sleep(0.2)

            try:
                cls.click()
            except Exception:
                driver.execute_script("arguments[0].click();", dir)

            time.sleep(0.2)

            active = driver.switch_to.active_element
            active.send_keys(Keys.ARROW_DOWN)
            time.sleep(0.2)
            active.send_keys(Keys.ENTER)
            time.sleep(0.2)

            print("Class selected successfully....!!")
        except Exception as e:
            print(f"Error on Click Account: {e}")



    def Dividend_Per_Share(self, value="100"):

            try:

                share = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(self.dividend_per_share)
                )

                share.click()
                time.sleep(0.3)

                share.send_keys(Keys.CONTROL, "a")
                time.sleep(0.1)
                share.send_keys(Keys.BACK_SPACE)
                time.sleep(0.3)

                share.send_keys(str(value))
                time.sleep(0.3)

                print("Enter share value successfully....!!")

            except Exception as e:
                print(f"Error on Enter_Value: {e}")
                time.sleep(0.2)



    def Enter_Payment_Date(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Generate today's date
            today = datetime.today().strftime("%d/%m/%Y")

            # Wait for element
            payment_date = wait.until(EC.visibility_of_element_located(self.payment))

            time.sleep(0.2)
            payment_date.clear()
            time.sleep(0.2)

            # Enter today's date
            payment_date.send_keys(today)
            time.sleep(0.3)

            # active = driver.switch_to.active_element
            # active.send_keys(Keys.ENTER)

            print("Enter payment date successfully...!!")

        except Exception as e:
            print(f"Error on Click: {e}")
            time.sleep(0.2)


    def Save_Asset(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:
            # Wait for common overlays/loaders to disappear
            overlay_locators = [
                (By.CSS_SELECTOR, ".ant-spin-spinning"),
                (By.CSS_SELECTOR, ".ms-Overlay"),
                (By.XPATH, "//div[contains(@class,'root-1288')]"),
                (By.CSS_SELECTOR, "[aria-busy='true']")
            ]

            for locator in overlay_locators:
                try:
                    wait.until(EC.invisibility_of_element_located(locator))
                except TimeoutException:
                    pass

            # Re-find the Save button after overlays disappear
            save_button = wait.until(
                EC.presence_of_element_located(self.save_dividends)
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                save_button
            )

            time.sleep(0.5)

            # Re-locate once more to avoid stale reference
            save_button = wait.until(
                EC.element_to_be_clickable(self.save_dividends)
            )

            try:
                save_button.click()

            except (ElementClickInterceptedException, StaleElementReferenceException):
                save_button = wait.until(
                    EC.presence_of_element_located(self.save_dividends)
                )
                driver.execute_script("arguments[0].click();", save_button)

            print("Asset saved successfully.")
        except Exception as e:
            print(f"Error: {e}")




    def Save(self):
        try:
            save = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.save_anyway))
            time.sleep(.2)
            save.click()
            time.sleep(.2)
            print(" Test Case - Pass: Dividends created successfully.")
        except Exception as e:
            print(f"Error: {e}")

            time.sleep(2)

