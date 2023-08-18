from selenium.webdriver.remote import webdriver, webelement


class BasePage(object):
    """Base abstract class with common methods, designed to serve as the foundation for other pages within the page
    object implementation. Subclasses are expected to inherit from BasePage to take advantage of its methods and
    enhance their own specific implementations. """

    def __init__(self, driver: webdriver):
        self.driver = driver

    def click(self, selector: tuple) -> None:
        element = self.driver.find_element(*selector)
        element.click()

    def is_visible(self, selector: tuple) -> bool:
        element = self.driver.find_element(*selector)
        return element.is_displayed()

    def get_text(self, selector: tuple) -> str:
        element = self.driver.find_element(*selector)
        return element.text

    def get_amount(self, selector: tuple) -> int:
        elements = self.driver.find_elements(*selector)
        return len(elements)

    def fill_in(self, text, selector: tuple) -> None:
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    def get_element(self, selector: tuple) -> webelement:
        element = self.driver.find_element(*selector)
        return element

    def get_elements(self, selector: tuple) -> list[webelement]:
        elements = self.driver.find_elements(*selector)
        return elements
