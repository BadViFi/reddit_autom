from pages.home_page import HomePage
from pages.navbar_items.popular_page import PopularPage
import pytest


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request, pw_page):
        request.cls.home_page = HomePage(pw_page)
        request.cls.popular_page = PopularPage(pw_page)
        request.cls.page = pw_page
