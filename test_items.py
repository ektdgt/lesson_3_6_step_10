import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def test_checking_button_is_present(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert visibility_of_element_located(browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')), 'Button should be present'
