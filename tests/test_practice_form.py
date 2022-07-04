import os

from src.models.automation_practice_form import PracticeFormPageModel
import pytest

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


class TestPracticeFormPage:
    """
    Тест сьют. Тестирование странцы demoqa
    """

    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_images")

    @pytest.mark.parametrize("image_file", os.listdir(image_dir))
    def test_form_registration_student(self, open_browser, image_file):
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
        open_browser.practice_form_page.input_information_student(field)
        open_browser.practice_form_page.fill_date_form(field)
        open_browser.practice_form_page.input_state_city(field)
        open_browser.practice_form_page.input_hobbies(field)
        open_browser.practice_form_page.input_gender(field)
        open_browser.practice_form_page.choose_image_file(abs_path)
        open_browser.practice_form_page.click_submit()
        open_browser.practice_form_page.check_have_text_on_submiting_form(field)
        open_browser.practice_form_page.click_on_button_close()


