from selenium.webdriver.common.by import By


class GetGitReposPageLocators:
    FORM_LOCATOR: str = 'form.input-area'
    MESSAGE_AREA_LOCATOR: str = 'section.message-area'
    OUTPUT_AREA_LOCATOR: str = '.output-area'

    @property
    def page_header(self) -> tuple:
        return (By.CSS_SELECTOR, 'header h1')

    @property
    def success_message(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.MESSAGE_AREA_LOCATOR} .message-success")

    @property
    def failure_message(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.MESSAGE_AREA_LOCATOR} .message-failure")

    @property
    def git_username_input(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.FORM_LOCATOR} #username")

    @property
    def go_button(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.FORM_LOCATOR} button.submit")

    @property
    def no_repos_text(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.OUTPUT_AREA_LOCATOR} .output-status-text")

    @property
    def repo_amount(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.OUTPUT_AREA_LOCATOR} .repo-amount")

    @property
    def repo_list_items(self) -> tuple:
        return (By.CSS_SELECTOR, f"{self.OUTPUT_AREA_LOCATOR} li.repo-row")

    @property
    def repo_description(self) -> tuple:
        return (By.CSS_SELECTOR, '.repo-description')

    def repo_link(self, repo_name: str) -> tuple:
        return (By.PARTIAL_LINK_TEXT, repo_name)

