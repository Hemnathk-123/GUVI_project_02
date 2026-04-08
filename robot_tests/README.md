# OrangeHRM Automation Testing - Robot Framework

This folder contains Robot Framework test automation for OrangeHRM.

## Test Cases

### TC5 - Create New User and Validate Login
- Login as Admin
- Navigate to User Management
- Click Add button
- Verify Add User form is displayed
- Logout and re-login to verify system

### TC6 - Validate User in Admin List
- Login as Admin
- Navigate to User Management
- Verify user list is displayed
- Get user count
- Search for Admin user
- Verify search results

## Running Tests

```bash
# Run TC5
python -m robot --outputdir output test_cases/TC5_Create_User.robot

# Run TC6
python -m robot --outputdir output test_cases/TC6_Validate_User.robot

# Run both
python -m robot --outputdir output test_cases/
```

## Requirements

- Python 3.x
- robotframework
- robotframework-seleniumlibrary
- selenium

Install: `pip install robotframework robotframework-seleniumlibrary selenium`

## Results

- TC5: ✅ PASSED
- TC6: ✅ PASSED

Reports saved in: `output/`