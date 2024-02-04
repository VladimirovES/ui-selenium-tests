from abc import abstractmethod, ABC

import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.assertions import assert_data_is_equal, assert_lists_equal


class Component(ABC):
    def __init__(self, driver: webdriver, locator: tuple, name: str) -> None:
        self.driver = driver
        self.locator = locator
        self.name = name

    @abstractmethod
    def _type_of(self) -> str:
        return 'component'

    def _wait_for_element(self, locator, timeout=12) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Не могу найти элемент по локатору {locator}"
        )

    def _wait_for_elements(self, locator, timeout=12) -> list[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def _wait_for_desapear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def _wait_loaders_and_skeletons(self):
        """
        Дождаться загрузки страницы пока не исчезнет лоадер(загрузчик)
        """
        self._wait_for_desapear(('xpath', "//*[contains(@class, 'loader-framework')]"), timeout=20)
        self._wait_for_desapear(('xpath', "//div[contains(@class, 'skeleton')]"), timeout=20)

    def _format_locator(self, **kwargs):
        locator_by, locator_value = self.locator
        formatted_locator_value = locator_value.format(**kwargs)
        return locator_by, formatted_locator_value

    def _format_name(self, **kwargs):
        return self.name.format(**kwargs)

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def _find_element(self, should_display=True, scroll_to_elem=True, **kwargs):
        self._wait_loaders_and_skeletons()

        locator = self._format_locator(**kwargs)

        try:
            if should_display:
                element = self._wait_for_element((locator[0], locator[1]))
                if scroll_to_elem:
                    self._scroll_to_element(element)
                return element
            else:
                return self._wait_for_desapear((locator[0], locator[1])) or None
        except TimeoutException:
            if should_display:
                raise AssertionError(
                    f"'{self.name}' не отображается, хотя ожидается, что должен быть видимым, \n locator: {locator[1]}")
            else:
                return None

    def click(self, **kwargs):
        with allure.step(f'Нажать {self._type_of}: "{self._format_name(**kwargs)}".'):
            self._find_element(**kwargs).click()

    def check_visibility(self, is_visible=True, **kwargs) -> None:
        vision_text = 'Отображается' if is_visible else 'Не отображается'
        with allure.step(f'Assert: "{self._type_of} - "{self._format_name(**kwargs)}" {vision_text} на странице.'):
            if is_visible:
                element = self._wait_for_element(self._format_locator(**kwargs))
                assert element and element.is_displayed(), f"{self._type_of} '{self._format_name(**kwargs)}' should be visible"
            else:
                is_invisible = self._wait_for_desapear(self._format_locator(**kwargs))
                assert is_invisible, f"{self._type_of} - '{self._format_name(**kwargs)}' should not be visible"

    def get_text(self, **kwargs):
        return self._find_element(**kwargs).text

    def assert_text_eql(self, expected: str, **kwargs):
        actual = self._find_element(**kwargs).text
        assert_data_is_equal(actual=actual, expected=expected,
                             name=f"Текст {self._type_of} - '{self._format_name(**kwargs)}' равен: {expected}.")

    def hover(self, **kwargs) -> None:
        with allure.step(f'Навести "{self._type_of}": - "{self._format_name(**kwargs)}"'):
            element = self._find_element(**kwargs)
            ActionChains(self.driver, duration=600).move_to_element(element).perform()


class Iframe(Component):

    @property
    def _type_of(self):
        return 'Iframe'

    def switch_to_iframe(self, **kwargs):
        iframe = self._find_element(**kwargs)
        self.driver.switch_to.frame(iframe)





class ListElements(Component):
    @property
    def _type_of(self) -> str:
        return 'list of elements'

    def _find_elements(self, **kwargs) -> list[WebElement]:
        locator = self._format_locator(**kwargs)
        self._wait_loaders_and_skeletons()
        elements = self._wait_for_elements(locator)
        if not elements:
            raise AssertionError(f"Элементы по локатору {locator} не найдены.")
        return elements

    def get_text_of_elements(self, exclude_text=None, **kwargs):
        elements = self._find_elements(**kwargs)
        if exclude_text:
            return [element.text for element in elements if exclude_text not in element.text]
        else:
            return [element.text for element in elements]

    def assert_text_of_elements_in_list(self, expected: list, exclude_text=None, reverse=False, **kwargs):
        actual = sorted(self.get_text_of_elements(exclude_text, **kwargs), reverse=reverse)
        assert_lists_equal(actual=actual, expected=expected,
                           name=f'Текст "{self._type_of}" - "{self._format_name(**kwargs)}" равен: {expected}.')

    def count_elements(self, **kwargs):
        return len(self._find_elements(**kwargs))

    def count_elements_eql(self, count, **kwargs):
        actual_count = self.count_elements(**kwargs)
        assert_data_is_equal(actual=actual_count, expected=count,
                             name=f'Кол-во "{self._type_of}": "{self._format_name(**kwargs)}" равно: {count}.')


class Title(Component):
    @property
    def _type_of(self) -> str:
        return 'Title'


class Button(Component):
    @property
    def _type_of(self):
        return 'Button'

    def double_click(self, **kwargs):
        with allure.step(f'Двойной клик на "{self._type_of}" - "{self._format_name(**kwargs)}"'):
            element = self._find_element(**kwargs)
            ActionChains(self.driver, duration=600).double_click(element).perform()

    def js_click(self, **kwargs) -> None:
        with allure.step(f'JavaScript-клик на "{self._type_of}" "{self._format_name(**kwargs)}"'):
            element = self._find_element(**kwargs)
            self.driver.execute_script("arguments[0].click();", element)


class InputValidationError(Component):
    @property
    def _type_of(self):
        return 'ValidationError'


class Input(Component):
    @property
    def _type_of(self):
        return 'input'

    def fill(self, text, clear_before=False, **kwargs):
        with allure.step(f'Заполнить "{self._type_of}" - "{self._format_name(**kwargs)}" текстом: "{text}"'):
            element = self._find_element(**kwargs)
            if clear_before:
                self.clear(**kwargs)
            element.send_keys(text)

    def add_file(self, file, **kwargs):
        with allure.step(f'Добавить в "{self._type_of}" - "{self._format_name(**kwargs)}" file'):
            element = self._find_element(**kwargs)
            element.send_keys(file)

    def clear(self, **kwargs):
        with allure.step(f'Очистить "{self._type_of}" -"{self._format_name(**kwargs)}"'):
            element = self._find_element(**kwargs)
            element.clear()
            element.send_keys(Keys.BACKSPACE * len(element.get_attribute("value")))
