import pytest
from pages.login_page import LoginPage



@pytest.mark.authorization
@pytest.mark.regression
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
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.login_form.fill(email, password)
    login_page.click_login()
    login_page.check_alert_text("Wrong email or password")
