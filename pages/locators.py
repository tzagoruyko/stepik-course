from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# class MainPageLocators():

class BasketPageLocators():
    MESSAGE_ABOUT_BASKET_EMPTY = (By.CSS_SELECTOR, ".content p")
    ITEMS = (By.CSS_SELECTOR, ".basket-items")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, ".register_form input[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".register_form input[name='registration-password1']")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, ".register_form input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_TEXT_ABOUT_ADDING_TO_CART = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    MESSAGE_TEXT_ABOUT_THE_CART_COST = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p")
