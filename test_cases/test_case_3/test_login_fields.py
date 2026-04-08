"""
Test Case 3: Validate presence of login fields

This test case validates that username and password input fields
are visible and enabled for input on the login page.

Scenario: Validate presence of login fields
Description:
- Check for visibility of username and password input fields on the login page

Expected Result:
- Username and password fields must be visible and enabled for input
"""

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestCase3:
    """Test Case 3: Validate presence of login fields."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
    
    def test_username_field_visible(self, driver, logger):
        """
        Test: Verify username field is visible
        
        Expected: Username field should be visible on login page.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify username field is visible")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        assert self.login_page.is_element_visible(self.login_page.USERNAME_INPUT), \
            "Username field should be visible"
        
        self.logger.info("Test passed: Username field is visible")
    
    def test_password_field_visible(self, driver, logger):
        """
        Test: Verify password field is visible
        
        Expected: Password field should be visible on login page.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify password field is visible")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        assert self.login_page.is_element_visible(self.login_page.PASSWORD_INPUT), \
            "Password field should be visible"
        
        self.logger.info("Test passed: Password field is visible")
    
    def test_login_button_visible(self, driver, logger):
        """
        Test: Verify login button is visible
        
        Expected: Login button should be visible on login page.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify login button is visible")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        assert self.login_page.is_element_visible(self.login_page.LOGIN_BUTTON), \
            "Login button should be visible"
        
        self.logger.info("Test passed: Login button is visible")
    
    def test_username_field_enabled(self, driver, logger):
        """
        Test: Verify username field is enabled
        
        Expected: Username field should be enabled for input.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify username field is enabled")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.USERNAME_INPUT)
        )
        
        assert username_field.is_enabled(), "Username field should be enabled"
        
        self.logger.info("Test passed: Username field is enabled")
    
    def test_password_field_enabled(self, driver, logger):
        """
        Test: Verify password field is enabled
        
        Expected: Password field should be enabled for input.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify password field is enabled")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.login_page.PASSWORD_INPUT)
        )
        
        assert password_field.is_enabled(), "Password field should be enabled"
        
        self.logger.info("Test passed: Password field is enabled")
    
    def test_all_login_fields_present(self, driver, logger):
        """
        Test: Verify all login fields are present and functional
        
        Expected: All required fields should be present.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify all login fields present")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        is_visible = self.login_page.is_login_page_displayed()
        assert is_visible, "All login fields should be present and visible"
        
        self.logger.info("Test passed: All login fields are present and visible")