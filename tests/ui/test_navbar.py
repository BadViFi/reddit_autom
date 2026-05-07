import time
import allure
def test_nav_items(setup):
    page = setup
    
    page.get_by_role("link", name="Popular").click()
    time.sleep(2)