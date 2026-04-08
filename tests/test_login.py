"""
OrangeHRM Login Test Cases

This module contains test cases for validating login functionality
of the OrangeHRM application. It includes both positive and negative
test scenarios with proper error handling and reporting.

Test Cases:
- Valid login credentials (positive)
- Invalid username (negative)
- Invalid password (negative)
- Empty credentials (negative)
- Case-insensitive username (positive)
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.login_page import LoginPage
from test_data import TestDataProvider


class TestLogin:
    """Test suite for OrangeHRM login functionality."""
    
    @pytest.mark.positive
    @pytest.mark.login
    def test_valid_admin_login(self, driver, logger, config):
        """
        Test Case: Verify successful login with valid admin credentials.
        
        Expected: User should be able to login successfully and see dashboard.
        """
        login_page = LoginPage(driver, logger)
        
        logger.info("Navigating to login page")
        login_page.navigate_to_login()
        
        logger.info("Entering admin credentials")
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        
        logger.info("Clicking login button")
        login_page.click_login()
        
        logger.info("Verifying login success")
        WebDriverWait(driver, 15).until(
            EC.url_contains("dashboard"),
            "Login failed - not redirected to dashboard"
        )
        
        assert "dashboard" in driver.current_url.lower(), \
            "Login failed - URL does not contain 'dashboard'"
        
        logger.info("Login successful - Dashboard page displayed")
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_invalid_password(self, driver, logger, config):
        """
        Test Case: Verify login fails when using invalid password.
        
        Expected: Error message should be displayed.
        """
        login_page = LoginPage(driver, logger)
        
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password("wrongpassword123")
        login_page.click_login()
        
        try:
            error_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "oxd-alert-content-text")
                )
            )
            error_message = error_element.text
            
            assert "Invalid" in error_message or "error" in error_message.lower(), \
                f"Expected error message, got: {error_message}"
            
            logger.info(f"Expected error message displayed: {error_message}")
        except TimeoutException:
            pytest.fail("Expected error message was not displayed")
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_invalid_username(self, driver, logger, config):
        """
        Test Case: Verify login fails when using non-existent username.
        
        Expected: Error message should be displayed.
        """
        login_page = LoginPage(driver, logger)
        
        login_page.navigate_to_login()
        login_page.enter_username("NonExistentUser123")
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        try:
            error_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "oxd-alert-content-text")
                )
            )
            error_message = error_element.text
            
            assert "Invalid" in error_message or "error" in error_message.lower(), \
                f"Expected error message, got: {error_message}"
            
            logger.info(f"Expected error message displayed: {error_message}")
        except TimeoutException:
            pytest.fail("Expected error message was not displayed")
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_empty_username(self, driver, logger, config):
        """
        Test Case: Verify login fails when username field is empty.
        
        Expected: Validation error should be displayed.
        """
        login_page = LoginPage(driver, logger)
        
        login_page.navigate_to_login()
        login_page.enter_username("")
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        current_url = driver.current_url
        assert "dashboard" not in current_url.lower(), \
            "Login should fail with empty username"
        
        logger.info("Login correctly rejected for empty username")
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_empty_password(self, driver, logger, config):
        """
        Test Case: Verify login fails when password field is empty.
        
        Expected: Validation error should be displayed.
        """
        login_page = LoginPage(driver, logger)
        
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password("")
        login_page.click_login()
        
        current_url = driver.current_url
        assert "dashboard" not in current_url.lower(), \
            "Login should fail with empty password"
        
        logger.info("Login correctly rejected for empty password")
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_empty_credentials(self, driver, logger, config):
        """
        Test Case: Verify login fails when both username and password are empty.
        
        Expected: Validation error should be displayed.
        """
        login_page = LoginPage(driver, logger)
        
        login_page.navigate_to_login()
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login()
        
        current_url = driver.current_url
        assert "dashboard" not in current_url.lower(), \
            "Login should fail with empty credentials"
        
        logger.info("Login correctly rejected for empty credentials")


class TestLoginDataDriven:
    """Data-driven test cases for login functionality."""
    
    @pytest.mark.parametrize("credentials", TestDataProvider.LOGIN_NEGATIVE_CASES)
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_data_driven(self, driver, logger, config, credentials):
        """
        Parameterized test for negative login scenarios.
        
        Tests multiple combinations of invalid credentials.
        """
        login_page = LoginPage(driver, logger)
        
        logger.info(f"Testing: {credentials.description}")
        login_page.navigate_to_login()
        login_page.enter_username(credentials.username)
        login_page.enter_password(credentials.password)
        login_page.click_login()
        
        try:
            error_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "oxd-alert-content-text")
                )
            )
            logger.info(f"Test passed: {credentials.description}")
        except TimeoutException:
            current_url = driver.current_url
            if "dashboard" not in current_url.lower():
                logger.info(f"Test passed: {credentials.description}")
            else:
                pytest.fail(f"Login unexpectedly succeeded for: {credentials.description}")


class TestLogout:
    """Test cases for logout functionality."""
    
    @pytest.mark.positive
    @pytest.mark.login
    def test_user_logout(self, driver, logger, config):
        """
        Test Case: Verify user can logout successfully.
        
        Expected: User should be redirected to login page after logout.
        """
        login_page = LoginPage(driver, logger)
        
        logger.info("Login as admin")
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard"),
            "Login failed"
        )
        logger.info("Logged in successfully")
        
        logger.info("Click user dropdown")
        try:
            user_dropdown = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown"))
            )
            user_dropdown.click()
            logger.info("Clicked user dropdown")
        except NoSuchElementException:
            pytest.fail("User dropdown not found")
        
        logger.info("Click logout")
        try:
            logout_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(),'Logout')]")
                )
            )
            logout_link.click()
            logger.info("Clicked logout")
            
            WebDriverWait(driver, 10).until(
                EC.url_contains("login"),
                "Logout failed - not redirected to login page"
            )
            
            assert "login" in driver.current_url.lower(), \
                "Logout failed"
            
            logger.info("Logout successful")
            
        except (NoSuchElementException, TimeoutException):
            pytest.fail("Logout link not found or not clickable")