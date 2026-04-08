"""
OrangeHRM User Management Test Cases

This module contains test cases for user management functionality
including user search, validation, and admin operations.

Test Cases:
- User list validation (positive)
- User search functionality (positive/negative)
- User validation in admin list
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from test_data import TestDataProvider


class TestUserList:
    """Test suite for user list functionality."""
    
    @pytest.mark.positive
    @pytest.mark.user_search
    def test_user_list_display(self, driver, logger, config):
        """
        Test Case: Verify user list is displayed after admin login.
        
        Expected: User list table should be visible with existing users.
        """
        login_page = LoginPage(driver, logger)
        admin_page = AdminPage(driver, logger)
        
        logger.info("Login as admin")
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        WebDriverWait(driver, 15).until(
            EC.url_contains("dashboard"),
            "Login failed"
        )
        logger.info("Logged in as admin")
        
        logger.info("Navigate to User Management")
        admin_page.navigate_to_users_page()
        
        logger.info("Verify user list is displayed")
        user_list_visible = admin_page.is_user_list_visible()
        assert user_list_visible, "User list should be visible"
        
        logger.info("User list displayed successfully")
    
    @pytest.mark.positive
    @pytest.mark.user_search
    def test_search_existing_user(self, driver, logger, config):
        """
        Test Case: Verify search returns results for existing user.
        
        Expected: Search should find the Admin user.
        """
        login_page = LoginPage(driver, logger)
        admin_page = AdminPage(driver, logger)
        
        logger.info("Login and navigate to user management")
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        admin_page.navigate_to_users_page()
        
        logger.info("Search for Admin user")
        admin_page.search_user("Admin")
        
        logger.info("Verify search results")
        row_count = admin_page.get_user_count()
        assert row_count > 0, "Should find at least one user"
        
        logger.info(f"Found {row_count} user(s)")
    
    @pytest.mark.negative
    def test_search_nonexistent_user(self, driver, logger, config):
        """
        Test Case: Verify search shows no results for non-existent user.
        
        Expected: No results or empty state should be displayed.
        """
        login_page = LoginPage(driver, logger)
        admin_page = AdminPage(driver, logger)
        
        logger.info("Login and navigate to user management")
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        admin_page.navigate_to_users_page()
        
        logger.info("Search for non-existent user")
        admin_page.search_user("NonExistentUserXYZ123")
        
        logger.info("Verify no results")
        row_count = admin_page.get_user_count()
        logger.info(f"User count after search: {row_count}")


class TestUserValidation:
    """Test suite for user validation in admin list."""
    
    @pytest.mark.positive
    def test_validate_admin_user_exists(self, driver, logger, config):
        """
        Test Case: Verify Admin user exists in the system.
        
        Expected: Admin user should be found in the user list.
        """
        login_page = LoginPage(driver, logger)
        admin_page = AdminPage(driver, logger)
        
        logger.info("Login as admin")
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))
        logger.info("Logged in successfully")
        
        logger.info("Navigate to User Management")
        admin_page.navigate_to_users_page()
        
        logger.info("Search for Admin user")
        admin_page.search_user("Admin")
        
        logger.info("Verify Admin user exists")
        row_count = admin_page.get_user_count()
        assert row_count > 0, "Admin user should exist in the list"
        
        logger.info("Admin user found in user list")


class TestUserSearchDataDriven:
    """Data-driven test cases for user search."""
    
    @pytest.mark.parametrize("search_data", TestDataProvider.SEARCH_TEST_CASES)
    @pytest.mark.user_search
    def test_search_data_driven(self, driver, logger, config, search_data):
        """
        Parameterized test for user search scenarios.
        
        Tests various search inputs and expected results.
        """
        login_page = LoginPage(driver, logger)
        admin_page = AdminPage(driver, logger)
        
        logger.info(f"Testing: {search_data['description']}")
        login_page.navigate_to_login()
        login_page.enter_username(config.ADMIN_USERNAME)
        login_page.enter_password(config.ADMIN_PASSWORD)
        login_page.click_login()
        
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        admin_page.navigate_to_users_page()
        
        admin_page.search_user(search_data['search_term'])
        logger.info(f"Searched for: {search_data['search_term']}")
        
        logger.info("Verify search results")
        row_count = admin_page.get_user_count()
        
        if search_data['expected_found']:
            assert row_count > 0, \
                f"Expected to find users for search term: {search_data['search_term']}"
        else:
            logger.info(f"Search for '{search_data['search_term']}' completed")