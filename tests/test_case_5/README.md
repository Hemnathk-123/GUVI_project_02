# Test Case 5: Create New User and Validate Login

## Description
This test case verifies that a new user can be created in the OrangeHRM system and then successfully login with the created credentials.

## Test Steps
1. Login as Admin
2. Navigate to Admin > User Management > Users
3. Click Add button to create new user
4. Fill in user details (User Role, Employee Name, Username, Status, Password)
5. Save the new user
6. Logout from admin account
7. Login with newly created user credentials
8. Verify login is successful

## How to Run

### Run Test Case 5 only:
```bash
cd "C:\Users\Praveen\Documents\test case 5 & 6"
python -m pytest tests/test_case_5/test_create_user.py -v
```

### Run with HTML report:
```bash
cd "C:\Users\Praveen\Documents\test case 5 & 6"
python -m pytest tests/test_case_5/test_create_user.py -v --html=test_report_case5.html --self-contained-html
```

## Expected Result
- New user should be created successfully
- New user should be able to login to the system

## Configuration
Edit `config.ini` to modify:
- `new_username` - Username for the new user
- `new_password` - Password for the new user
- `employee_name` - Employee name to associate with user
- `user_role` - User role (Admin, ESS, etc.)
- `status` - User status (Enabled, Disabled)