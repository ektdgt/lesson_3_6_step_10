import time

def test_checking_button_on_french(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    text_on_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').text
    assert text_on_button == 'Ajouter au panier'
