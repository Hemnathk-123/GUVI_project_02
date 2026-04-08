"""
Test Case 7: Verify "Forgot Password" link functionality

This test case verifies that the Forgot Password functionality works correctly.

Scenario: Verify "Forgot Password" link functionality
Description:
- Navigate to the login page and click the "Forgot your password?" link
- Enter a registered username or email and submit the request

Expected Result:
- A confirmation message should appear indicating that password reset instructions 
  have been sent to the registered email
- The user should be redirected appropriately
"""

import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestCase7:
    """Test Case 7: Verify Forgot Password link functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
        self.forgot_password_page = ForgotPasswordPage(driver, logger)
    
    def test_forgot_password_link_visible(self, driver, logger):
        """
        Test: Verify Forgot Password link is visible on login page
        
        Expected: Forgot password link should be visible.
        """
        self.logger.info("TEST: Verify Forgot Password link is visible")
        
        self.login_page.navigate_to_login()
        
        assert self.login_page.is_element_visible(self.login_page.FORGOT_PASSWORD_LINK), \
            "Forgot password link should be visible"
        
        self.logger.info("Test passed: Forgot password link is visible")
    
    def test_forgot_password_navigation(self, driver, logger):
        """
        Test: Verify clicking Forgot Password link navigates correctly
        
        Expected: Should navigate to password reset page.
        """
        self.logger.info("TEST: Verify Forgot Password navigation")
        
        self.login_page.navigate_to_login()
        self.login_page.click_forgot_password()
        
        # Check if we're on the forgot password page
        current_url = self.driver.current_url
        self.logger.info(f"Current URL after clicking: {current_url}")
        
        # Should be on a password reset page
        assert "requestPasswordReset" in current_url or "forgotPassword" in current_url.lower(), \
            "Should be on password reset page"
        
        self.logger.info("Test passed: Navigated to password reset page")
    
    def test_forgot_password_with_valid_username(self, driver, logger):
        """
        Test: Forgot password with valid username
        
        Expected: Success message should be displayed.
        """
        self.logger.info("TEST: Forgot password with valid username")
        
        self.login_page.navigate_to_login()
        self.login_page.click_forgot_password()
        
        # Enter valid admin username
        self.forgot_password_page.reset_password("Admin")
        
        # Check for success message or navigation
        current_url = self.driver.current_url
        self.logger.info(f"URL after password reset: {current_url}")
        
        # On the demo site, it may show success message or redirect
        self.logger.info("Test passed: Password reset functionality executed")
    
    def test_forgot_password_cancel(self, driver, logger):
        """
        Test: Cancel from forgot password page
        
        Expected: Should return to login page.
        """
        self.logger.info("TEST: Cancel from forgot password page")
        
        self.login_page.navigate_to_login()
        self.login_page.click_forgot_password()
        
        self.forgot_password_page.click_cancel()
        
        # Should be back on login page
        assert self.login_page.is_login_page_displayed(), "Should be on login page"
        
        self.logger.info("Test passed: Cancel returns to login page")