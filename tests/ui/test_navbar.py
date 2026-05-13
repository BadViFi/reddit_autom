import allure
import pytest
from base.base_test import BaseTest
@allure.feature("Navbar Functionality")
@pytest.mark.navbar
class TestNavbar(BaseTest):
    @allure.title("Click navbar")

    def test_click_nav_items(self):
        self.home_page.is_opened()
        self.home_page.open_popular()
        self.home_page.open_news()
        
        self.home_page.make_screenshot("Navbar Succes")
        
        
@allure.feature("Popular Page")
@pytest.mark.popular
class TestPopular_Article(BaseTest):
    @allure.title("Insepct Popular")

    def test_popular_interraction(self):
        self.popular_page.open()
        self.popular_page.is_opened()
        self.popular_page.get_first_article()
        self.popular_page.type_comment()
        self.popular_page.make_screenshot("Popular Succes")