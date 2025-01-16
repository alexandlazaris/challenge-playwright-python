from base import *

class LoginPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.USERNAME_INPUT = "#user-name"
        self.PASSWORD_INPUT = "#password"
        self.LOGIN_BTN = "#login-button"
        self.ERROR_TXT = ".error-message-container h3"

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BTN)

    def get_error_text(self):
        return self.page.locator(self.ERROR_TXT)
        