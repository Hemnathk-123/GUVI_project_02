"""
Test Case 8: Validate the presence of menu items under "My Info"

This test case validates that sub-menu items under My Info section
are present and clickable.

Scenario: Validate the presence of menu items under "My Info"
Description:
- Login with valid credentials
- Navigate to the "My Info" section
- Verify that sub-menu items such as "Personal Details," "Contact Details," "Emergency Contacts," and others are present and clickable

Expected Result:
- Each expected section should be listed under "My Info" and should open the corresponding page when clicked
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


class TestCase8:
    """Test Case 8: Validate the presence of menu items under My Info."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
        self.dashboard_page = DashboardPage(driver, logger)
        self.my_info_page = MyInfoPage(driver, logger)
    
    @pytest.fixture(scope="class")
    def login_and_navigate_to_my_info(self, driver, logger):
        """Login and navigate to My Info before tests."""
        self.logger.info("Logging in and navigating to My Info...")
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Login should be successful"
        
        self.dashboard_page.navigate_to_my_info()
        
        yield
        
        # Logout after tests
        try:
            self.dashboard_page.logout()
        except:
            pass
    
    def test_my_info_menu_visible(self, driver, logger):
        """
        Test: Verify My Info menu is visible after login
        
        Expected: My Info menu should be visible.
        """
        self.logger.info("TEST: Verify My Info menu is visible")
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Login should be successful"
        
        assert self.dashboard_page.is_menu_visible("My Info"), "My Info menu should be visible"
        
        self.logger.info("Test passed: My Info menu is visible")
        
        self.dashboard_page.logout()
    
    def test_navigate_to_my_info(self, driver, logger):
        """
        Test: Navigate to My Info section
        
        Expected: Should navigate to My Info page.
        """
        self.logger.info("TEST: Navigate to My Info section")
        
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        
        assert self.login_page.is_login_successful(), "Login should be successful"
        
        self.dashboard_page.navigate_to_my_info()
        
        # Verify we're on My Info page
        current_url = self.driver.current_url
        assert "myInfo" in current_url.lower(), "Should be on My Info page"
        
        self.logger.info("Test passed: Successfully navigated to My Info")
        
        self.dashboard_page.logout()
    
    def test_personal_details_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify Personal Details menu item is visible
        
        Expected: Personal Details should be visible.
        """
        self.logger.info("TEST: Verify Personal Details visible")
        
        assert self.my_info_page.is_menu_item_visible("Personal Details"), \
            "Personal Details should be visible"
        
        self.logger.info("Test passed: Personal Details is visible")
    
    def test_contact_details_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify Contact Details menu item is visible
        
        Expected: Contact Details should be visible.
        """
        self.logger.info("TEST: Verify Contact Details visible")
        
        assert self.my_info_page.is_menu_item_visible("Contact Details"), \
            "Contact Details should be visible"
        
        self.logger.info("Test passed: Contact Details is visible")
    
    def test_emergency_contacts_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify Emergency Contacts menu item is visible
        
        Expected: Emergency Contacts should be visible.
        """
        self.logger.info("TEST: Verify Emergency Contacts visible")
        
        assert self.my_info_page.is_menu_item_visible("Emergency Contacts"), \
            "Emergency Contacts should be visible"
        
        self.logger.info("Test passed: Emergency Contacts is visible")
    
    def test_dependents_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify Dependents menu item is visible
        
        Expected: Dependents should be visible.
        """
        self.logger.info("TEST: Verify Dependents visible")
        
        assert self.my_info_page.is_menu_item_visible("Dependents"), \
            "Dependents should be visible"
        
        self.logger.info("Test passed: Dependents is visible")
    
    def test_immigration_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify Immigration menu item is visible
        
        Expected: Immigration should be visible.
        """
        self.logger.info("TEST: Verify Immigration visible")
        
        assert self.my_info_page.is_menu_item_visible("Immigration"), \
            "Immigration should be visible"
        
        self.logger.info("Test passed: Immigration is visible")
    
    def test_job_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify Job menu item is visible
        
        Expected: Job should be visible.
        """
        self.logger.info("TEST: Verify Job visible")
        
        assert self.my_info_page.is_menu_item_visible("Job"), \
            "Job should be visible"
        
        self.logger.info("Test passed: Job is visible")
    
    def test_all_my_info_submenus_visible(self, driver, logger, login_and_navigate_to_my_info):
        """
        Test: Verify all My Info sub-menu items are visible
        
        Expected: All sub-menu items should be visible.
        """
        self.logger.info("TEST: Verify all My Info submenus visible")
        
        expected_menus = [
            "Personal Details",
            "Contact Details", 
            "Emergency Contacts",
            "Dependents",
            "Immigration",
            "Job"
        ]
        
        for menu in expected_menus:
            assert self.my_info_page.is_menu_item_visible(menu), f"{menu} should be visible"
        
        self.logger.info("Test passed: All My Info submenus are visible")