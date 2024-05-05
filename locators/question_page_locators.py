from selenium.webdriver.common.by import By


class QuestionPageLocators:
    question_title = (By.XPATH, ".//div[text()='Вопросы о важном']")
    head_title = (By.XPATH, ".//img[@alt='Scooter']")
