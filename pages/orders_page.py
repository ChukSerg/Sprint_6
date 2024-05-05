import allure
from selenium.webdriver import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrdersPageScooter(BasePage):
    @allure.step('Нажатие на кнопку Заказать {button_xpath}')
    def order_button_click(self, button_xpath):
        self.scroll_element(button_xpath)
        self.button_click(button_xpath)

    @allure.step('Вводим данные станции метро {locator}')
    def set_data_metro_station(self, locator):
        self.driver.find_element(*OrderPageLocators.data_metro_station).click()
        self.scroll_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Заполнение первой страницы формы заказа')
    def set_data_first_page_order(self, data_order_first_page, metro_station):
        self.wait_open_form(OrderPageLocators.title_order_form)
        self.driver.find_element(*OrderPageLocators.data_name).send_keys(data_order_first_page[0])
        self.driver.find_element(*OrderPageLocators.data_surname).send_keys(data_order_first_page[1])
        self.driver.find_element(*OrderPageLocators.data_address).send_keys(data_order_first_page[2])
        self.set_data_metro_station(metro_station)
        self.driver.find_element(*OrderPageLocators.data_phone).send_keys(data_order_first_page[3])
        self.button_click(OrderPageLocators.button_next)

    @allure.step('Выбор продолжительности заказа')
    def set_duration(self, duration):
        self.button_click(OrderPageLocators.order_period_button)
        self.button_click(duration)

    @allure.step('Заполнение второй страницы формы заказа')
    def set_data_second_page_order(self, data_order_first_page, duration):
        self.wait_open_form(OrderPageLocators.title_next_page_order_form)
        self.driver.find_element(*OrderPageLocators.order_date).send_keys(data_order_first_page[4])
        self.driver.find_element(*OrderPageLocators.order_date).send_keys(Keys.ENTER)
        self.set_duration(duration)
        self.button_click(OrderPageLocators.button_order)
        self.wait_open_form(OrderPageLocators.title_confirm_form)
        self.button_click(OrderPageLocators.button_confirm_form)
        self.wait_open_form(OrderPageLocators.title_order_confirm)
