"""
Test Configuration Module

Contains all configuration settings for the OrangeHRM test suite.
"""

import os
from pathlib import Path


class Config:
    """Main configuration class for test settings."""
    
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    ADMIN_USERNAME = "Admin"
    ADMIN_PASSWORD = "admin123"
    
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30
    
    SCREENSHOT_DIR = "screenshots"
    REPORT_DIR = "reports"
    TEST_DATA_DIR = "test_data"
    LOG_DIR = "logs"
    
    @classmethod
    def get_base_dir(cls):
        """Get the base directory of the project."""
        return Path(__file__).parent.parent
    
    @classmethod
    def get_test_data_path(cls, filename):
        """Get full path for test data file."""
        return cls.get_base_dir() / cls.TEST_DATA_DIR / filename
    
    @classmethod
    def get_screenshot_path(cls, filename):
        """Get full path for screenshot file."""
        path = cls.get_base_dir() / cls.SCREENSHOT_DIR
        path.mkdir(exist_ok=True)
        return path / filename
    
    @classmethod
    def get_report_path(cls, filename):
        """Get full path for report file."""
        path = cls.get_base_dir() / cls.REPORT_DIR
        path.mkdir(exist_ok=True)
        return path / filename


class Locators:
    """Centralized locator definitions for all pages."""
    
    # Login Page
    USERNAME_INPUT = "username"
    PASSWORD_INPUT = "password"
    LOGIN_BUTTON = "oxd-button"
    ERROR_MESSAGE = "oxd-alert-content-text"
    FORGOT_PASSWORD_LINK = "Forgot your password?"
    
    # Dashboard
    USER_DROPDOWN = "oxd-userdropdown"
    LOGOUT_LINK = "Logout"
    ADMIN_MENU = "//span[text()='Admin']"
    PIM_MENU = "//span[text()='PIM']"
    LEAVE_MENU = "//span[text()='Leave']"
    TIME_MENU = "//span[text()='Time']"
    RECRUITMENT_MENU = "//span[text()='Recruitment']"
    MY_INFO_MENU = "//span[text()='My Info']"
    PERFORMANCE_MENU = "//span[text()='Performance']"
    DASHBOARD_MENU = "//span[text()='Dashboard']"
    
    # Admin Page
    USER_MANAGEMENT_MENU = "//span[text()='User Management']"
    ADD_BUTTON = "oxd-button--secondary"
    SEARCH_INPUT = "oxd-input"
    SEARCH_BUTTON = "oxd-button--secondary"
    USER_TABLE = "oxd-table"
    
    # My Info
    PERSONAL_DETAILS = "//a[text()='Personal Details']"
    CONTACT_DETAILS = "//a[text()='Contact Details']"
    EMERGENCY_CONTACTS = "//a[text()='Emergency Contacts']"
    DEPENDENTS = "//a[text()='Dependents']"
    IMMIGRATION = "//a[text()='Immigration']"
    JOB = "//a[text()='Job']"
    SALARY = "//a[text()='Salary']"
    REPORT_TO = "//a[text()='Report-to']"
    QUALIFICATIONS = "//a[text()='Qualifications']"
    
    # Leave
    ASSIGN_LEAVE = "//a[text()='Assign Leave']"
    LEAVE_TYPE = "oxd-select-text"
    
    # Claim
    CLAIM_MENU = "//span[text()='Claim']"
    SUBMIT_CLAIM = "//button[text()='Submit Claim']"