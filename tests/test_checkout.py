from playwright.sync_api import Page, expect
from constants import *
from .page_objects.login_page import LoginPage
from .page_objects.inventory_page import InventoryPage
from .page_objects.checkout_page import CheckoutPage

def test_product_is_added_to_cart(page: Page):
    # arrange
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    PRODUCT_BACKPACK_NAME = "Sauce Labs Backpack"
    page.goto(URL_BASE)
    login_page.login(USERNAME_STANDARD, PASSWORD)

    # act
    product_sauce_backpack = "[data-test=add-to-cart-sauce-labs-backpack]"
    inventory_page.add_product_to_cart(product_sauce_backpack)
    
    # assert
    expect(inventory_page.get_shopping_cart_badge_text()).to_have_text("1")
    inventory_page.go_to_shopping_cart()
    expect(checkout_page.get_cart_item_name()).to_contain_text(PRODUCT_BACKPACK_NAME)

def test_complete_checkout_for_an_item(page: Page):
    # arrange
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    page.goto(URL_BASE)
    login_page.login(USERNAME_STANDARD, PASSWORD)

    # act
    product_sauce_backpack = "[data-test=add-to-cart-sauce-labs-backpack]"
    inventory_page.add_product_to_cart(product_sauce_backpack)
    inventory_page.go_to_shopping_cart()

    # assert
    checkout_page.proceed_to_checkout()
    checkout_page.enter_checkout_details("first", "second", "third")
    # TODO: improve this assertion
    expect(checkout_page.get_total_price_txt()).to_be_visible()
    checkout_page.finish_checkout()
    
    # assert
    expect(checkout_page.get_order_complete_txt()).to_have_text("Thank you for your order!")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    checkout_page.exit_order_back_to_products()


    