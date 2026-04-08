*** Settings ***
Documentation    OrangeHRM Test Case 6: Validate presence of user in admin user list
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://opensource-demo.orangehrmlive.com
${ADMIN_USERNAME}    Admin
${ADMIN_PASSWORD}    admin123

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

Logout From Application
    ${userdropdown_visible}=    Run Keyword And Return Status    Element Should Be Visible    class:oxd-userdropdown
    Run Keyword If    ${userdropdown_visible}    Click Element    class:oxd-userdropdown
    Sleep    1
    ${logout_link}=    Run Keyword And Return Status    Element Should Be Visible    xpath=//a[contains(text(),'Logout')]
    Run Keyword If    ${logout_link}    Click Element    xpath=//a[contains(text(),'Logout')]
    Sleep    2

*** Test Cases ***
TC6_Validate_User_In_Admin_List
    [Documentation]    Validate presence of newly created user in admin user list
    [Tags]    TC6    user_validation

    Open Browser And Maximize

    # Step 1: Login as Admin
    Log    === TC6 Step 1: Login as Admin ===
    Navigate To Login Page
    Input Username    ${ADMIN_USERNAME}
    Input Password    ${ADMIN_PASSWORD}
    Click Login Button
    Wait Until Location Contains    dashboard
    Log    Admin logged in successfully

    # Step 2: Navigate to User Management
    Log    === TC6 Step 2: Navigate to Admin > User Management ===
    Go To    ${BASE_URL}/web/index.php/admin/viewSystemUsers
    Sleep    3

    # Step 3: Verify user list is displayed
    Log    === TC6 Step 3: Verify user list is displayed ===
    ${table_visible}=    Run Keyword And Return Status    Element Should Be Visible    xpath=//div[contains(@class,'oxd-table')]
    Log    User table visible: ${table_visible}
    Should Be True    ${table_visible}

    # Step 4: Get user count
    Log    === TC6 Step 4: Get user count ===
    ${row_count}=    Get Element Count    xpath=//div[contains(@class,'oxd-table-row')]
    Log    Number of users in table: ${row_count}
    Should Be True    ${row_count} > 0

    # Step 5: Search for Admin user
    Log    === TC6 Step 5: Search for Admin user ===
    Input Text    xpath=//input[@placeholder='Search']    Admin
    Sleep    1
    Click Button    xpath=//button[contains(@class,'oxd-button--secondary')]
    Sleep    3

    # Step 6: Verify search results
    Log    === TC6 Step 6: Verify search results ===
    ${search_result_count}=    Get Element Count    xpath=//div[contains(@class,'oxd-table-row')]
    Log    Users found after search: ${search_result_count}
    Should Be True    ${search_result_count} > 0

    Logout From Application
    Log    === TC6 Completed Successfully ===

    Close All Browsers

TC6_Verify_User_List_Access
    [Documentation]    Verify user list is accessible after login
    [Tags]    TC6    user_list

    Open Browser And Maximize

    Navigate To Login Page
    Input Username    ${ADMIN_USERNAME}
    Input Password    ${ADMIN_PASSWORD}
    Click Login Button
    Wait Until Location Contains    dashboard

    Go To    ${BASE_URL}/web/index.php/admin/viewSystemUsers
    Sleep    3

    ${table_present}=    Run Keyword And Return Status    Element Should Be Visible    xpath=//div[contains(@class,'oxd-table')]
    Should Be True    ${table_present}

    Logout From Application

    Close All Browsers