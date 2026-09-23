import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(params=["chromium", "firefox"])
def page(request):

    with sync_playwright() as p:

        browser_type = getattr(p, request.param)

        if os.getenv("JENKINS_URL"):
            browser = browser_type.launch(headless=True)
        else:
            browser = browser_type.launch(headless=False)

        page = browser.new_page()

        page.goto("https://practice.expandtesting.com/login")

        yield page

        browser.close()

'''import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(params=["chromium", "firefox",])
def page(request):

    with sync_playwright() as p:

        browser_type = getattr(p, request.param)

        browser = browser_type.launch(headless=False)

        page = browser.new_page()

        page.goto("https://practice.expandtesting.com/login")

        yield page

        browser.close()'''

#If we want to run in a single browser, we can use the below code snippet instead of the above code snippet.
'''import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://practice.expandtesting.com/login")

        yield page

        browser.close()'''