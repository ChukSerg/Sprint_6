import allure
import pytest
from selenium import webdriver

from pages.orders_page import OrdersPageScooter
from locators.order_page_locators import OrderPageLocators


class TestOrderPages:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        cls.driver = webdriver.Firefox(options=options)

    @allure.title('Тестирование заказа самоката')
    @allure.description(
        'Кликнуть на одну из кнопок Заказать > заполнить форму заказа > появляется окно содержащее Заказ оформлен'
    )
    @pytest.mark.parametrize('order_button, data_first_page, metro_station, duration', [
        [OrderPageLocators.order_button_head, OrderPageLocators.data_order_first_page[0],
         OrderPageLocators.metro_station_1, OrderPageLocators.order_second_day_period],
        [OrderPageLocators.order_button_body, OrderPageLocators.data_order_first_page[1],
         OrderPageLocators.metro_station_2, OrderPageLocators.order_forth_day_period]
    ])
    def test_check_order_scooter(self, order_button, data_first_page, metro_station, duration):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrdersPageScooter(self.driver)
        order_page.order_button_click(order_button)
        order_page.wait_open_form(OrderPageLocators.title_order_form)
        order_page.set_data_first_page_order(data_first_page, metro_station)
        order_page.button_click(OrderPageLocators.button_next)
        order_page.wait_open_form(OrderPageLocators.title_next_page_order_form)
        order_page.set_data_second_page_order(data_first_page, duration)
        order_page.button_click(OrderPageLocators.button_order)
        order_page.wait_open_form(OrderPageLocators.title_confirm_form)
        order_page.button_click(OrderPageLocators.button_confirm_form)
        order_page.wait_open_form(OrderPageLocators.title_order_confirm)
        assert order_page.driver.find_element(*OrderPageLocators.title_order_confirm).is_displayed()

    @allure.title('Тест перехода на главную страницу Яндекс Самокат')
    @allure.description('Клик на лого Самокат в хедере формы заказа > переход на главную страницу Яндекс Самокат')
    def test_redirect_on_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        order_page = OrdersPageScooter(self.driver)
        order_page.button_click(OrderPageLocators.project_button_head)
        current_url = self.driver.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Тест перехода на страницу Dzen')
    @allure.description('Клик по лого Яндекс в хедере > переход на страницу Dzen')
    def test_redirect_dzen_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        order_page = OrdersPageScooter(self.driver)
        order_page.button_click(OrderPageLocators.yandex_button_head)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        order_page.wait_open_form(OrderPageLocators.title_dzen)
        current_url = self.driver.current_url
        assert current_url.__contains__("https://dzen.ru/?yredirect=true"), 'Главная страница "Дзен" не открылась'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
