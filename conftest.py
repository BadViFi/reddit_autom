from data.redit_user import ReditUser

import pytest
from playwright.sync_api import sync_playwright
import pytest
import os
import time
import allure

@pytest.fixture(scope="session")
def auth_state():
    if os.path.exists("auth.json"):
        return
    red_user = ReditUser()

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        page.goto("https://reddit.com")

        try:
            google_iframe = page.frame_locator(
                "iframe[src*='accounts.google.com/gsi/iframe']"
            )
            close_button = google_iframe.locator("#close, [role='button']")
            close_button.wait_for(state="visible", timeout=3000)
            close_button.click()
        except:
            pass

        page.get_by_role("link", name="Log In").click()
        page.get_by_role("textbox", name="Email or username").fill(red_user.username)
        page.get_by_role("textbox", name="Password").fill(red_user.password)

        page.locator(".login").click()
        page.locator("#header-action-item-chat-button").wait_for()

        context.storage_state(path="auth.json")
        browser.close()
        
        
@pytest.fixture(autouse=True)
def pw_page(auth_state):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(storage_state="auth.json",viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        page.goto("https://reddit.com")

        yield page

        context.close()
        browser.close()