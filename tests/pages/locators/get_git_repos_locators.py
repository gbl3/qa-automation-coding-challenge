from selenium.webdriver.common.by import By


class GetGitReposPageLocators:
    FORM_LOCATOR = 'form.input-area'
    REPO_LIST_LOCATOR = 'repo-list-container'
    MESSAGE_AREA_LOCATOR = 'section.message-area'

    @property
    def success_message(self):
        return (By.CSS_SELECTOR, f"{self.MESSAGE_AREA_LOCATOR} .message-success")

    @property
    def failure_message(self):
        return (By.CSS_SELECTOR, f"{self.MESSAGE_AREA_LOCATOR} .message-failure")

    @property
    def git_username_input(self):
        return (By.CSS_SELECTOR, f"{self.FORM_LOCATOR} .field-username")

    @property
    def go_button(self):
        return (By.CSS_SELECTOR, f"{self.FORM_LOCATOR} button.submit")

    @property
    def repo_amount(self):
        return (By.CSS_SELECTOR, f"{self.REPO_LIST_LOCATOR} .repo-amount")

    @property
    def repo_list_items(self):
        return (By.CSS_SELECTOR, f"{self.REPO_LIST_LOCATOR} li.repo-row")

    def get_repo_item_locators(self, item_number):
        repo_name_locator = (By.CSS_SELECTOR, f"{self.REPO_LIST_LOCATOR} li.repo-row:nth-child({item_number}) a")
        repo_description_locator = (
            By.CSS_SELECTOR,
            f"{self.REPO_LIST_LOCATOR} li.repo-row:nth-child({item_number}) .repo-description"
        )

        return {
            "repo_name": repo_name_locator,
            "repo_description": repo_description_locator
        }
