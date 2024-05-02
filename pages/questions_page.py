import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.question_page_locators import QuestionPageLocators


class QuestionsPageSamokat:
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокручиваем до заголовка вопросов')
    def scroll_questions_title(self):
        element = self.driver.find_element(*QuestionPageLocators.question_title)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем локатор вопроса')
    def take_question_locator(self, index):
        return By.XPATH, f".//div[@id='accordion__heading-{index}']"

    @allure.step('Получаем локатор ответа')
    def take_answer_locator(self, index):
        return By.XPATH, f".//div[@id='accordion__panel-{index}']"

    @allure.step('Получаем ожидаемый текст ответа')
    def take_answer(self, index):
        return QuestionPageLocators.expected_answers[index]

    @allure.step('Шаг нажатия на вопрос и получения ответа')
    def click_element(self, index):
        self.driver.find_element(*self.take_question_locator(index)).click()
        self.wait_for_page_open(self.take_answer_locator(index))
        return self.driver.find_element(*self.take_answer_locator(index)).text

    @allure.step('Ожидание появления элемента')
    def wait_for_page_open(self, locator=QuestionPageLocators.head_title):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator)
        )
