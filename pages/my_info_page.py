"""
My Info Page Object

This module contains the My Info page object with methods for
interacting with My Info section and its sub-menus.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyInfoPage(BasePage):
    """
    Page object for OrangeHRM My Info page.
    Handles My Info section and its sub-menus.
    """
    
    # My Info sub-menus
    PERSONAL_DETAILS = (By.XPATH, "//a[text()='Personal Details']")
    CONTACT_DETAILS = (By.XPATH, "//a[text()='Contact Details']")
    EMERGENCY_CONTACTS = (By.XPATH, "//a[text()='Emergency Contacts']")
    DEPENDENTS = (By.XPATH, "//a[text()='Dependents']")
    IMMIGRATION = (By.XPATH, "//a[text()='Immigration']")
    JOB = (By.XPATH, "//a[text()='Job']")
    SALARY = (By.XPATH, "//a[text()='Salary']")
    REPORT_TO = (By.XPATH, "//a[text()='Report-to']")
    QUALIFICATIONS = (By.XPATH, "//a[text()='Qualifications']")
    
    # Menu container
    MENU_CONTAINER = (By.CLASS_NAME, "oxd-topbar-body-nav")
    
    def __init__(self, driver, logger):
        """Initialize the My Info page."""
        super().__init__(driver, logger)
        self.logger.info("Initialized MyInfoPage")
    
    def click_personal_details(self):
        """Click on Personal Details."""
        self.click(self.PERSONAL_DETAILS)
        self.logger.info("Clicked Personal Details")
        self.wait_for_page_load()
    
    def click_contact_details(self):
        """Click on Contact Details."""
        self.click(self.CONTACT_DETAILS)
        self.logger.info("Clicked Contact Details")
        self.wait_for_page_load()
    
    def click_emergency_contacts(self):
        """Click on Emergency Contacts."""
        self.click(self.EMERGENCY_CONTACTS)
        self.logger.info("Clicked Emergency Contacts")
        self.wait_for_page_load()
    
    def click_dependents(self):
        """Click on Dependents."""
        self.click(self.DEPENDENTS)
        self.logger.info("Clicked Dependents")
        self.wait_for_page_load()
    
    def click_immigration(self):
        """Click on Immigration."""
        self.click(self.IMMIGRATION)
        self.logger.info("Clicked Immigration")
        self.wait_for_page_load()
    
    def click_job(self):
        """Click on Job."""
        self.click(self.JOB)
        self.logger.info("Clicked Job")
        self.wait_for_page_load()
    
    def click_salary(self):
        """Click on Salary."""
        self.click(self.SALARY)
        self.logger.info("Clicked Salary")
        self.wait_for_page_load()
    
    def click_report_to(self):
        """Click on Report-to."""
        self.click(self.REPORT_TO)
        self.logger.info("Clicked Report-to")
        self.wait_for_page_load()
    
    def click_qualifications(self):
        """Click on Qualifications."""
        self.click(self.QUALIFICATIONS)
        self.logger.info("Clicked Qualifications")
        self.wait_for_page_load()
    
    def is_menu_item_visible(self, menu_name):
        """Check if a specific menu item is visible."""
        menu_locator = (By.XPATH, f"//a[text()='{menu_name}']")
        return self.is_element_visible(menu_locator)
    
    def get_all_menu_items(self):
        """Get all visible menu items under My Info."""
        menu_items = []
        try:
            menus = self.find_elements((By.CSS_SELECTOR, ".oxd-topbar-body-nav li a"))
            for menu in menus:
                menu_items.append(menu.text)
        except:
            pass
        return menu_items