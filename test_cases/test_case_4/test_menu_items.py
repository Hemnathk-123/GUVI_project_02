"""
Test Case 4: Verify visibility and clickability of main menu items after login

This test case verifies that main menu items are visible and functional
after successful login.

Scenario: Verify visibility and clickability of main menu items after login
Description:
- Log in with valid credentials
- Check for visibility and clickability of menu items: Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard

Expected Result:
- Each of the specified menu items should be visible and functional
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestCase4:
    """Test Case 4: Verify visibility and clickability of main menu items."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, logger):
        """Setup for each test."""
        self.driver = driver
        self.logger = logger
        self.login_page = LoginPage(driver, logger)
        self.dashboard_page = DashboardPage(driver, logger)
    
    @pytest.fixture(scope="class")
    def login_as_admin(self, driver, logger):
        """Login as admin before running tests."""
        self.logger.info("Logging in as admin...")
        self.login_page.navigate_to_login()
        self.login_page.login("Admin", "admin123")
        assert self.login_page.is_login_successful(), "Login should be successful"
        yield
        self.logger.info("Logging out...")
        try:
            self.dashboard_page.logout()
        except:
            pass
    
    def test_menu_admin_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify Admin menu is visible and clickable
        
        Expected: Admin menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify Admin menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("Admin"), "Admin menu should be visible"
        assert self.dashboard_page.is_menu_clickable("Admin"), "Admin menu should be clickable"
        
        self.logger.info("Test passed: Admin menu is visible and clickable")
    
    def test_menu_pim_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify PIM menu is visible and clickable
        
        Expected: PIM menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify PIM menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("PIM"), "PIM menu should be visible"
        assert self.dashboard_page.is_menu_clickable("PIM"), "PIM menu should be clickable"
        
        self.logger.info("Test passed: PIM menu is visible and clickable")
    
    def test_menu_leave_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify Leave menu is visible and clickable
        
        Expected: Leave menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify Leave menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("Leave"), "Leave menu should be visible"
        assert self.dashboard_page.is_menu_clickable("Leave"), "Leave menu should be clickable"
        
        self.logger.info("Test passed: Leave menu is visible and clickable")
    
    def test_menu_time_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify Time menu is visible and clickable
        
        Expected: Time menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify Time menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("Time"), "Time menu should be visible"
        assert self.dashboard_page.is_menu_clickable("Time"), "Time menu should be clickable"
        
        self.logger.info("Test passed: Time menu is visible and clickable")
    
    def test_menu_recruitment_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify Recruitment menu is visible and clickable
        
        Expected: Recruitment menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify Recruitment menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("Recruitment"), "Recruitment menu should be visible"
        assert self.dashboard_page.is_menu_clickable("Recruitment"), "Recruitment menu should be clickable"
        
        self.logger.info("Test passed: Recruitment menu is visible and clickable")
    
    def test_menu_my_info_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify My Info menu is visible and clickable
        
        Expected: My Info menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify My Info menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("My Info"), "My Info menu should be visible"
        assert self.dashboard_page.is_menu_clickable("My Info"), "My Info menu should be clickable"
        
        self.logger.info("Test passed: My Info menu is visible and clickable")
    
    def test_menu_performance_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify Performance menu is visible and clickable
        
        Expected: Performance menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify Performance menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("Performance"), "Performance menu should be visible"
        assert self.dashboard_page.is_menu_clickable("Performance"), "Performance menu should be clickable"
        
        self.logger.info("Test passed: Performance menu is visible and clickable")
    
    def test_menu_dashboard_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify Dashboard menu is visible and clickable
        
        Expected: Dashboard menu should be visible and clickable.
        """
        self.logger.info("TEST: Verify Dashboard menu visible and clickable")
        
        assert self.dashboard_page.is_menu_visible("Dashboard"), "Dashboard menu should be visible"
        assert self.dashboard_page.is_menu_clickable("Dashboard"), "Dashboard menu should be clickable"
        
        self.logger.info("Test passed: Dashboard menu is visible and clickable")
    
    def test_all_menu_items_visible(self, driver, logger, login_as_admin):
        """
        Test: Verify all main menu items are visible
        
        Expected: All main menu items should be visible.
        """
        self.logger.info("TEST: Verify all main menu items visible")
        
        menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]
        
        for menu in menu_items:
            assert self.dashboard_page.is_menu_visible(menu), f"{menu} menu should be visible"
        
        self.logger.info("Test passed: All main menu items are visible")