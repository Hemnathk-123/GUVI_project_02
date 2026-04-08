"""
OrangeHRM Automation Test Suite

Test Case 5: Create a new user and validate login
Test Case 6: Validate presence of the newly created user in the admin user list

This module contains the test cases for OrangeHRM web application automation testing.
"""

import pytest
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from pages.base_page import ConfigManager, Logger


class TestOrangeHRM:
    """
    Test suite for OrangeHRM web application.
    Contains test cases for user creation and validation.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Setup fixture - runs before each test.
        Initializes driver, logger, and page objects.
        """
        self.config = ConfigManager()
        self.logger = Logger("TestOrangeHRM")
        self.logger.info("=" * 60)
        self.logger.info("Starting new test execution")
        self.logger.info("=" * 60)
        
        self.driver = self._initialize_driver()
        self.login_page = LoginPage(self.driver, self.logger)
        self.dashboard_page = DashboardPage(self.driver, self.logger)
        self.admin_page = AdminPage(self.driver, self.logger)
        self.add_user_page = AddUserPage(self.driver, self.logger)
        
        self.base_url = self.config.get('TEST_CONFIG', 'base_url')
        self.admin_username = self.config.get('USER_CREDENTIALS', 'admin_username')
        self.admin_password = self.config.get('USER_CREDENTIALS', 'admin_password')
        
        self.new_user_data = {
            'username': self.config.get('NEW_USER_DATA', 'new_username'),
            'password': self.config.get('NEW_USER_DATA', 'new_password'),
            'employee_name': self.config.get('NEW_USER_DATA', 'employee_name'),
            'user_role': self.config.get('NEW_USER_DATA', 'user_role'),
            'status': self.config.get('NEW_USER_DATA', 'status')
        }
        
        yield
        
        self._teardown()
    
    def _initialize_driver(self):
        """
        Initialize WebDriver with configured browser settings.
        
        Returns:
            WebDriver instance
        """
        try:
            browser = self.config.get('BROWSER', 'default_browser')
            headless = self.config.get_boolean('BROWSER', 'headless_mode')
            
            options = Options()
            if headless:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-web-security')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            
            driver = webdriver.Chrome(options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.implicitly_wait(self.config.get_int('TEST_CONFIG', 'implicit_wait'))
            driver.set_page_load_timeout(self.config.get_int('TEST_CONFIG', 'page_load_timeout'))
            
            self.logger.info(f"WebDriver initialized - Browser: {browser}, Headless: {headless}")
            return driver
            
        except WebDriverException as e:
            self.logger.error(f"Failed to initialize WebDriver: {str(e)}")
            raise
    
    def _teardown(self):
        """
        Teardown fixture - runs after each test.
        Closes browser and logs test completion.
        """
        try:
            if self.driver:
                self.driver.quit()
                self.logger.info("Browser closed successfully")
        except Exception as e:
            self.logger.warning(f"Error while closing browser: {str(e)}")
        
        self.logger.info("=" * 60)
        self.logger.info("Test execution completed")
        self.logger.info("=" * 60)
    
    def login_as_admin(self):
        """
        Helper method to login as admin user.
        """
        import time
        self.logger.info("Logging in as admin user")
        self.login_page.navigate_to_login()
        time.sleep(5)  # Wait for page to fully load
        self.login_page.login(self.admin_username, self.admin_password)
        
        if self.login_page.is_login_successful():
            self.logger.info("Admin login successful")
            return True
        else:
            self.logger.error("Admin login failed")
            return False
    
    def capture_screenshot(self, test_name):
        """
        Capture screenshot on failure.
        
        Args:
            test_name: Name of the test for filename
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "screenshots"
        
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        filename = f"{screenshot_dir}/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        self.logger.info(f"Screenshot saved: {filename}")
        return filename
    
    @pytest.mark.order(1)
    def test_case_5_create_new_user_and_validate_login(self):
        """
        Test Case 5: Create a new user and validate login
        
        Description:
        - Navigate to the Admin menu
        - Add a new user with valid details
        - Log out and attempt login with the newly created user
        
        Expected Result:
        - New user should be created successfully and able to log in to the system
        """
        test_name = "test_case_5_create_new_user_and_validate_login"
        self.logger.info(f"Starting {test_name}")
        
        try:
            # Step 1: Login as Admin
            self.logger.info("Step 1: Login as Admin")
            if not self.login_as_admin():
                pytest.fail("Failed to login as admin")
            
            # Step 2: Navigate directly to User Management page via URL
            self.logger.info("Step 2: Navigate to Admin > User Management > Users")
            self.driver.get(f"{self.base_url}/web/index.php/admin/viewSystemUsers")
            time.sleep(3)
            
            # Step 3: Click Add button to create new user
            self.logger.info("Step 3: Click Add button to create new user")
            self.admin_page.click_add_button()
            
            # Step 4: Fill in user details and create user
            self.logger.info("Step 4: Fill in user details and create user")
            self.add_user_page.create_user(
                user_role=self.new_user_data['user_role'],
                employee_name=self.new_user_data['employee_name'],
                username=self.new_user_data['username'],
                status=self.new_user_data['status'],
                password=self.new_user_data['password']
            )
            
            # Step 5: Verify user creation success
            self.logger.info("Step 5: Verify user creation success")
            time.sleep(2)  # Wait for success message
            
            # Step 6: Logout from admin account
            self.logger.info("Step 6: Logout from admin account")
            self.dashboard_page.logout()
            
            # Step 7: Login with newly created user
            self.logger.info("Step 7: Login with newly created user")
            self.login_page.navigate_to_login()
            self.login_page.login(self.new_user_data['username'], self.new_user_data['password'])
            
            # Step 8: Verify login with new user is successful
            self.logger.info("Step 8: Verify login with new user is successful")
            
            if self.login_page.is_login_successful():
                self.logger.info("Test Case 5: PASSED - New user created and able to login")
            else:
                self.logger.error("Test Case 5: FAILED - New user cannot login")
                self.capture_screenshot(test_name)
                pytest.fail("New user login validation failed")
            
        except Exception as e:
            self.logger.error(f"Test Case 5: FAILED with exception: {str(e)}")
            self.capture_screenshot(test_name)
            raise
    
    @pytest.mark.order(2)
    def test_case_6_validate_user_in_admin_list(self):
        """
        Test Case 6: Validate presence of the newly created user in the admin user list
        
        Description:
        - Access the Admin > User Management section
        - Search for the newly created user
        
        Expected Result:
        - The new user record should be found in the user listing
        """
        test_name = "test_case_6_validate_user_in_admin_list"
        self.logger.info(f"Starting {test_name}")
        
        try:
            # Step 1: Login as Admin
            self.logger.info("Step 1: Login as Admin")
            if not self.login_as_admin():
                pytest.fail("Failed to login as admin")
            
            # Step 2: Navigate directly to User Management page via URL
            self.logger.info("Step 2: Navigate to Admin > User Management > Users")
            self.driver.get(f"{self.base_url}/web/index.php/admin/viewSystemUsers")
            time.sleep(5)  # Wait longer for page to fully load
            
            # Get all users in table for debugging
            self.logger.info("Getting all users in table for debugging...")
            js_all_users = """
            var cells = document.querySelectorAll('.oxd-table-cell a');
            var users = [];
            for(var i = 0; i < cells.length; i++) {
                users.push(cells[i].textContent.trim());
            }
            return users;
            """
            all_users = self.driver.execute_script(js_all_users)
            self.logger.info(f"Users found in table: {all_users}")
            
            # Step 3: Search for the newly created user
            self.logger.info("Step 3: Search for the newly created user")
            self.admin_page.search_by_username(self.new_user_data['username'])
            time.sleep(2)
            self.admin_page.click_search_button()
            time.sleep(3)
            
            # Step 4: Verify the user is found in the list
            self.logger.info("Step 4: Verify the user is found in the list")
            
            if self.admin_page.is_user_present(self.new_user_data['username']):
                self.logger.info("Test Case 6: PASSED - New user found in admin user list")
            else:
                self.logger.error("Test Case 6: FAILED - New user not found in admin user list")
                # Debug: Get visible rows after search
                js_after_search = """
                var cells = document.querySelectorAll('.oxd-table-cell a');
                var users = [];
                for(var i = 0; i < cells.length; i++) {
                    users.push(cells[i].textContent.trim());
                }
                return users;
                """
                users_after = self.driver.execute_script(js_after_search)
                self.logger.error(f"Users after search: {users_after}")
                self.capture_screenshot(test_name)
                pytest.fail("User not found in admin user list")
            
        except Exception as e:
            self.logger.error(f"Test Case 6: FAILED with exception: {str(e)}")
            self.capture_screenshot(test_name)
            raise


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=test_report.html", "--self-contained-html"])
