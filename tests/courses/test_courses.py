from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import pytest


@pytest.mark.courses
@pytest.mark.regression
# @pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/')
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", max_score="0", min_score="0", description="", estimated_time="")
        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_form.fill(
            title='Test Course From Auto',
            estimated_time='5 hours',
            description='Vsem Zdarova',
            max_score='100',
            min_score='1'
        )
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title='Test Course From Auto',
            estimated_time='5 hours',
            max_score='100',
            min_score='1',
        )
        courses_list_page.course_menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title='Test Course From Auto (Edited)',
            estimated_time='5 hours (Edited)',
            description='Vsem Zdarova (Edited)',
            max_score='333',
            min_score='222'
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Test Course From Auto (Edited)',
            estimated_time='5 hours (Edited)',
            max_score='333',
            min_score='222'
        )


