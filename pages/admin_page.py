"""
Admin Page Object

This module contains the admin page object with methods for
user management operations in OrangeHRM.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class AdminPage(BasePage):
    """
    Page object for OrangeHRM Admin page.
    Handles User Management operations.
    """
    
    MENU_USER_MANAGEMENT = (By.XPATH, "//span[text()='User Management']")
    MENU_USERS = (By.XPATH, "//a[text()='Users']")
    
    ADD_BUTTON = (By.CLASS_NAME, "oxd-button--secondary")
    DELETE_BUTTON = (By.CLASS_NAME, "oxd-button--danger")
    SEARCH_BUTTON = (By.CLASS_NAME, "oxd-button--secondary")
    RESET_BUTTON = (By.CLASS_NAME, "oxd-button--ghost")
    
    SEARCH_USERNAME = (By.CSS_SELECTOR, "input.oxd-input[placeholder='Username']")
    SEARCH_EMPLOYEE = (By.CSS_SELECTOR, "input.oxd-input[placeholder='Employee Name']")
    
    TABLE_RESULT = (By.CSS_SELECTOR, ".oxd-table-body")
    TABLE_ROWS = (By.CSS_SELECTOR, ".oxd-table-row")
    
    def __init__(self, driver, logger):
        """Initialize the admin page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized AdminPage")
    
    def navigate_to_user_management(self):
        """Navigate to User Management section."""
        self.click(self.MENU_USER_MANAGEMENT)
        self.logger.info("Clicked User Management menu")
        self.wait_for_page_load()
    
    def navigate_to_users(self):
        """Navigate to Users section."""
        self.click(self.MENU_USERS)
        self.logger.info("Clicked Users menu")
        self.wait_for_page_load()
    
    def navigate_to_users_page(self):
        """Navigate directly to users page via URL."""
        from conftest import TestConfig
        self.navigate_to(f"{TestConfig.BASE_URL}/web/index.php/admin/viewSystemUsers")
        self.logger.info("Navigated to User Management page")
    
    def click_add_button(self):
        """Click Add button to create new user."""
        self.click(self.ADD_BUTTON)
        self.logger.info("Clicked Add button")
        self.wait_for_page_load()
    
    def search_by_username(self, username):
        """Search users by username."""
        time.sleep(3)
        
        js_code = """
        var inputs = document.querySelectorAll('input[placeholder="Username"]');
        for(var i = 0; i < inputs.length; i++) {
            var rect = inputs[i].getBoundingClientRect();
            if(rect.width > 0 && rect.height > 0) {
                inputs[i].value = arguments[0];
                inputs[i].dispatchEvent(new Event('input', {bubbles: true}));
                return 'success';
            }
        }
        return 'not_found';
        """
        result = self.driver.execute_script(js_code, username)
        
        if result == 'success':
            self.logger.info(f"Entered username to search: {username}")
        else:
            self.logger.error(f"Could not find username search field")
    
    def click_search_button(self):
        """Click Search button."""
        time.sleep(2)
        
        js_search = """
        var buttons = document.querySelectorAll('button.oxd-button');
        for(var i = 0; i < buttons.length; i++) {
            var text = buttons[i].textContent.trim().toLowerCase();
            if(text === 'search') {
                buttons[i].click();
                return 'success';
            }
        }
        return 'not_found';
        """
        self.driver.execute_script(js_search)
        self.logger.info("Clicked Search button")
        time.sleep(5)
    
    def search_user(self, username):
        """Search for user by username."""
        self.search_by_username(username)
        self.click_search_button()
    
    def get_user_count(self):
        """Get count of users in the table."""
        try:
            rows = self.find_elements(self.TABLE_ROWS)
            return len(rows)
        except:
            return 0
    
    def is_user_list_visible(self):
        """Check if user list table is visible."""
        return self.is_element_visible(self.TABLE_RESULT)
    
    def is_user_present(self, username):
        """Check if user is present in the user list."""
        time.sleep(3)
        
        js_find = """
        var cells = document.querySelectorAll('.oxd-table-cell, td');
        for(var j = 0; j < cells.length; j++) {
            if(cells[j].textContent.trim() === arguments[0]) {
                return 'found';
            }
        }
        return 'not_found';
        """
        result = self.driver.execute_script(js_find, username)
        return result == 'found'