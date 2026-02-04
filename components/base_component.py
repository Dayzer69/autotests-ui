from playwright.sync_api import Page, expect
from re import Pattern
from tools.logger import get_logger


logger = get_logger("BASE COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        logger.info(f'Check current url matches pattern "{expected_url.pattern}"')
        expect(self.page).to_have_url(expected_url)

    def refresh_page(self):
        self.page.reload()
        

