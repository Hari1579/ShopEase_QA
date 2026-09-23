# JIRA-101 - Login Test Cases

## TC001 - Valid Login

**Test Scenario:**  
Verify that a registered user can log in with a valid email and password.

**Precondition:**  
A registered ShopEase user exists.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter the registered email.
3. Enter the valid password.
4. Click the Login button.

**Test Data:**
- Email: user1@test.com
- Password: Test@123

**Expected Result:**  
User should log in successfully and navigate to the expected page.

**Actual Result:**  
User successfully logged in and was navigated to the Secure Area page. The message "You logged into a secure area!" was displayed.

**Status:**  
Pass


## TC002 - Invalid Password

**Test Scenario:**  
Verify login with a valid email and invalid password.

**Precondition:**  
A registered ShopEase user exists.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter the registered email.
3. Enter an incorrect password.
4. Click the Login button.

**Test Data:**
- Email: user1@test.com
- Password: Wrong@123

**Expected Result:**  
"Invalid email or password" should be displayed.

**Actual Result:**  
"Your password is invalid!" was displayed and the user remained on the Login Page.

**Status:**  
Pass


## TC003 - Unregistered Email

**Test Scenario:**  
Verify login with an unregistered email and valid password.

**Precondition:**  
The email used for testing is not registered in ShopEase.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter an unregistered email.
3. Enter a valid password.
4. Click the Login button.

**Test Data:**
- Email: unknown@test.com
- Password: Test@123

**Expected Result:**  
"Invalid email or password" should be displayed.

**Actual Result:**  
"Your username is invalid!" was displayed and the user remained on the Login Page.

**Status:**  
Pass


## TC004 - Empty Email

**Test Scenario:**  
Verify login when the email field is empty.

**Precondition:**  
ShopEase login page is available.

**Test Steps:**
1. Open the ShopEase login page.
2. Leave the email field empty.
3. Enter a valid password.
4. Click the Login button.

**Test Data:**
- Email: Empty
- Password: Test@123

**Expected Result:**  
Email mandatory-field validation should be displayed and login should not be submitted.

**Actual Result:**  
"Your username is invalid!" was displayed and the user remained on the Login Page.

**Status:**  
Pass


## TC005 - Empty Password

**Test Scenario:**  
Verify login when the password field is empty.

**Precondition:**  
ShopEase login page is available.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter a valid registered email.
3. Leave the password field empty.
4. Click the Login button.

**Test Data:**
- Email: user1@test.com
- Password: Empty

**Expected Result:**  
Password mandatory-field validation should be displayed and login should not be submitted.

**Actual Result:**  
"Your password is invalid!" was displayed and the user remained on the Login Page.

**Status:**  
Fail


## TC006 - Both Fields Empty

**Test Scenario:**  
Verify login when both email and password fields are empty.

**Precondition:**  
ShopEase login page is available.

**Test Steps:**
1. Open the ShopEase login page.
2. Leave the email field empty.
3. Leave the password field empty.
4. Click the Login button.

**Test Data:**
- Email: Empty
- Password: Empty

**Expected Result:**  
Required-field validation should be displayed and login should not be submitted.

**Actual Result:**  

"Your username is invalid!" was displayed and the user remained on the Login Page.


**Status:**  
Fail


## TC007 - Invalid Email Format

**Test Scenario:**  
Verify login with an invalid email format.

**Precondition:**  
ShopEase login page is available.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter an invalid email format.
3. Enter a valid password.
4. Click the Login button.

**Test Data:**
- Email: hari@
- Password: Test@123

**Expected Result:**  
Email format validation should be displayed and login should not be submitted.

**Actual Result:**  
"Your username is invalid!" was displayed and the user remained on the Login Page.

**Status:**  
Pass


## TC008 - Password Masking

**Test Scenario:**  
Verify that the password is masked when entered.

**Precondition:**  
ShopEase login page is available.

**Test Steps:**
1. Open the ShopEase login page.
2. Click the password field.
3. Enter a password.

**Test Data:**
- Password: Test@123

**Expected Result:**  
The password characters should be masked and should not be displayed as plain text.

**Actual Result:**  
Password was displayed in masked form and was not visible as plain text.

**Status:**  
Pass


## TC009 - Login Button

**Test Scenario:**  
Verify that the Login button is available and can be used to submit the login form.

**Precondition:**  
ShopEase login page is available.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter valid login credentials.
3. Verify that the Login button is displayed.
4. Click the Login button.

**Test Data:**
- Email: user1@test.com
- Password: Test@123

**Expected Result:**  
Login button should be visible and clickable, and the login request should be submitted.

**Actual Result:**  
Login button was visible and clickable. Clicking it successfully submitted the login request and logged the user in.

**Status:**  
Pass


## TC010 - Successful Navigation

**Test Scenario:**  
Verify that the user is navigated to the expected page after successful login.

**Precondition:**  
A registered ShopEase user exists.

**Test Steps:**
1. Open the ShopEase login page.
2. Enter the registered email.
3. Enter the valid password.
4. Click the Login button.
5. Observe the page after successful login.

**Test Data:**
- Email: user1@test.com
- Password: Test@123

**Expected Result:**  
User should be successfully logged in and navigated to the expected page.

**Actual Result:**  
User successfully logged in and was navigated to the Secure Area page. The message "You logged into a secure area!" was displayed.

**Status:**  
Pass