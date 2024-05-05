import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку {button_xpath}')
    def button_click(self, button_xpath):
        self.driver.find_element(*button_xpath).click()

    @allure.step('Ожидаем открытие раздела {form_title}')
    def wait_open_form(self, form_title):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(form_title))

    @allure.step('Прокрутка до нужного элемента {locator}')
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_open_form(locator)
