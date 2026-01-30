import pytest
from tools.playwrigh.pages import initialize_playwright_page
from config import settings
import allure
from playwright.sync_api import Page, Playwright, sync_playwright
from _pytest.fixtures import SubRequest
from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright):

    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit("./#/auth/registration")
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.registration_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )


