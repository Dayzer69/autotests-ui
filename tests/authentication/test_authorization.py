import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.authorization
@pytest.mark.regression
class TestAuthorization:
    @pytest.mark.parametrize(
        'email, password',
        [("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")],
        ids= [
            'Проверяем, что пользователь не может войти в систему с невалидными email и password',
            'Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password',
            'Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password'
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill(email, password)
        login_page.click_login()
        login_page.check_alert_text("Wrong email or password")


    def test_successful_authorization(
            self,
            registration_page: RegistrationPage,
            login_page: LoginPage,
            dashboard_page: DashboardPage
    ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user2name@mail.ru', username='user2name', password='password')
        registration_page.registration_button.click()

        dashboard_page.dashboard.check_visible()
        dashboard_page.navbar.check_visible('user2name')
        dashboard_page.sidebar.check_visible()

        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='user2name@mail.ru', password='password')
        login_page.click_login()

        dashboard_page.dashboard.check_visible()
        dashboard_page.navbar.check_visible('user2name')
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email='', username='', password='')

