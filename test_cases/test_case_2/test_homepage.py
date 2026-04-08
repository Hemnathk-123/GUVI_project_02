"""
Test Case 2: Verify that the home URL is accessible

This test case verifies that the OrangeHRM home page loads without error.

Scenario: Verify that the home URL is accessible
Description:
- Launch the browser and navigate to https://opensource-demo.orangehrmlive.com

Expected Result:
- Home page should load without error
"""

import pytest
from pages.login_page import LoginPage


class TestCase2:
    """Test Case 2: Verify that the home URL is accessible."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
    
    def test_home_page_accessible(self, driver, logger):
        """
        Test: Verify home page loads without error
        
        Expected: Home page should load and display login form.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify home URL is accessible")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        assert self.login_page.is_login_page_displayed(), "Login page should be displayed"
        
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        
        assert "opensource-demo.orangehrmlive.com" in current_url, "Should be on OrangeHRM home page"
        
        self.logger.info("Test passed: Home page loaded successfully without error")
    
    def test_login_page_elements_visible(self, driver, logger):
        """
        Test: Verify login page elements are visible
        
        Expected: Username, password fields and login button should be visible.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Verify login page elements visible")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        
        assert self.login_page.is_element_visible(self.login_page.USERNAME_INPUT), "Username field should be visible"
        assert self.login_page.is_element_visible(self.login_page.PASSWORD_INPUT), "Password field should be visible"
        assert self.login_page.is_element_visible(self.login_page.LOGIN_BUTTON), "Login button should be visible"
        
        self.logger.info("Test passed: All login page elements are visible")