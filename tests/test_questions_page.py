import allure
import pytest

from pages.questions_page import QuestionsPageSamokat


class TestQuestionPages:
    @allure.title('Тест открытия ответов в Вопросах о важном')
    @allure.description('Клик по вопросам по очереди > открываются ответы на вопросы по очереди')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_questions_open_text(self, driver, index):
        question_page = QuestionsPageSamokat(driver)
        current_answer = question_page.click_element(index)
        expected_answer = question_page.take_answer(index)
        assert current_answer == expected_answer
