"""
Dashboard Page Object

This module contains the dashboard page object with methods for
navigating through the OrangeHRM application menu items.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Page object for OrangeHRM Dashboard page.
    Handles navigation to different menu sections.
    """
    
    # Menu locators
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_LEAVE = (By.XPATH, "//span[text()='Leave']")
    MENU_TIME = (By.XPATH, "//span[text()='Time']")
    MENU_RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    MENU_PERFORMANCE = (By.XPATH, "//span[text()='Performance']")
    MENU_DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    MENU_MY_INFO = (By.XPATH, "//span[text()='My Info']")
    MENU_DIRECTORY = (By.XPATH, "//span[text()='Directory']")
    MENU_MAINTENANCE = (By.XPATH, "//span[text()='Maintenance']")
    MENU_CLAIM = (By.XPATH, "//span[text()='Claim']")
    
    # User profile
    USER_PROFILE_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
    PROFILE_LINK = (By.XPATH, "//a[text()='Profile']")
    
    def __init__(self, driver, logger):
        """Initialize the dashboard page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized DashboardPage")
    
    def navigate_to_admin(self):
        """Click on Admin menu."""
        self.click(self.MENU_ADMIN)
        self.logger.info("Clicked Admin menu")
        self.wait_for_page_load()
    
    def navigate_to_pim(self):
        """Click on PIM menu."""
        self.click(self.MENU_PIM)
        self.logger.info("Clicked PIM menu")
        self.wait_for_page_load()
    
    def navigate_to_leave(self):
        """Click on Leave menu."""
        self.click(self.MENU_LEAVE)
        self.logger.info("Clicked Leave menu")
        self.wait_for_page_load()
    
    def navigate_to_time(self):
        """Click on Time menu."""
        self.click(self.MENU_TIME)
        self.logger.info("Clicked Time menu")
        self.wait_for_page_load()
    
    def navigate_to_recruitment(self):
        """Click on Recruitment menu."""
        self.click(self.MENU_RECRUITMENT)
        self.logger.info("Clicked Recruitment menu")
        self.wait_for_page_load()
    
    def navigate_to_performance(self):
        """Click on Performance menu."""
        self.click(self.MENU_PERFORMANCE)
        self.logger.info("Clicked Performance menu")
        self.wait_for_page_load()
    
    def navigate_to_dashboard(self):
        """Click on Dashboard menu."""
        self.click(self.MENU_DASHBOARD)
        self.logger.info("Clicked Dashboard menu")
        self.wait_for_page_load()
    
    def navigate_to_my_info(self):
        """Click on My Info menu."""
        self.click(self.MENU_MY_INFO)
        self.logger.info("Clicked My Info menu")
        self.wait_for_page_load()
    
    def navigate_to_directory(self):
        """Click on Directory menu."""
        self.click(self.MENU_DIRECTORY)
        self.logger.info("Clicked Directory menu")
        self.wait_for_page_load()
    
    def navigate_to_claim(self):
        """Click on Claim menu."""
        self.click(self.MENU_CLAIM)
        self.logger.info("Clicked Claim menu")
        self.wait_for_page_load()
    
    def logout(self):
        """Logout from the application."""
        try:
            self.click(self.USER_PROFILE_DROPDOWN)
            self.logger.info("Clicked user dropdown")
            
            self.click(self.LOGOUT_LINK)
            self.logger.info("Clicked logout")
            self.wait_for_page_load()
        except Exception as e:
            self.logger.error(f"Failed to logout: {str(e)}")
            raise
    
    def is_menu_visible(self, menu_name):
        """Check if a specific menu is visible."""
        menu_locator = (By.XPATH, f"//span[text()='{menu_name}']")
        return self.is_element_visible(menu_locator)
    
    def is_menu_clickable(self, menu_name):
        """Check if a specific menu is clickable."""
        menu_locator = (By.XPATH, f"//span[text()='{menu_name}']")
        return self.is_element_present(menu_locator)