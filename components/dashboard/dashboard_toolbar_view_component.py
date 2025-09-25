from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
import allure


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check that label "Dashboard" is visible')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Dashboard')

