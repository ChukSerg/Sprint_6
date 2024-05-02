import allure
import pytest
from selenium import webdriver

from pages.questions_page import QuestionsPageSamokat


class TestQuestionPages:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        cls.driver = webdriver.Firefox(options=options)

    @allure.title('Тест открытия ответов в Вопросах о важном')
    @allure.description('Клик по вопросам по очереди > открываются ответы на вопросы по очереди')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_questions_open_text(self, index):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        question_page = QuestionsPageSamokat(self.driver)
        question_page.wait_for_page_open()
        question_page.scroll_questions_title()
        current_answer = question_page.click_element(index)
        expected_answer = question_page.take_answer(index)
        assert current_answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
