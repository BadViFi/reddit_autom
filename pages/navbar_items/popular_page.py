import allure
from base.base_page import BasePage
import time

class PopularPage(BasePage):
    PAGE_URL = "https://www.reddit.com/r/popular/"
    ARTICLES_SELECTOR = "article.w-full"
    TEXT_ARIA_LOCAT = "comment-composer-host.nd\\:hidden"
    FORM_CONTAINER = ".cursor-text"
    FORM_LOCATOR = "#main-content"
    SUBMIT_BTN_SELECTOR = "#comment-composer-submit-button"

    def get_first_article(self):
        article = self.page.locator(self.ARTICLES_SELECTOR).nth(0)
        article.wait_for(state="visible", timeout=3000)

        href = article.nth(0).locator("a").nth(0).get_attribute("href")
        self.page.goto(f"{self.BASE_URL}{href}")

        time.sleep(3)
        
    def type_comment(self):
        
        text_area = self.page.locator(
            self.TEXT_ARIA_LOCAT
        )
        text_area.scroll_into_view_if_needed()
        text_area.click()
        fill_input = self.FORM_CONTAINER
        self.page.locator(self.FORM_LOCATOR).get_by_role("textbox").fill("Great job!")
        self.page.locator(self.SUBMIT_BTN_SELECTOR).click()
        time.sleep(5)