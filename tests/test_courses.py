from playwright.sync_api import sync_playwright, expect, Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
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

@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form('','','','0','0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        'Playwright',
        '2 weeks',
        'Playwright',
        '100',
        '10'
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_courses_title_is_visible()
    courses_list_page.check_create_course_button_is_visible()
    courses_list_page.check_visible_course_card(
        0,
        'Playwright',
        '100',
        '10',
        '2 weeks'
    )

