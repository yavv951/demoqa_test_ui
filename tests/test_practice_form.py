import os

import pytest
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

    @pytest.mark.parametrize("image_file", os.listdir(image_dir))
    def test_form_registration_student(self, app, image_file):
        """
        Тест кейс 0001
        1. открыть страницу https://demoqa.com/automation-practice-form
        2. Заполнить форму регистрации студента:
           Name
           Email
           Gender
           Mobile
           Date of Birth
           Subjects
           Hobbies
           Picture
           Current Address
           State and City
        3. Проверить,что заполненные поля отобразились в форме регистрациию
        4. Закрыть модальное окно
        """
        abs_path = os.path.join(self.image_dir, image_file)
        field = PracticeFormPageModel.random()
        app.practice_form_page\
            .input_information_student(field)\
            .fill_date_form(field)\
            .input_state_city(field)\
            .input_hobbies(field)\
            .input_gender(field)\
            .choose_image_file(abs_path)\
            .click_submit()\
            .check_have_text_on_submiting_form(field)\
            .click_on_button_close()

        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
