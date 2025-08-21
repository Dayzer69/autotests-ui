from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # карточка курса
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # меню карточки курса
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_button = page.get_by_test_id('course-view-delete-menu-item')

        # отображение пустого списка курсов
        self.empty_courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_courses_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_courses_description = page.get_by_test_id('courses-list-empty-view-description-text')


    def check_courses_title_is_visible(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_empty_view(self):
        expect(self.empty_courses_icon).to_be_visible()

        expect(self.empty_courses_title).to_be_visible()
        expect(self.empty_courses_title).to_have_text('There is no results')

        expect(self.empty_courses_description).to_be_visible()
        expect(self.empty_courses_description).to_have_text(
            'Results from the load test pipeline will be displayed here'
        )

    def check_create_course_button_is_visible(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_course_card(
            self,
            index: int, # айди карточки
            title: str, # заголовок карточки
            max_score: str,  # значение максимального балла
            min_score: str, # значение миниматьного балла
            estimated_time: str # значение примерного времени прхождения
    ):
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)

        expect(self.course_max_score_text.nth(index)).to_be_visible()
        expect(self.course_max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.course_min_score_text.nth(index)).to_be_visible()
        expect(self.course_min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.course_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')


    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()
        expect(self.course_edit_button).to_be_visible()
        self.course_edit_button.click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()
        expect(self.course_delete_button).to_be_visible()
        self.course_delete_button.click()



