"""
Login Page Object

This module contains the login page object with methods for
interacting with the OrangeHRM login page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page object for OrangeHRM Login page.
    Handles all login-related operations and validations.
    """
    
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "oxd-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "oxd-alert-content-text")
    DASHBOARD_HEADER = (By.CLASS_NAME, "oxd-topbar-header")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot your password?")
    
    def __init__(self, driver, logger):
        """Initialize the login page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized LoginPage")
    
    def navigate_to_login(self):
        """Navigate to the OrangeHRM login page."""
        from conftest import TestConfig
        self.navigate_to(TestConfig.BASE_URL)
        self.logger.info("Navigated to login page")
    
    def enter_username(self, username):
        """Enter username in the username field."""
        self.type_text(self.USERNAME_INPUT, username)
        self.logger.info(f"Entered username: {username}")
    
    def enter_password(self, password):
        """Enter password in the password field."""
        self.type_text(self.PASSWORD_INPUT, password)
        self.logger.info("Entered password")
    
    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)
        self.logger.info("Clicked login button")
        self.wait_for_page_load()
    
    def login(self, username, password):
        """
        Perform complete login operation.
        
        Args:
            username: Username for authentication
            password: Password for authentication
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.logger.info(f"Login attempted with username: {username}")
    
    def get_error_message(self):
        """Get the error message displayed on login failure."""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def is_login_successful(self):
        """Check if login was successful."""
        import time
        time.sleep(2)
        
        if self.is_element_visible(self.ERROR_MESSAGE):
            error_text = self.get_text(self.ERROR_MESSAGE)
            self.logger.warning(f"Login failed with error: {error_text}")
            return False
        
        if self.is_element_visible(self.DASHBOARD_HEADER):
            return True
        
        current_url = self.driver.current_url
        if "dashboard" in current_url.lower():
            return True
        
        return False
    
    def is_login_page_displayed(self):
        """Check if login page is displayed."""
        return (self.is_element_visible(self.USERNAME_INPUT) and 
                self.is_element_visible(self.PASSWORD_INPUT) and
                self.is_element_visible(self.LOGIN_BUTTON))
    
    def click_forgot_password(self):
        """Click on forgot password link."""
        self.click(self.FORGOT_PASSWORD_LINK)
        self.logger.info("Clicked forgot password link")