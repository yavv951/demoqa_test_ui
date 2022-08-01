import os

import allure
import pytest
from allure_commons.types import Severity
from selene.support.shared import browser

from src.models.automation_practice_form import PracticeFormPageModel
from utils import attach

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


class TestPracticeFormPage:
    """
    Тест сьют. Тестирование странцы demoqa
    """

    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_images")

    @allure.tag('WEB UI')
    @allure.severity(Severity.CRITICAL)
    @allure.label('Owner', 'Vadim')
    @allure.feature('Testing site qa guru with selene')
    @allure.story(f'Тест кейс 0001 Регистрация студента')
    @allure.link('https://github.com/yavv951', name='Owner')
    @allure.step("Открываем страницу https://demoqa.com/automation-practice-form")
    @pytest.mark.parametrize("image_file", os.listdir(image_dir))
    def test_form_registration_student(self, app, image_file):
        abs_path = os.path.join(self.image_dir, image_file)
        field = PracticeFormPageModel.random()
        app.practice_form_page \
            .input_information_student(field) \
            .fill_date_form(field) \
            .input_state_city(field) \
            .input_hobbies(field) \
            .input_gender(field) \
            .choose_image_file(abs_path) \
            .click_submit() \
            .check_have_text_on_submiting_form(field) \
            .click_on_button_close()
        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
