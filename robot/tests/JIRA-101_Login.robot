*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***

TC001 - Valid Login
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Text    id=username    practice
    Input Password    id=password    SuperSecretPassword!
    Scroll Element Into View    id=submit-login
    Wait Until Element Is Visible    id=submit-login
    Execute JavaScript    document.getElementById('submit-login').click();
    Wait Until Page Contains    Secure Area
    Close Browser


TC002 - Invalid Password
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Text    id=username    practice
    Input Password    id=password    WrongPassword123
    Execute JavaScript    document.getElementById('submit-login').click();
    Wait Until Page Contains    Your password is invalid!
    Close Browser


TC003 - Unregistered Email
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Text    id=username    unknown@test.com
    Input Password    id=password    SuperSecretPassword!
    Execute JavaScript    document.getElementById('submit-login').click();
    Wait Until Page Contains    Your username is invalid!
    Close Browser


TC004 - Empty Email
    [Tags]    skipped
    [Documentation]    Skipped because practice website behavior is not being automated for this scenario.
    Skip    Not automated for this practice website.


TC005 - Empty Password
    [Tags]    skipped
    [Documentation]    Skipped because practice website behavior is not being automated for this scenario.
    Skip    Not automated for this practice website.


TC006 - Both Fields Empty
    [Tags]    skipped
    [Documentation]    Skipped because practice website behavior is not being automated for this scenario.
    Skip    Not automated for this practice website.


TC007 - Invalid Email Format
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Text    id=username    hari@
    Input Password    id=password    SuperSecretPassword!
    Execute JavaScript    document.getElementById('submit-login').click();
    Wait Until Page Contains    Your username is invalid!
    Close Browser


TC008 - Password Masking
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Password    id=password    SuperSecretPassword!
    ${input_type}=    Get Element Attribute    id=password    type
    Should Be Equal    ${input_type}    password
    Close Browser


TC009 - Login Button
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Text    id=username    practice
    Input Password    id=password    SuperSecretPassword!
    Wait Until Element Is Visible    id=submit-login
    Element Should Be Enabled    id=submit-login
    Execute JavaScript    document.getElementById('submit-login').click();
    Wait Until Page Contains    Secure Area
    Close Browser


TC010 - Successful Navigation
    Open Browser    https://practice.expandtesting.com/login    chrome
    Maximize Browser Window
    Input Text    id=username    practice
    Input Password    id=password    SuperSecretPassword!
    Execute JavaScript    document.getElementById('submit-login').click();
    Wait Until Page Contains    Secure Area
    ${current_url}=    Get Location
    Should Contain    ${current_url}    secure
    Close Browser