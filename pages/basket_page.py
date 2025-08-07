from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    #Ожидаем, что в корзине нет товаров
    def no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "There should be no items in the basket"

    #проверяем, что в корзине есть сообщение о том, что она пустая
    def should_be_message_about_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_BASKET_EMPTY), "message about basket empty is not presented"
