from elements.text import Text
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
import re

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.login_form = LoginFormComponent(page)
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page,'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(
            page, 'login-page-wrong-email-or-password-alert', 'Wrong email or password'
        )


    def click_login(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    def check_alert_text(self, text):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text(text)


