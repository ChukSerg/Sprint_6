import allure
from selenium.webdriver.common.by import By

from locators.question_page_locators import QuestionPageLocators
from data.data_question_page import DataQuestions
from pages.base_page import BasePage


class QuestionsPageSamokat(BasePage):
    @allure.step('Получаем локатор вопроса')
    def take_question_locator(self, index):
        return By.XPATH, f".//div[@id='accordion__heading-{index}']"

    @allure.step('Получаем локатор ответа')
    def take_answer_locator(self, index):
        return By.XPATH, f".//div[@id='accordion__panel-{index}']"

    @allure.step('Получаем ожидаемый текст ответа')
    def take_answer(self, index):
        return DataQuestions.expected_answers[index]

    @allure.step('Шаг нажатия на вопрос и получения ответа')
    def click_element(self, index):
        self.wait_open_form(QuestionPageLocators.head_title)
        self.scroll_element(QuestionPageLocators.question_title)
        self.driver.find_element(*self.take_question_locator(index)).click()
        self.wait_open_form(self.take_answer_locator(index))
        return self.driver.find_element(*self.take_answer_locator(index)).text
