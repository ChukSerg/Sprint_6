import pytest
from selenium import webdriver

from data.data_order_page import DataOrderPage


@pytest.fixture()
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(DataOrderPage.MAIN_PAGE_URL)

    yield driver

    driver.quit()
