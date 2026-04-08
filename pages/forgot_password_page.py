"""
Forgot Password Page Object

This module contains the Forgot Password page object with methods for
resetting password in OrangeHRM.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ForgotPasswordPage(BasePage):
    """
    Page object for OrangeHRM Forgot Password page.
    Handles password reset functionality.
    """
    
    USERNAME_INPUT = (By.NAME, "username")
    CANCEL_BUTTON = (By.CLASS_NAME, "oxd-button--ghost")
    RESET_BUTTON = (By.CLASS_NAME, "oxd-button--secondary")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "oxd-alert-content-text")
    
    def __init__(self, driver, logger):
        """Initialize the Forgot Password page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized ForgotPasswordPage")
    
    def enter_username(self, username):
        """Enter username for password reset."""
        self.type_text(self.USERNAME_INPUT, username)
        self.logger.info(f"Entered username: {username}")
    
    def click_reset_password(self):
        """Click reset password button."""
        self.click(self.RESET_BUTTON)
        self.logger.info("Clicked Reset Password button")
        time.sleep(3)
    
    def click_cancel(self):
        """Click cancel button."""
        self.click(self.CANCEL_BUTTON)
        self.logger.info("Clicked Cancel button")
        self.wait_for_page_load()
    
    def is_success_message_visible(self):
        """Check if success message is visible."""
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    def get_success_message(self):
        """Get success message text."""
        if self.is_success_message_visible():
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
    
    def reset_password(self, username):
        """Reset password for given username."""
        self.enter_username(username)
        self.click_reset_password()
        self.logger.info(f"Password reset requested for: {username}")