from .base import *

class InventoryPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.SHOPPING_CART_LINK = ".shopping_cart_link"
        self.SHOPPING_CART_BADGE = "[data-test=shopping-cart-badge]"
        
    def select_shopping_cart(self):
        self.page.click(self.SHOPPING_CART_LINK)

    def get_shopping_cart_link(self):
        return self.page.locator(self.SHOPPING_CART_LINK)
    
    def get_shopping_cart_badge_text(self):
        return self.page.locator(self.SHOPPING_CART_BADGE)
    
    def go_to_shopping_cart(self):
        return self.page.locator(self.SHOPPING_CART_LINK).click()
    
    def add_product_to_cart(self, product_link: str):
        product = self.page.locator(product_link)
        product.click()