from .base import *

class CheckoutPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.CHECKOUT_BTN = "#checkout"
        self.CART_ITEM_NAME = ".inventory_item_name"
        self.FIRST_NAME_INPUT = "#first-name"
        self.LAST_NAME_INPUT = "#last-name"
        self.POSTAL_CODE_INPUT = "#postal-code"
        self.CONTINUE_BTN = "#continue"
        self.PRICE_TOTAL_TXT = ".summary_total_label"
        self.FINISH_BTN = "#finish"
        self.ORDER_COMPLETE_TXT = ".complete-header"
        self.BACK_TO_PRODUCTS_BTN = "#back-to-products"
        
    def get_cart_item_name(self):
        return self.page.locator(self.CART_ITEM_NAME)

    def proceed_to_checkout(self):
        self.page.click(self.CHECKOUT_BTN)

    def enter_checkout_details(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.page.click(self.CONTINUE_BTN)

    def get_total_price_txt(self):
        return self.page.locator(self.PRICE_TOTAL_TXT)
    
    def finish_checkout(self):
        self.page.click(self.FINISH_BTN)

    def get_order_complete_txt(self):
        return self.page.locator(self.ORDER_COMPLETE_TXT)
    
    def exit_order_back_to_products(self):
        self.page.click(self.BACK_TO_PRODUCTS_BTN)
    
    
