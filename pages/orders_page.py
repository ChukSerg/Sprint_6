import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


class OrdersPageScooter:
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку {button_xpath}')
    def button_click(self, button_xpath):
        self.driver.find_element(*button_xpath).click()

    @allure.step('Нажатие на кнопку Заказать {button_xpath}')
    def order_button_click(self, button_xpath):
        element = self.driver.find_element(*button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_open_form(button_xpath)
        element.click()

    @allure.step('Ожидаем открытие раздела {form_title}')
    def wait_open_form(self, form_title):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(form_title))

    @allure.step('Вводим данные {data}')
    def set_data(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Вводим данные станции метро {data}')
    def set_data_metro_station(self, data):
        self.driver.find_element(*OrderPageLocators.data_metro_station).click()
        element = self.driver.find_element(*data)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(data))
        self.driver.find_element(*data).click()

    @allure.step('Заполнение первой страницы формы заказа')
    def set_data_first_page_order(self, data_order_first_page, metro_station):
        self.set_data(OrderPageLocators.data_name, data_order_first_page[0])
        self.set_data(OrderPageLocators.data_surname, data_order_first_page[1])
        self.set_data(OrderPageLocators.data_address, data_order_first_page[2])
        self.set_data_metro_station(metro_station)
        self.set_data(OrderPageLocators.data_phone, data_order_first_page[3])

    @allure.step('Выбор продолжительности заказа')
    def set_duration(self, duration):
        self.button_click(OrderPageLocators.order_period_button)
        self.button_click(duration)

    @allure.step('Заполнение второй страницы формы заказа')
    def set_data_second_page_order(self, data_order_first_page, duration):
        self.set_data(OrderPageLocators.order_date, data_order_first_page[4])
        self.set_data(OrderPageLocators.order_date, Keys.ENTER)
        self.set_duration(duration)
