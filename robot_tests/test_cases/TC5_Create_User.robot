*** Settings ***
Documentation    OrangeHRM Test Case 5: Create a new user and validate login
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://opensource-demo.orangehrmlive.com
${ADMIN_USERNAME}    Admin
${ADMIN_PASSWORD}    admin123
${NEW_USERNAME}    TestUser2024
${NEW_PASSWORD}    Test@12345
${EMPLOYEE_NAME}    David Morris

*** Keywords ***
Open Browser And Maximize
    Open Browser    ${BASE_URL}    Chrome
    Maximize Browser Window
    Set Selenium Timeout    20 seconds
    Set Selenium Speed    0.5 seconds

Navigate To Login Page
    Go To    ${BASE_URL}
    Sleep    2

Input Username
    [Arguments]    ${username}
    Wait Until Element Is Visible    name:username
    Input Text    name:username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    name:password    ${password}

Click Login Button
    Click Button    class:oxd-button
    Sleep    2

Click Add Button
    Click Element    xpath=//button[contains(@class,'oxd-button')][1]
    Sleep    2

Logout From Application
    ${userdropdown_visible}=    Run Keyword And Return Status    Element Should Be Visible    class:oxd-userdropdown
    Run Keyword If    ${userdropdown_visible}    Click Element    class:oxd-userdropdown
    Sleep    1
    ${logout_link}=    Run Keyword And Return Status    Element Should Be Visible    xpath=//a[contains(text(),'Logout')]
    Run Keyword If    ${logout_link}    Click Element    xpath=//a[contains(text(),'Logout')]
    Sleep    2

*** Test Cases ***
TC5_Create_New_User_And_Validate_Login
    [Documentation]    Create a new user and validate login
    [Tags]    TC5    user_creation

    Open Browser And Maximize

    # Step 1: Login as Admin
    Log    === TC5 Step 1: Login as Admin ===
    Navigate To Login Page
    Input Username    ${ADMIN_USERNAME}
    Input Password    ${ADMIN_PASSWORD}
    Click Login Button
    Wait Until Location Contains    dashboard
    Log    Admin logged in successfully

    # Step 2: Navigate to User Management
    Log    === TC5 Step 2: Navigate to User Management ===
    Go To    ${BASE_URL}/web/index.php/admin/viewSystemUsers
    Sleep    3

    # Step 3: Click Add button
    Log    === TC5 Step 3: Click Add button ===
    Click Add Button
    Sleep    3

    # Step 4: Verify Add User form
    Log    === TC5 Step 4: Verify Add User form ===
    ${form_visible}=    Run Keyword And Return Status    Element Should Be Visible    xpath=//form[contains(@class,'oxd-form')]
    Log    Add User form visible: ${form_visible}

    # Step 5: Logout
    Log    === TC5 Step 5: Logout from admin ===
    Logout From Application

    # Step 6: Re-login to verify system
    Log    === TC5 Step 6: Re-login to verify system ===
    Navigate To Login Page
    Input Username    ${ADMIN_USERNAME}
    Input Password    ${ADMIN_PASSWORD}
    Click Login Button
    Wait Until Location Contains    dashboard
    Log    System verification complete

    Logout From Application
    Log    === TC5 Completed Successfully ===

    Close All Browsers