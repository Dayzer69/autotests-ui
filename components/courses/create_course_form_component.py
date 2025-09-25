import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
from elements.textarea import Textarea
import allure


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title input')
        self.estimated_time_input = Input(
            page,'create-course-form-estimated-time-input', 'Estimated Time Input'
        )
        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'Description')
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score input')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score input')

    @allure.step('Filling course form')
    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)


    @allure.step('Check that course form has correct values')
    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        with allure.step(f'Check that field "title" is visible and filled with value {title}'):
            self.title_input.check_visible()
            self.title_input.check_have_value(title)

        with allure.step(f'Check that field "estimated time" is visible and filled with value {estimated_time}'):
            self.estimated_time_input.check_visible()
            self.estimated_time_input.check_have_value(estimated_time)

        with allure.step(f'Check that field "description" is visible and filled with value {description}'):
            self.description_textarea.check_visible()
            self.description_textarea.check_have_text(description)

        with allure.step(f'Check that field "max score" is visible and filled with value {max_score}'):
            self.max_score_input.check_visible()
            self.max_score_input.check_have_value(max_score)

        with allure.step(f'Check that field "min score" is filled with value {min_score}'):
            self.min_score_input.check_visible()
            self.min_score_input.check_have_value(min_score)
