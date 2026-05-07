import pytest
from playwright.sync_api import sync_playwright
import pytest
import os
from dotenv import load_dotenv
import os
import time
load_dotenv()
import allure

@pytest.fixture(scope="session")
def auth_state():
    if os.path.exists("auth.json"):
        return

    username = os.getenv("REDDIT_USERNAME")
    password = os.getenv("REDDIT_PASSWORD")

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://reddit.com")
        try:
            google_iframe = page.frame_locator("iframe[src*='accounts.google.com/gsi/iframe']")
            close_button = google_iframe.locator("#close, [role='button']")
            close_button.wait_for(state="visible", timeout=3000)
            close_button.click()
        except:
            pass
        page.get_by_role("link", name="Log In").click()
        page.get_by_role("textbox", name="Email or username").fill(username)
        page.get_by_role("textbox", name="Password").fill(password)

        page.locator(".login").click()
        page.locator("#header-action-item-chat-button").wait_for()
        time.sleep(3)
        context.storage_state(path="auth.json")
        browser.close()
        
        
@pytest.fixture(autouse=True)
@allure.step("Setupping")
def setup(auth_state):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(storage_state = "auth.json")
        page = context.new_page()
        page.goto("https://reddit.com")
        yield page
        browser.close()