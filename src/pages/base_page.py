from selene import *
from selene.core.entity import SeleneElement
from selene.core.wait import Command
from selene.support.shared import browser
from selene.support.conditions import have, be


class BasePage:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def open_page(url):
        browser.open_url(url).driver.maximize_window()

    @staticmethod
    def fill_element(locator, text):
        browser.element(locator).clear().type(text)

    @staticmethod
    def fill_element_and_press_enter(locator, text):
        browser.element(locator).type(text).press_enter()

    @staticmethod
    def click_radio_button(locator, text):
        browser.all(locator).element_by(have.exact_text(text)).click()

    @staticmethod
    def load_file(locator, text):
        browser.element(locator).send_keys(text)

    @staticmethod
    def click_element(locator):
        browser.element(locator).should(be.clickable).click()

    @staticmethod
    def click_first_element(locator):
        browser.elements(locator).first().click()

    @staticmethod
    def check_element_have_text(locator, text):
        browser.element(locator).should(have.text(text))

    @staticmethod
    def cells_of_row(index, locator, locator_2, locator_3, text, text_2):
        """ метод по работе с табличными данными, применим когда необходимо по строкам определить введенный текст"""
        browser.element(locator).all(locator_2)[index].all(locator_3).should(have.exact_texts(text, text_2))

    @staticmethod
    def check_element_have_text_by(index, locator, text):
        browser.all(locator)[index].should(have.text(text))

    @staticmethod
    def check_element_have_text_(locator, text):
        browser.all(locator).should(have.text(text))

    @staticmethod
    def condition_is_not_text(locator, text):
        browser.element(locator).should_not_have(have.text(text))

    @staticmethod
    def check_element_have_attr(locator, attr_name, value):
        browser.element(locator).should(have.attribute(attr_name, value))

    @staticmethod
    def get_element_text(locator):
        return browser.element(locator).text

    @staticmethod
    def element_have_value(locator, text):
        browser.element(locator).should(have.attribute("value", text))

    @staticmethod
    def get_element_attr(locator):
        return browser.element(locator).get_attribute()

    @staticmethod
    def type_blank(locator):
        browser.element(locator).clear().type(' ').press_enter()

    @staticmethod
    def find_all_elements_and_click(locator, value):
        return browser.all(locator).element(have.text(value)).click()

    @staticmethod
    def size_line(locator):
        return browser.all(locator)

    @staticmethod
    def find_element(locator):
        return browser.find(locator)

    @staticmethod
    def find_element_(locator, locator_2):
        return browser.all('option').element(locator).element(locator_2).click()

    @staticmethod
    def close():
        return browser.close()

    @staticmethod
    def scroll_metod(x=0, y=0):
        """ Метод скрола на странице, в х и у указыватюся координаты страницы"""
        # browser.perform(Scroll.scroll_by_offset(x, y))
        browser.execute_script(f'window.scrollTo{x, y}')

    @staticmethod
    def switch_to_window(index: int):
        """ Метод переключения между окнами страницы,в скобках указывается индекс страницы,отсчет идет с 0"""
        browser.switch_to_tab(index)

    @staticmethod
    def hover_element(locator):
        """ Метод наведения курсора на поле"""
        browser.element(locator).hover()

    @staticmethod
    def select(locator, locator_2, option):
        """Функция для работы с select элементами"""
        browser.element(locator).perform(command.js.scroll_into_view).click()
        browser.all(locator_2).element_by(have.exact_text(option)).click()

class SelectList(object):
    """ Создан отдельных класс для работы с select элементами"""
    def __init__(self, element):
        self._element = element

    def open(self):
        self._element.click()

    def _options(self):
        return self._element.all('option')

    def select_by_value(self, value):
        self._options().element_by(have.value(value)).click()

    def select_by_text(self, text):
        self._options().element_by(have.text(text)).click()

    def select_by_exact_text(self, text):
        self._options().element_by(have.exact_text(text)).click()

    def set(self, value):
        self.open()
        self.select_by_value(value)


class Scroll(object):
    """ Создал отдельный класс для функции скролла на странице"""

    def scroll_by_offset(x: int, y: int) -> Command:
        return Command(
            f'scroll page by x {x} y {y}',
            lambda browser: browser.driver.execute_script(
                f'window.scrollBy({x}, {y});'
            )
        )
