import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Navbar Functionality")
class TestProfileFeature(BaseTest):
    @allure.title("Click navbar")
    @pytest.mark.smoke

    def test_click_nav_items(self):
        self.home_page.is_opened()
        self.home_page.open_popular()
        self.home_page.open_news()
        
        self.home_page.make_screenshot("Success")