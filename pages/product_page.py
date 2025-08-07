from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_not_be_success_message(self): #проверка что на странице нет плашки с сообщением об успешном добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_TEXT_ABOUT_ADDING_TO_CART), \
            "Success message is presented, but should not be"
    def add_product_to_basket(self): #этот метод находит кнопку "добавить в корзину" и нажимает ее
        button_add = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button_add.click()

    def correct_message_about_adding_to_cart(self): #проверяем что текст сообщения в плашке корректный
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        message_about_adding_to_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT_ABOUT_ADDING_TO_CART).text
        expected_text = f"{title} был добавлен в вашу корзину."
        assert expected_text in message_about_adding_to_cart, f"Ожидали '{expected_text}', но получили '{message_about_adding_to_cart}'"

    def correct_message_about_the_cart_cost(self): #проверяем что стоимость корзины в плашке указана корректно
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        message_about_adding_the_cart_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_TEXT_ABOUT_THE_CART_COST).text
        expected_text = f"Стоимость корзины теперь составляет {price}"
        assert expected_text in message_about_adding_the_cart_cost, f"Ожидали '{expected_text}', но получили '{message_about_adding_the_cart_cost}'"

    def success_message_is_disappeared(self): #проверка, что сообщение исчезло (тест должен падать, так как сообщение не должно исчезать)
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_TEXT_ABOUT_ADDING_TO_CART), \
            "Success message is presented, but should not be"
