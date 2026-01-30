import pytest
import allure
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from tools.routes import AppRoute
from config import settings



@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
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
    # @allure.severity(Severity.CRITICAL)
    # @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email, password)
        login_page.click_login()
        login_page.check_alert_text("Wrong email or password")

    @allure.severity(Severity.BLOCKER)
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    def test_successful_authorization(
            self,
            registration_page: RegistrationPage,
            login_page: LoginPage,
            dashboard_page: DashboardPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.registration_button.click()

        dashboard_page.dashboard.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        login_page.click_login()

        dashboard_page.dashboard.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @allure.severity(Severity.NORMAL)
    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email='', username='', password='')

