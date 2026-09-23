def test_valid_login(page):

    page.locator("#username").fill("practice")
    page.wait_for_timeout(3000)

    page.locator("#password").fill("SuperSecretPassword!")
    page.wait_for_timeout(3000)

    page.locator("#submit-login").click()
    page.wait_for_timeout(3000)

    success_message = page.locator("h1")

    assert "Secure Area" in success_message.inner_text()


def test_invalid_password(page):

    page.locator("#username").fill("practice")
    page.wait_for_timeout(3000)

    page.locator("#password").fill("WrongPassword123")
    page.wait_for_timeout(3000)

    page.locator("#submit-login").click()
    page.wait_for_timeout(3000)

    error_message = page.locator("#flash")

    assert "Your password is invalid!" in error_message.inner_text()


def test_unregistered_email(page):

    page.locator("#username").fill("unknown@test.com")
    page.wait_for_timeout(3000)

    page.locator("#password").fill("SuperSecretPassword!")
    page.wait_for_timeout(3000)

    page.locator("#submit-login").click()
    page.wait_for_timeout(3000)

    error_message = page.locator("#flash")

    assert "Your username is invalid!" in error_message.inner_text()