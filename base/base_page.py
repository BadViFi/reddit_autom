import allure
from allure_commons.types import AttachmentType
class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.page.goto(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            print(type(self.page))
            self.page.wait_for_url(self.PAGE_URL)

    def make_screenshot(self, screenshot_name):

        allure.attach(
            body=self.page.screenshot(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )