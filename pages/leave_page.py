"""
Leave Page Object

This module contains the Leave page object with methods for
leave management operations in OrangeHRM.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LeavePage(BasePage):
    """
    Page object for OrangeHRM Leave page.
    Handles Leave operations including assigning leave.
    """
    
    # Menu items
    ASSIGN_LEAVE_MENU = (By.XPATH, "//a[text()='Assign Leave']")
    LEAVE_LIST_MENU = (By.XPATH, "//a[text()='Leave List']")
    LEAVE_ENTITLEMENTS_MENU = (By.XPATH, "//a[text()='Leave Entitlements']")
    REPORTS_MENU = (By.XPATH, "//a[text()='Leave Reports']")
    CONFIGURE_MENU = (By.XPATH, "//a[text()='Configure']")
    
    # Assign Leave Form
    EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Type for hints']")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    FROM_DATE = (By.CSS_SELECTOR, "input.oxd-input[type='date']")
    TO_DATE = (By.CSS_SELECTOR, "input.oxd-input[type='date']")
    ASSIGN_BUTTON = (By.CLASS_NAME, "oxd-button--secondary")
    
    def __init__(self, driver, logger):
        """Initialize the Leave page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized LeavePage")
    
    def navigate_to_assign_leave(self):
        """Navigate to Assign Leave section."""
        self.click(self.ASSIGN_LEAVE_MENU)
        self.logger.info("Clicked Assign Leave")
        self.wait_for_page_load()
    
    def enter_employee_name(self, name):
        """Enter employee name."""
        js_code = """
        var input = document.querySelector('input[placeholder*="Type for hints"]');
        if(input) {
            input.value = arguments[0];
            input.dispatchEvent(new Event('input', {bubbles: true}));
            return 'typed';
        }
        return 'not_found';
        """
        self.driver.execute_script(js_code, name)
        time.sleep(2)
        
        js_click = """
        var option = document.querySelector('[class*="oxd-autocomplete-option"]');
        if(option) { option.click(); return 'success'; }
        return 'not_found';
        """
        self.driver.execute_script(js_click)
        self.logger.info(f"Entered employee name: {name}")
    
    def select_leave_type(self, leave_type):
        """Select leave type."""
        self.click(self.LEAVE_TYPE_DROPDOWN)
        time.sleep(1)
        
        js_code = f"""
        var options = document.querySelectorAll('[class*="oxd-select-option"]');
        for(var i=0; i<options.length; i++) {{
            if(options[i].textContent.includes('{leave_type}')) {{
                options[i].click();
                return 'success';
            }}
        }}
        return 'not_found';
        """
        self.driver.execute_script(js_code)
        self.logger.info(f"Selected leave type: {leave_type}")
    
    def enter_from_date(self, date):
        """Enter from date."""
        js_code = """
        var inputs = document.querySelectorAll('input.oxd-input[type="date"]');
        if(inputs.length > 0) { inputs[0].value = arguments[0]; return 'success'; }
        return 'not_found';
        """
        self.driver.execute_script(js_code, date)
        self.logger.info(f"Entered from date: {date}")
    
    def enter_to_date(self, date):
        """Enter to date."""
        js_code = """
        var inputs = document.querySelectorAll('input.oxd-input[type="date"]');
        if(inputs.length > 1) { inputs[1].value = arguments[0]; return 'success'; }
        return 'not_found';
        """
        self.driver.execute_script(js_code, date)
        self.logger.info(f"Entered to date: {date}")
    
    def click_assign(self):
        """Click assign button."""
        self.click(self.ASSIGN_BUTTON)
        self.logger.info("Clicked Assign button")
        time.sleep(3)
    
    def assign_leave(self, employee_name, leave_type, from_date, to_date):
        """Assign leave with all details."""
        self.enter_employee_name(employee_name)
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        self.click_assign()
        self.logger.info(f"Leave assigned for {employee_name}")