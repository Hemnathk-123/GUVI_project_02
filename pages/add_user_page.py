"""
Add User Page Object

This module contains the Add User page object with methods for
creating new users in OrangeHRM.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class AddUserPage(BasePage):
    """
    Page object for OrangeHRM Add User page.
    Handles new user creation form.
    """
    
    # Form elements
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Type for hints']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input.oxd-input:not([placeholder*='Type for hints']):not([placeholder='Search'])")
    PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[2]")
    STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[2]")
    SAVE_BUTTON = (By.CLASS_NAME, "oxd-button--secondary")
    
    def __init__(self, driver, logger):
        """Initialize the Add User page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized AddUserPage")
    
    def select_user_role(self, role):
        """Select user role from dropdown."""
        self.click(self.USER_ROLE_DROPDOWN)
        time.sleep(1)
        
        js_code = f"""
        var options = document.querySelectorAll('[class*="oxd-select-option"]');
        for(var i=0; i<options.length; i++) {{
            if(options[i].textContent.includes('{role}')) {{
                options[i].click();
                return 'success';
            }}
        }}
        return 'not_found';
        """
        result = self.driver.execute_script(js_code)
        self.logger.info(f"Selected user role: {role}")
    
    def enter_employee_name(self, name):
        """Enter employee name in autocomplete field."""
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
        time.sleep(3)
        
        js_click = """
        var option = document.querySelector('[class*="oxd-autocomplete-option"]');
        if(option) { option.click(); return 'success'; }
        return 'not_found';
        """
        self.driver.execute_script(js_click)
        self.logger.info(f"Entered employee name: {name}")
    
    def enter_username(self, username):
        """Enter username."""
        js_code = """
        var inputs = document.querySelectorAll('.oxd-input');
        for(var i=0; i<inputs.length; i++) {
            var ph = inputs[i].getAttribute('placeholder') || '';
            if(!ph.includes('Type for hints') && !ph.includes('Search')) {
                inputs[i].value = arguments[0];
                inputs[i].dispatchEvent(new Event('input', {bubbles: true}));
                return 'success';
            }
        }
        return 'not_found';
        """
        self.driver.execute_script(js_code, username)
        self.logger.info(f"Entered username: {username}")
    
    def select_status(self, status):
        """Select user status."""
        self.click(self.STATUS_DROPDOWN)
        time.sleep(1)
        
        js_code = f"""
        var options = document.querySelectorAll('[class*="oxd-select-option"]');
        for(var i=0; i<options.length; i++) {{
            if(options[i].textContent.includes('{status}')) {{
                options[i].click();
                return 'success';
            }}
        }}
        return 'not_found';
        """
        result = self.driver.execute_script(js_code)
        self.logger.info(f"Selected status: {status}")
    
    def enter_password(self, password):
        """Enter password."""
        js_code = """
        var inputs = document.getElementsByTagName('input');
        for(var i=3; i<10; i++) {
            var ph = inputs[i].getAttribute('placeholder') || '';
            if(ph !== 'Search' && !ph.includes('Type for hints') && !ph.includes('Username')) {
                inputs[i].value = arguments[0];
                inputs[i].dispatchEvent(new Event('input', {bubbles: true}));
                return 'found';
            }
        }
        return 'not_found';
        """
        self.driver.execute_script(js_code, password)
        self.logger.info("Entered password")
    
    def enter_confirm_password(self, password):
        """Enter confirm password."""
        js_code = """
        var inputs = document.getElementsByTagName('input');
        for(var i=4; i<10; i++) {
            var ph = inputs[i].getAttribute('placeholder') || '';
            if(ph !== 'Search' && !ph.includes('Type for hints')) {
                if(!inputs[i].value) {
                    inputs[i].value = arguments[0];
                    inputs[i].dispatchEvent(new Event('input', {bubbles: true}));
                    return 'found';
                }
            }
        }
        return 'not_found';
        """
        self.driver.execute_script(js_code, password)
        self.logger.info("Entered confirm password")
    
    def click_save(self):
        """Click save button."""
        self.driver.execute_script("document.querySelector('form.oxd-form').submit();")
        time.sleep(5)
        self.logger.info("Clicked save button")
    
    def create_user(self, employee_name, username, password, user_role="Admin", status="Enabled"):
        """Create a new user with all fields."""
        self.select_user_role(user_role)
        self.enter_employee_name(employee_name)
        self.enter_username(username)
        self.select_status(status)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_save()
        self.logger.info(f"User {username} created")