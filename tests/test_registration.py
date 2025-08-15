import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize(
    'email, user_name, password', [('user.name@gmail.com', 'username', 'password')]
)
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage,
                                 email: str, user_name: str, password: str):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email, user_name, password)
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title_is_visible()