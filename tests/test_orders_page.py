import allure
import pytest

from pages.orders_page import OrdersPageScooter
from locators.order_page_locators import OrderPageLocators
from data.data_order_page import DataOrderPage


class TestOrderPages:
    @allure.title('Тестирование заказа самоката')
    @allure.description(
        'Кликнуть на одну из кнопок Заказать > заполнить форму заказа > появляется окно содержащее Заказ оформлен'
    )
    @pytest.mark.parametrize('order_button, data_first_page, metro_station, duration', [
        [OrderPageLocators.order_button_head, DataOrderPage.data_order_first_page[0],
         OrderPageLocators.metro_station_1, OrderPageLocators.order_second_day_period],
        [OrderPageLocators.order_button_body, DataOrderPage.data_order_first_page[1],
         OrderPageLocators.metro_station_2, OrderPageLocators.order_forth_day_period]
    ])
    def test_check_order_scooter(self, driver, order_button, data_first_page, metro_station, duration):
        order_page = OrdersPageScooter(driver)
        order_page.order_button_click(order_button)
        order_page.set_data_first_page_order(data_first_page, metro_station)
        order_page.set_data_second_page_order(data_first_page, duration)
        assert order_page.driver.find_element(*OrderPageLocators.title_order_confirm).is_displayed()

    @allure.title('Тест перехода на главную страницу Яндекс Самокат')
    @allure.description('Клик на лого Самокат в хедере формы заказа > переход на главную страницу Яндекс Самокат')
    def test_redirect_on_main_page(self, driver):
        driver.get(DataOrderPage.ORDER_PAGE_URL)
        order_page = OrdersPageScooter(driver)
        order_page.button_click(OrderPageLocators.project_button_head)
        current_url = driver.current_url
        assert current_url == DataOrderPage.MAIN_PAGE_URL

    @allure.title('Тест перехода на страницу Dzen')
    @allure.description('Клик по лого Яндекс в хедере > переход на страницу Dzen')
    def test_redirect_dzen_page(self, driver):
        order_page = OrdersPageScooter(driver)
        order_page.button_click(OrderPageLocators.yandex_button_head)
        driver.switch_to.window(driver.window_handles[-1])
        order_page.wait_open_form(OrderPageLocators.title_dzen)
        current_url = driver.current_url
        assert current_url.__contains__(DataOrderPage.DZEN_PAGE_URL), 'Главная страница "Дзен" не открылась'
