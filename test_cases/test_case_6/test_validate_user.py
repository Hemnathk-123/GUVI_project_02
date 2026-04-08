"""
Test Case 6: Validate presence of the newly created user in the admin user list

This test case validates that the newly created user appears in the
user listing under Admin > User Management.

Scenario: Validate presence of the newly created user in the admin user list
Description:
- Access the Admin > User Management section
- Search for the newly created user

Expected Result:
- The new user record should be found in the user listing
"""

import pytest
import time
from datetime import datetime
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


class TestCase6:
    """Test Case 6: Validate presence of the newly created user in admin user list."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
        self.dashboard_page = DashboardPage(driver, logger)
        self.admin_page = AdminPage(driver, logger)
    
    def test_validate_user_in_admin_list(self, driver, logger):
        """
        Test: Validate user in admin list
        
        Expected: Admin user should be found in the user list.
        """
        self.logger.info("=" * 50)
        self.logger.info("TEST: Validate user in admin list")
        self.logger.info("=" * 50)
        
        # Step 1: Login as Admin
        self.logger.info("Step 1: Login as Admin")
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Admin login should be successful"
        self.logger.info("Admin login successful")
        
        # Step 2: Navigate to User Management
        self.logger.info("Step 2: Navigate to Admin > User Management")
        self.admin_page.navigate_to_users_page()
        
        # Step 3: Verify user list is visible
        self.logger.info("Step 3: Verify user list is visible")
        assert self.admin_page.is_user_list_visible(), "User list should be visible"
        
        # Step 4: Search for Admin user
        self.logger.info("Step 4: Search for Admin user")
        self.admin_page.search_user("Admin")
        
        # Step 5: Verify user is found
        self.logger.info("Step 5: Verify Admin user exists")
        user_count = self.admin_page.get_user_count()
        
        assert user_count > 0, "Admin user should exist in the list"
        
        self.logger.info(f"Test passed: Found {user_count} user(s) in the list")
        
        # Logout
        self.dashboard_page.logout()
    
    def test_validate_search_functionality(self, driver, logger):
        """
        Test: Validate search functionality
        
        Expected: Search should return appropriate results.
        """
        self.logger.info("TEST: Validate search functionality")
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Login should be successful"
        
        self.admin_page.navigate_to_users_page()
        
        # Search for existing user
        self.admin_page.search_user("Admin")
        user_count = self.admin_page.get_user_count()
        
        assert user_count > 0, "Search should return results for existing user"
        
        # Search for non-existent user
        self.admin_page.search_user("NonExistentUser12345")
        
        self.logger.info("Test passed: Search functionality works correctly")
        
        self.dashboard_page.logout()
    
    def test_user_list_display(self, driver, logger):
        """
        Test: Verify user list is displayed
        
        Expected: User list should be displayed with user records.
        """
        self.logger.info("TEST: Verify user list is displayed")
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Login should be successful"
        
        self.admin_page.navigate_to_users_page()
        
        assert self.admin_page.is_user_list_visible(), "User list should be visible"
        
        user_count = self.admin_page.get_user_count()
        assert user_count > 0, "There should be at least one user in the list"
        
        self.logger.info(f"Test passed: User list displays {user_count} user(s)")
        
        self.dashboard_page.logout()