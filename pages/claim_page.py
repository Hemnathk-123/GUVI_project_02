"""
Claim Page Object

This module contains the Claim page object with methods for
claim management operations in OrangeHRM.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ClaimPage(BasePage):
    """
    Page object for OrangeHRM Claim page.
    Handles Claim operations including submitting claims.
    """
    
    # Menu items
    SUBMIT_CLAIM_MENU = (By.XPATH, "//a[text()='Submit Claim']")
    MY_CLAIMS_MENU = (By.XPATH, "//a[text()='My Claims']")
    
    # Submit Claim Form
    CLAIM_TYPE_DROPDOWN = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    AMOUNT_INPUT = (By.CSS_SELECTOR, "input.oxd-input[type='number']")
    REMARKS_TEXTAREA = (By.CSS_SELECTOR, "textarea.oxd-textarea")
    SUBMIT_BUTTON = (By.CLASS_NAME, "oxd-button--secondary")
    
    # Success message
    SUCCESS_MESSAGE = (By.CLASS_NAME, "oxd-alert-content-text")
    
    def __init__(self, driver, logger):
        """Initialize the Claim page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized ClaimPage")
    
    def navigate_to_submit_claim(self):
        """Navigate to Submit Claim section."""
        self.click(self.SUBMIT_CLAIM_MENU)
        self.logger.info("Clicked Submit Claim")
        self.wait_for_page_load()
    
    def select_claim_type(self, claim_type):
        """Select claim type."""
        self.click(self.CLAIM_TYPE_DROPDOWN)
        time.sleep(1)
        
        js_code = f"""
        var options = document.querySelectorAll('[class*="oxd-select-option"]');
        for(var i=0; i<options.length; i++) {{
            if(options[i].textContent.includes('{claim_type}')) {{
                options[i].click();
                return 'success';
            }}
        }}
        return 'not_found';
        """
        self.driver.execute_script(js_code)
        self.logger.info(f"Selected claim type: {claim_type}")
    
    def enter_amount(self, amount):
        """Enter claim amount."""
        self.type_text(self.AMOUNT_INPUT, str(amount))
        self.logger.info(f"Entered amount: {amount}")
    
    def enter_remarks(self, remarks):
        """Enter remarks."""
        self.type_text(self.REMARKS_TEXTAREA, remarks)
        self.logger.info("Entered remarks")
    
    def click_submit(self):
        """Click submit button."""
        self.click(self.SUBMIT_BUTTON)
        self.logger.info("Clicked Submit button")
        time.sleep(3)
    
    def is_success_message_visible(self):
        """Check if success message is visible."""
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    def get_success_message(self):
        """Get success message text."""
        if self.is_success_message_visible():
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
    
    def submit_claim(self, claim_type, amount, remarks):
        """Submit a claim with all details."""
        self.select_claim_type(claim_type)
        self.enter_amount(amount)
        self.enter_remarks(remarks)
        self.click_submit()
        self.logger.info(f"Claim submitted: {claim_type} - {amount}")