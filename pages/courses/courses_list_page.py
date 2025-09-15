from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent




class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.empty_view = EmptyViewComponent(page, 'courses-list')


        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.course_menu = CourseViewMenuComponent(page)

        # заголовок и кнопка создания курса
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # карточка курса
        self.course_view = CourseViewComponent(page)

        # меню карточки курса
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_button = page.get_by_test_id('course-view-delete-menu-item')

        # отображение пустого списка курсов
        self.empty_courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_courses_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_courses_description = page.get_by_test_id('courses-list-empty-view-description-text')


    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )





