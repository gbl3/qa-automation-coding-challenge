from .BasePage import BasePage
from .locators.get_git_repos_locators import GetGitReposPageLocators


class GetGitReposPage(BasePage):
    def __init__(self, driver: object):
        super().__init__(driver)
        self.locators = GetGitReposPageLocators()
        self.pageURL = 'http://localhost:3000/'

    def visit(self) -> None:
        self.driver.get(self.pageURL)

    def get_page_title(self) -> str:
        return self.driver.title

    def get_header(self) -> object:
        return super().get_element(self.locators.page_header)

    def get_failure_message(self) -> object:
        return super().get_element(self.locators.failure_message)

    def get_success_message(self) -> object:
        return super().get_element(self.locators.success_message)

    def get_no_repos(self) -> object:
        return super().get_element(self.locators.no_repos_text)

    def get_header_visibility(self) -> bool:
        return super().is_visible(self.locators.page_header)

    def get_search_input_visibility(self) -> bool:
        return super().is_visible(self.locators.git_username_input)

    def get_no_repos_visibility(self) -> bool:
        return super().is_visible(self.locators.no_repos_text)

    def click_on_username_field(self) -> None:
        super().click(self.locators.git_username_input)

    def click_on_go_button(self) -> None:
        super().click(self.locators.go_button)

