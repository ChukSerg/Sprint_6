from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_button_head = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    order_button_body = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    yandex_button_head = (By.XPATH, "//img[@alt='Yandex']")
    project_button_head = (By.XPATH, "//img[@alt='Scooter']")
    title_dzen = (By.CLASS_NAME, "desktop-base-header__logo-tA")
    title_order_form = (By.XPATH, ".//div[text()='Для кого самокат']")
    title_next_page_order_form = (By.XPATH, ".//div[text()='Про аренду']")
    title_confirm_form = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    title_order_confirm = (By.XPATH, "//div[text()='Заказ оформлен']")
    button_confirm_form = (By.XPATH, "//button[text()='Да']")
    data_name = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    data_surname = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    data_address = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    data_metro_station = (By.XPATH, ".//input[contains(@placeholder, 'Станция метро')]")
    metro_station_1 = (By.XPATH, '//div[@class="select-search__select"]//div[text()="Черкизовская"]')
    metro_station_2 = (By.XPATH, "//div[@class='select-search__select']//div[text()='Сокольники']")
    data_phone = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    order_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    order_period_button = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    order_second_day_period = (By.XPATH, "//div[text()='двое суток']")
    order_forth_day_period = (By.XPATH, "//div[text()='четверо суток']")
    button_next = (By.XPATH, ".//button[text()='Далее']")
    button_order = (By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Заказать']")
    data_order_first_page = [
        ['Егор', 'Хохлов', 'Первомайская, 69', '+79999999999', '10.05.2024'],
        ['Иван', 'Николаев', 'Ленина, 95', '+78888888888', '12.05.2024']
    ]

