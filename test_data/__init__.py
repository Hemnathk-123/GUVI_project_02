"""
Test Data Module - Provides test data for data-driven testing.

This module contains test data for positive and negative test cases,
organized in a structured way for maintainability and reusability.
"""

import json
import os
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class UserCredentials:
    """Data class for user credentials."""
    username: str
    password: str
    expected_result: bool
    description: str


@dataclass
class NewUserData:
    """Data class for creating new users."""
    username: str
    password: str
    confirm_password: str
    employee_name: str
    user_role: str
    status: str
    expected_result: bool
    description: str
    test_type: str  # positive or negative


class TestDataProvider:
    """
    Provides test data for the OrangeHRM test suite.
    Supports both positive and negative test scenarios.
    """
    
    # Valid admin credentials for the demo site
    ADMIN_CREDENTIALS = {
        "username": "Admin",
        "password": "admin123"
    }
    
    # Test data for login positive cases
    LOGIN_POSITIVE_CASES = [
        UserCredentials(
            username="Admin",
            password="admin123",
            expected_result=True,
            description="Valid admin credentials"
        ),
        UserCredentials(
            username="admin",
            password="admin123",
            expected_result=True,
            description="Admin with lowercase (case-insensitive)"
        ),
    ]
    
    # Test data for login negative cases
    LOGIN_NEGATIVE_CASES = [
        UserCredentials(
            username="Admin",
            password="wrongpassword",
            expected_result=False,
            description="Valid username with wrong password"
        ),
        UserCredentials(
            username="invaliduser",
            password="admin123",
            expected_result=False,
            description="Invalid username with valid password"
        ),
        UserCredentials(
            username="",
            password="admin123",
            expected_result=False,
            description="Empty username"
        ),
        UserCredentials(
            username="Admin",
            password="",
            expected_result=False,
            description="Empty password"
        ),
        UserCredentials(
            username="",
            password="",
            expected_result=False,
            description="Empty username and password"
        ),
        UserCredentials(
            username="Admin",
            password="admin",
            expected_result=False,
            description="Wrong password format"
        ),
        UserCredentials(
            username="admin123",
            password="Admin",
            expected_result=False,
            description="Reversed username and password"
        ),
    ]
    
    # Test data for user creation positive cases
    USER_CREATION_POSITIVE_CASES = [
        NewUserData(
            username="TestUser001",
            password="Test@12345",
            confirm_password="Test@12345",
            employee_name="David Morris",
            user_role="Admin",
            status="Enabled",
            expected_result=True,
            description="Create admin user with all valid data",
            test_type="positive"
        ),
        NewUserData(
            username="ESSUser001",
            password="Test@12345",
            confirm_password="Test@12345",
            employee_name="David Morris",
            user_role="ESS",
            status="Enabled",
            expected_result=True,
            description="Create ESS user with valid data",
            test_type="positive"
        ),
    ]
    
    # Test data for user creation negative cases
    USER_CREATION_NEGATIVE_CASES = [
        NewUserData(
            username="",
            password="Test@12345",
            confirm_password="Test@12345",
            employee_name="David Morris",
            user_role="Admin",
            status="Enabled",
            expected_result=False,
            description="Empty username",
            test_type="negative"
        ),
        NewUserData(
            username="TestUser001",
            password="",
            confirm_password="Test@12345",
            employee_name="David Morris",
            user_role="Admin",
            status="Enabled",
            expected_result=False,
            description="Empty password",
            test_type="negative"
        ),
        NewUserData(
            username="TestUser001",
            password="Test@12345",
            confirm_password="Different@123",
            employee_name="David Morris",
            user_role="Admin",
            status="Enabled",
            expected_result=False,
            description="Passwords do not match",
            test_type="negative"
        ),
        NewUserData(
            username="TestUser001",
            password="weak",
            confirm_password="weak",
            employee_name="David Morris",
            user_role="Admin",
            status="Enabled",
            expected_result=False,
            description="Weak password",
            test_type="negative"
        ),
        NewUserData(
            username="TestUser001",
            password="Test@12345",
            confirm_password="Test@12345",
            employee_name="",
            user_role="Admin",
            status="Enabled",
            expected_result=False,
            description="Empty employee name",
            test_type="negative"
        ),
        NewUserData(
            username="Admin",
            password="Test@12345",
            confirm_password="Test@12345",
            employee_name="David Morris",
            user_role="Admin",
            status="Enabled",
            expected_result=False,
            description="Duplicate username (Admin already exists)",
            test_type="negative"
        ),
    ]
    
    # Search test data
    SEARCH_TEST_CASES = [
        {"search_term": "Admin", "expected_found": True, "description": "Search for existing admin user"},
        {"search_term": "admin", "expected_found": True, "description": "Search with lowercase"},
        {"search_term": "NonExistentUser12345", "expected_found": False, "description": "Search for non-existent user"},
        {"search_term": "", "expected_found": True, "description": "Empty search (show all)"},
    ]
    
    @classmethod
    def get_login_test_data(cls, include_positive=True, include_negative=True):
        """Get login test data based on parameters."""
        data = []
        if include_positive:
            data.extend(cls.LOGIN_POSITIVE_CASES)
        if include_negative:
            data.extend(cls.LOGIN_NEGATIVE_CASES)
        return data
    
    @classmethod
    def get_user_creation_test_data(cls, include_positive=True, include_negative=True):
        """Get user creation test data based on parameters."""
        data = []
        if include_positive:
            data.extend(cls.USER_CREATION_POSITIVE_CASES)
        if include_negative:
            data.extend(cls.USER_CREATION_NEGATIVE_CASES)
        return data
    
    @classmethod
    def load_test_data_from_json(cls, filepath):
        """Load test data from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Test data file not found: {filepath}")
        
        with open(filepath, 'r') as f:
            return json.load(f)
    
    @classmethod
    def save_test_data_to_json(cls, data, filepath):
        """Save test data to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    
    @classmethod
    def get_all_search_test_data(cls):
        """Get all search test cases."""
        return cls.SEARCH_TEST_CASES


def get_test_data_file_path(filename="test_data.json"):
    """Get the full path to a test data file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)


def create_sample_test_data_file():
    """Create a sample test data JSON file."""
    sample_data = {
        "login_tests": [
            {
                "username": "Admin",
                "password": "admin123",
                "expected_result": True,
                "description": "Valid admin credentials"
            }
        ],
        "user_creation_tests": [
            {
                "username": "NewUser123",
                "password": "Test@123",
                "confirm_password": "Test@123",
                "employee_name": "David Morris",
                "user_role": "Admin",
                "status": "Enabled",
                "expected_result": True,
                "description": "Create new admin user"
            }
        ]
    }
    
    filepath = get_test_data_file_path()
    TestDataProvider.save_test_data_to_json(sample_data, filepath)
    return filepath