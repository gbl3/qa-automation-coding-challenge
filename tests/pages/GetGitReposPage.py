from selenium.common import NoSuchElementException

from .BasePage import BasePage
from .locators.get_git_repos_locators import GetGitReposPageLocators
from selenium.webdriver.remote import webdriver, webelement


class GetGitReposPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locators: GetGitReposPageLocators = GetGitReposPageLocators()
        self.pageURL: str = 'http://localhost:3000/'

    def visit(self) -> None:
        self.driver.get(self.pageURL)

    def get_page_title(self) -> str:
        return self.driver.title

    def get_header(self) -> webelement:
        return super().get_element(self.locators.page_header)

    def get_failure_message(self) -> webelement:
        super().wait_for_element(self.locators.failure_message)
        return super().get_element(self.locators.failure_message)

    def get_success_message(self) -> webelement:
        super().wait_for_element(self.locators.success_message)
        return super().get_element(self.locators.success_message)

    def get_no_repos(self) -> webelement:
        return super().get_element(self.locators.no_repos_text)

    def get_repo_amount(self) -> webelement:
        return super().get_element(self.locators.repo_amount)

    def get_all_repos(self) -> list[webelement]:
        return super().get_elements(self.locators.repo_list_items)

    def get_repo_by_name(self, repo_name: str) -> dict:
        all_repos: list[webelement] = self.get_all_repos()
        desired_repo: dict = {}
        repo_link: webelement
        repo_description: webelement

        for repo in all_repos:
            try:
                repo_link = repo.find_element(*self.locators.repo_link(repo_name))
                repo_description = repo.find_element(*self.locators.repo_description)

                desired_repo["link"] = repo_link
                desired_repo["description"] = repo_description
                break
            except NoSuchElementException:
                continue

        if desired_repo:
            return desired_repo
        else:
            raise Exception(f"Requested repository '{repo_name}' not found, use a valid name")

    def get_search_input_visibility(self) -> bool:
        return super().is_visible(self.locators.git_username_input)

    def click_on_repo_name(self, repo_name: str) -> None:
        desired_repo: dict = self.get_repo_by_name(repo_name)
        desired_repo["link"].click()

    def click_on_go_button(self) -> None:
        super().click(self.locators.go_button)

    def fill_username_field(self, username: str) -> None:
        super().fill_in(self.locators.git_username_input, username)

