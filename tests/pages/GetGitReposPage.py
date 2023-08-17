from .BasePage import BasePage
from .locators.get_git_repos_locators import GetGitReposPageLocators


class GetGitReposPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = GetGitReposPageLocators()
        self.pageURL = 'http://localhost:3000/'

    def visit(self):
        self.driver.get(self.pageURL)

    def click_on_username_field(self):
        super().click(self.locators.git_username_input)

    def click_on_go_button(self):
        super().click(self.locators.go_button)

    def get_failure_message(self):
        super().get_element(self.locators.failure_message)

    def get_success_message(self):
        super().get_element(self.locators.success_message)
