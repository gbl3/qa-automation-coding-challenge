class BasePage(object):
    """Base abstract class with common methods, designed to serve as the foundation for other pages within the page
    object implementation. Subclasses are expected to inherit from BasePage to take advantage of its methods and
    enhance their own specific implementations. """

    def __init__(self, driver):
        self.driver = driver

    def click(self, selector):
        element = self.driver.find_element(*selector)
        element.click()

    def is_visible(self, selector):
        element = self.driver.find_element(*selector)
        return element.is_displayed()

    def get_text(self, selector):
        element = self.driver.find_element(*selector)
        return element.text

    def get_amount(self, selector):
        elements = self.driver.find_elements(*selector)
        return len(elements)

    def fill_in(self, text, selector):
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    def get_element(self, selector):
        element = self.driver.find_element(*selector)
        return element

    def get_elements(self, selector):
        elements = self.driver.find_elements(*selector)
        return elements
