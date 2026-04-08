# OrangeHRM Automation Testing Project

A comprehensive automation testing framework for OrangeHRM using Python, Selenium, and pytest.

## Project Overview

This project implements automated testing for the OrangeHRM HR Management System (https://opensource-demo.orangehrmlive.com) using:
- **Python 3.x** - Programming language
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **Page Object Model (POM)** - Design pattern for better code organization

## Features Implemented

- **Page Object Model (POM)** - Object-oriented design with inheritance
- **Data-Driven Testing** - CSV-based test data for login validation
- **Positive & Negative Test Cases** - Comprehensive test coverage
- **Exception Handling** - Robust error handling for test resilience
- **Logging** - Comprehensive execution logs
- **HTML Reports** - pytest-html for detailed test reports
- **Allure Reports** - Rich interactive reports (optional)

## Test Cases Covered

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC-1 | Validate login with multiple credential sets | ✅ |
| TC-2 | Verify home URL is accessible | ✅ |
| TC-3 | Validate presence of login fields | ✅ |
| TC-4 | Verify main menu items after login | ✅ |
| TC-5 | Create new user and validate login | ✅ |
| TC-6 | Validate user in admin list | ✅ |
| TC-7 | Verify Forgot Password functionality | ✅ |
| TC-8 | Validate My Info menu items | ✅ |
| TC-9 | Assign leave to employee | ✅ |
| TC-10 | Initiate claim request | ✅ |

## Project Structure

```
OrangeHRM-Automation/
├── config.py                 # Configuration settings
├── conftest.py              # Pytest fixtures and hooks
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── pages/                  # Page Object Model classes
│   ├── base_page.py       # Base page with common methods
│   ├── login_page.py      # Login page object
│   ├── dashboard_page.py  # Dashboard page object
│   ├── admin_page.py      # Admin page object
│   ├── add_user_page.py   # Add user page object
│   ├── my_info_page.py    # My Info page object
│   ├── leave_page.py      # Leave page object
│   ├── claim_page.py      # Claim page object
│   └── forgot_password_page.py  # Forgot password page
├── test_data/             # Test data files
│   └── login_credentials.csv  # Login test data
├── test_cases/            # Test case folders (each runs individually)
│   ├── test_case_1/       # Login with multiple credentials
│   ├── test_case_2/       # Home URL accessibility
│   ├── test_case_3/       # Login fields validation
│   ├── test_case_4/       # Menu items validation
│   ├── test_case_5/       # Create new user
│   ├── test_case_6/       # Validate user in list
│   ├── test_case_7/       # Forgot password
│   ├── test_case_8/       # My Info menu items
│   ├── test_case_9/       # Assign leave
│   └── test_case_10/      # Claim request
├── reports/               # Test reports
├── screenshots/           # Screenshots on failure
└── logs/                 # Test execution logs
```

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Requirements
- Python 3.7+
- Chrome browser
- ChromeDriver (automatically managed)

## Running Tests

### Run All Tests
```bash
pytest test_cases/ -v
```

### Run Individual Test Case
```bash
# Test Case 1
pytest test_cases/test_case_1/ -v

# Test Case 2
pytest test_cases/test_case_2/ -v

# And so on...
```

### Run with HTML Report
```bash
pytest test_cases/ -v --html=reports/test_report.html --self-contained-html
```

### Run Specific Test
```bash
pytest test_cases/test_case_1/test_login.py::TestCase1::test_login_with_valid_credentials -v
```

## Test Case Details

### Test Case 1: Login with Multiple Credentials
- Uses data-driven approach with CSV file
- Tests positive cases (valid credentials)
- Tests negative cases (invalid credentials, empty fields)
- Validates logout functionality

### Test Case 2: Home URL Accessibility
- Verifies home page loads without error
- Checks login page elements are displayed

### Test Case 3: Login Fields Validation
- Verifies username field visibility and enabled state
- Verifies password field visibility and enabled state
- Verifies login button visibility

### Test Case 4: Menu Items After Login
- Validates Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard menus
- Checks visibility and clickability

### Test Case 5: Create New User
- Navigates to Admin > User Management
- Creates new user with valid details
- Validates new user can login

### Test Case 6: Validate User in Admin List
- Searches for user in admin list
- Validates user exists in the listing

### Test Case 7: Forgot Password
- Verifies Forgot Password link is visible
- Tests password reset functionality

### Test Case 8: My Info Menu Items
- Validates sub-menu items under My Info
- Personal Details, Contact Details, Emergency Contacts, etc.

### Test Case 9: Assign Leave
- Navigates to Leave section
- Tests Assign Leave form

### Test Case 10: Claim Request
- Navigates to Claim section
- Tests claim submission form

## Reports

### HTML Report
```bash
pytest test_cases/ -v --html=reports/report.html --self-contained-html
```

### Allure Report (Optional)
```bash
# Install allure
pip install allure-pytest

# Generate
pytest test_cases/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Best Practices Implemented

1. **Page Object Model** - Each page has its own class with methods
2. **Data-Driven Testing** - Test data separated from test code
3. **Fixtures** - Pytest fixtures for setup/teardown
4. **Logging** - Comprehensive logging for debugging
5. **Exception Handling** - Try-except blocks with proper handling
6. **Screenshots** - Automatic screenshots on failure
7. **Modular Structure** - Each test case in separate folder

## Known Limitations

1. **OrangeHRM Demo Site** - Uses Vue.js 5.8 which may have automation challenges
2. **User Creation** - May not work consistently due to Vue.js reactivity
3. **Network Dependency** - Tests require stable internet connection

## Notes

- Each test case folder can be run independently
- Browser is automatically closed after each test
- Screenshots are saved on test failures
- Logs are generated for each test execution

## License

This project is for educational and testing purposes.

## Author

Automated Test Suite for OrangeHRM