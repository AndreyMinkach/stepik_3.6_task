import time


def test_button_add_to_basket_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    button_add_to_basket = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    if len(button_add_to_basket) == 0:
        print('Button "Add to basket" not axist on page!')
