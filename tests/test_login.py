import re
from playwright.sync_api import Page, expect
from constants import *
from login_page import LoginPage
from inventory_page import InventoryPage

def test_login_as_standard_user(page: Page):
    # arrange
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    page.goto(URL_BASE)

    # act
    login_page.login(USERNAME_STANDARD, PASSWORD)

    # assert
    expect(page).to_have_url(URL_INVENTORY)
    expect(inventory_page.get_shopping_cart_link()).to_be_visible()
    

def test_login_as_locked_user(page: Page):
    # arrange
    login_page = LoginPage(page)
    ERROR_MSG = "Epic sadface: Sorry, this user has been locked out."
    page.goto(URL_BASE)

    # act
    login_page.login(USERNAME_LOCKED, PASSWORD)

    # assert
    expect(login_page.get_error_text()).to_have_text(ERROR_MSG)