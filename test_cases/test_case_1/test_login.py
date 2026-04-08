"""
Test Case 1: Validate login functionality using multiple sets of credentials

This test case validates login functionality using different combinations
of usernames and passwords from external data source (CSV).

Scenario: Validate login functionality using multiple sets of credentials
Description:
- Use structured external data source (CSV) containing different username/password combinations
- Attempt login with each dataset
- Validate successful login
- Perform logout after each successful login

Expected Result:
- Valid credentials should log in successfully
- Invalid credentials should be rejected with an appropriate message
- Login status should be validated properly
"""

import pytest
import csv
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestCase1:
    """Test Case 1: Validate login functionality using multiple sets of credentials."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
        self.dashboard_page = DashboardPage(driver, logger)
        self.test_data = []
    
    def load_test_data(self):
        """Load test data from CSV file."""
        csv_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "login_credentials.csv")
        
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.test_data.append(row)
        
        self.logger.info(f"Loaded {len(self.test_data)} test data sets")
        return self.test_data
    
    def test_login_with_valid_credentials(self, driver, logger):
        """
        Test: Login with valid credentials (positive case)
        
        Expected: User should be able to login successfully and see dashboard.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Login with valid credentials")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Login should be successful with valid credentials"
        
        self.dashboard_page.logout()
        self.logger.info("Test passed: Valid login and logout completed")
    
    def test_login_with_invalid_password(self, driver, logger):
        """
        Test: Login with invalid password (negative case)
        
        Expected: Error message should be displayed.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Login with invalid password")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "wrongpassword")
        
        assert not self.login_page.is_login_successful(), "Login should fail with invalid password"
        
        error_msg = self.login_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        
        self.logger.info(f"Test passed: Error message displayed - {error_msg}")
    
    def test_login_with_invalid_username(self, driver, logger):
        """
        Test: Login with invalid username (negative case)
        
        Expected: Error message should be displayed.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Login with invalid username")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        self.login_page.login("InvalidUser123", "admin123")
        
        assert not self.login_page.is_login_successful(), "Login should fail with invalid username"
        
        error_msg = self.login_page.get_error_message()
        assert error_msg is not None, "Error message should be displayed"
        
        self.logger.info(f"Test passed: Error message displayed - {error_msg}")
    
    def test_login_with_empty_username(self, driver, logger):
        """
        Test: Login with empty username (negative case)
        
        Expected: Login should fail.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Login with empty username")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        self.login_page.login("", "admin123")
        
        assert not self.login_page.is_login_successful(), "Login should fail with empty username"
        
        self.logger.info("Test passed: Login rejected for empty username")
    
    def test_login_with_empty_password(self, driver, logger):
        """
        Test: Login with empty password (negative case)
        
        Expected: Login should fail.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Login with empty password")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "")
        
        assert not self.login_page.is_login_successful(), "Login should fail with empty password"
        
        self.logger.info("Test passed: Login rejected for empty password")
    
    def test_login_with_empty_credentials(self, driver, logger):
        """
        Test: Login with empty credentials (negative case)
        
        Expected: Login should fail.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Login with empty credentials")
        self.logger.info("=" * 50)
        
        self.login_page.navigate_to_login()
        self.login_page.login("", "")
        
        assert not self.login_page.is_login_successful(), "Login should fail with empty credentials"
        
        self.logger.info("Test passed: Login rejected for empty credentials")
    
    @pytest.mark.parametrize("data", [
        {"username": "Admin", "password": "admin123", "expected": "TRUE"},
        {"username": "admin", "password": "admin123", "expected": "TRUE"},
        {"username": "Admin", "password": "wrongpassword", "expected": "FALSE"},
        {"username": "InvalidUser", "password": "admin123", "expected": "FALSE"},
    ])
    def test_login_data_driven(self, driver, logger, data):
        """
        Test: Data-driven login tests
        
        Expected: Based on expected result in test data.
        """
        self.logger.info(f"Testing: {data['username']} / {data['password']} - Expected: {data['expected']}")
        
        self.login_page.navigate_to_login()
        self.login_page.login(data["username"], data["password"])
        
        is_success = self.login_page.is_login_successful()
        
        if data["expected"].upper() == "TRUE":
            assert is_success, "Login should be successful"
            self.dashboard_page.logout()
        else:
            assert not is_success, "Login should fail"
        
        self.logger.info(f"Test result: {'PASS' if is_success == (data['expected'].upper() == 'TRUE') else 'FAIL'}")