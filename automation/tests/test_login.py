from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# TC001 - Valid Login
def test_valid_login():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("practice")
    time.sleep(3)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-login"))
    )

    time.sleep(3)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        login_button
    )

    time.sleep(2)

    login_button.click()
    time.sleep(5)

    success_message = driver.find_element(By.TAG_NAME, "h1")

    assert "Secure Area" in success_message.text

    driver.quit()


# TC002 - Invalid Password
def test_invalid_password():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("practice")
    time.sleep(3)

    password = driver.find_element(By.ID, "password")
    password.send_keys("WrongPassword123")
    time.sleep(3)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-login"))
    )

    time.sleep(3)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        login_button
    )

    time.sleep(2)

    login_button.click()
    time.sleep(5)

    # Verify invalid password error message
    error_message = driver.find_element(By.ID, "flash")

    assert "Your password is invalid!" in error_message.text

    driver.quit()

# TC003 - Invalid Username

def test_invalid_username():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("invalid_user")
    time.sleep(3)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-login"))
    )

    time.sleep(3)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        login_button
    )

    time.sleep(2)

    login_button.click()
    time.sleep(5)


    # Get error message
    error_message = driver.find_element(By.ID, "flash")

    # Validate error message
    assert "Your username is invalid!" in error_message.text

    # We will inspect the actual error message here
    driver.quit()

# TC007 - Invalid Email Format
def test_invalid_email_format():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("hari@")
    time.sleep(3)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-login"))
    )

    time.sleep(3)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        login_button
    )

    time.sleep(2)

    login_button.click()
    time.sleep(5)

    error_message = driver.find_element(By.ID, "flash")

    assert "Your username is invalid!" in error_message.text

    driver.quit()

# TC008 - Password Masking
def test_password_masking():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    password = driver.find_element(By.ID, "password")

    password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    # Verify password field is masked
    assert password.get_attribute("type") == "password"

    time.sleep(2)

    driver.quit()

# TC009 - Login Button
def test_login_button():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("practice")
    time.sleep(3)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-login"))
    )

    # Verify Login button is displayed and enabled
    assert login_button.is_displayed()
    assert login_button.is_enabled()

    time.sleep(3)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        login_button
    )

    time.sleep(2)

    # Click Login button
    login_button.click()

    time.sleep(5)

    # Verify login was successful
    success_message = driver.find_element(By.TAG_NAME, "h1")

    assert "Secure Area" in success_message.text

    driver.quit()

# TC010 - Successful Navigation
def test_successful_navigation():

    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")
    time.sleep(3)

    driver.maximize_window()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("practice")
    time.sleep(3)

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-login"))
    )

    time.sleep(3)

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        login_button
    )

    time.sleep(2)

    login_button.click()
    time.sleep(5)

    # Verify successful navigation
    assert "secure" in driver.current_url.lower()

    success_message = driver.find_element(By.TAG_NAME, "h1")

    assert "Secure Area" in success_message.text

    driver.quit()