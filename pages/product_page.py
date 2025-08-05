from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self): #этот метод сохраняет имя и стоимость книги, затем находит кнопку "добавить в корзину" и нажимает ее
        button_add = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button_add.click()

    def correct_message_about_adding_to_cart(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        message_about_adding_to_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT_ABOUT_ADDING_TO_CART).text
        expected_text = f"{title} был добавлен в вашу корзину."
        assert expected_text in message_about_adding_to_cart, f"Ожидали '{expected_text}', но получили '{message_about_adding_to_cart}'"

    def correct_message_about_the_cart_cost(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        message_about_adding_the_cart_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT_ABOUT_THE_CART_COST).text
        expected_text = f"Стоимость корзины теперь составляет {price}"
        assert expected_text in message_about_adding_the_cart_cost, f"Ожидали '{expected_text}', но получили '{message_about_adding_the_cart_cost}'"


