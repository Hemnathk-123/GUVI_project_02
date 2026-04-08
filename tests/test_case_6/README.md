# Test Case 6: Validate Presence of Newly Created User in Admin User List

## Description
This test case verifies that the newly created user appears in the admin user list after creation.

## Test Steps
1. Login as Admin
2. Navigate to Admin > User Management > Users
3. Search for the newly created user by username
4. Click Search button
5. Verify the user appears in the user list

## How to Run

### Run Test Case 6 only:
```bash
cd "C:\Users\Praveen\Documents\test case 5 & 6"
python -m pytest tests/test_case_6/test_validate_user.py -v
```

### Run with HTML report:
```bash
cd "C:\Users\Praveen\Documents\test case 5 & 6"
python -m pytest tests/test_case_6/test_validate_user.py -v --html=test_report_case6.html --self-contained-html
```

## Expected Result
- The newly created user should be found in the admin user list

## Configuration
Make sure the `new_username` in `config.ini` matches the user created in Test Case 5.

## Note
Test Case 6 should be run after Test Case 5 to validate the user that was created.