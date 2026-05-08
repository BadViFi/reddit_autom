import allure
from base.base_page import BasePage
import time
class HomePage(BasePage):
    PAGE_URL = "https://www.reddit.com/"
    NEWS_LOCTOR = 'a[href="/news/"]'
    def __init__(self, page):
        super().__init__(page)
        
    def open_popular(self):
        self.page.get_by_role("link", name="Popular").click()
        time.sleep(1)
        
    def open_news(self):
        self.page.locator(self.NEWS_LOCTOR).click()
        time.sleep(1)
