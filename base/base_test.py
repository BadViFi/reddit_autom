from pages.home_page import HomePage
from data.redit_user import ReditUser
import pytest


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request, pw_page):
        request.cls.home_page = HomePage(pw_page)
        request.cls.page = pw_page
