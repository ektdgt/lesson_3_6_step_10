import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checking_button_is_present(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
    )
    assert button.is_displayed(), 'Button should be present'
    # Следующий assert всегда будет приводить к ошибке, т.к. условие всегда ложно (False).
    # assert False, "Не удалось найти кнопку 'ДОБАВИТЬ В КОРЗИНУ' в течение 10 секунд"
