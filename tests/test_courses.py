from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    toolbar_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(toolbar_title).to_be_visible()
    expect(toolbar_title).to_have_text('Courses')

    result_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(result_icon).to_be_visible()

    result_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_title).to_be_visible()
    expect(result_title).to_have_text('There is no results')

    result_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(result_description).to_be_visible()
    expect(result_description).to_have_text('Results from the load test pipeline will be displayed here')

