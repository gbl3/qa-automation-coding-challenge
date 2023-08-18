import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.GetGitReposPage import GetGitReposPage


class GetGitReposPageTests(unittest.TestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        # If you want to run it headless, just uncomment the line below:
        # options.add_argument("--headless=new")

        # Using webdriver_manager library to programmatically download and get chrome driver path
        self.driver: webdriver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        self.page: GetGitReposPage = GetGitReposPage(self.driver)
        self.page.visit()

    def test_verify_initial_state(self) -> None:
        """
        Test case being addressed:

        1. Page should have:
            1.1 A header
            1.2 A search form
            1.3 A search result section
        2.The content of the header should be equal to the page title
        3. On the results section, there should be a text "No repos" being displayed

        :return: None
        """

        # Set up test data
        expected_no_repos_text: str = "No repos"
        actual_page_title_text: str = self.page.get_page_title()
        actual_page_header_text: str = self.page.get_header().text
        actual_no_repos_text: str = self.page.get_no_repos().text

        # Checking initial state of UI elements
        self.assertTrue(self.page.get_header().is_displayed(), "Page header should be visible")
        self.assertEqual(
            actual_page_title_text,
            actual_page_header_text,
            "The content of the header should be equal to the page title"
        )
        self.assertTrue(self.page.get_search_input_visibility(), 'Search form should be visible')
        self.assertTrue(self.page.get_no_repos().is_displayed(), 'Search result should be visible')
        self.assertEqual(
            actual_no_repos_text,
            expected_no_repos_text,
            f"Expected results section to display '{expected_no_repos_text}', got '{actual_no_repos_text}' instead"
        )

    def test_search_valid_user_with_public_repositories(self) -> None:
        """
        Test case being addressed:

        1. After clicking on 'Go' button:
            1.1 Search should trigger
            1.2 Success message "Success!" should be displayed
            1.3 Amount of user repositories displayed
            1.4 All public repositories of the user should be listed
            1.5 Proper info(name and description) about the repositories should be displayed.
            1.6 Repositories without a description should have "-" displayed on the description column
        2. After clicking on a repository name, corresponding repo should open in a new tab

        :return: None
        """

        # Set up test data
        username: str = "gbl3"
        expected_success_message: str = "Success!"
        expected_repo_amount: str = "13"
        expected_complete_repo_title: str = "qa-automation-coding-challenge"
        expected_complete_repo_description: str = "tn-lp-qa"
        expected_incomplete_repo_title: str = "my-first-blog"
        expected_incomplete_repo_description: str = "–"
        expected_page_url: str = "github.com"
        initial_page_identifier: str = self.driver.current_window_handle

        # Fills username and then clicks on 'Go' button to trigger search
        self.page.fill_username_field(username)
        self.page.click_on_go_button()

        # Checking success message visibility and content after search is triggered
        actual_success_message: str = self.page.get_success_message().text
        self.assertTrue(
            self.page.get_success_message().is_displayed(),
            "Success message should be displayed after search is triggered"
        )
        self.assertEqual(
            actual_success_message,
            expected_success_message,
            f"Expected message: '{expected_success_message}', Actual: '{actual_success_message}'"
        )

        # Checking amount of user repositories being displayed through both text and actual list of elements
        actual_repo_amount_found_text: str = self.page.get_repo_amount().text
        actual_repo_amount_from_repo_list: int = len(self.page.get_all_repos())
        self.assertIn(
            expected_repo_amount,
            actual_repo_amount_found_text,
            f"Expected amount of repos to be '{expected_repo_amount}', got '{actual_repo_amount_found_text}' instead"
        )
        self.assertEqual(
            int(expected_repo_amount),
            actual_repo_amount_from_repo_list,
            f"Expected amount of listed repos: '{expected_repo_amount}', Actual: '{actual_repo_amount_from_repo_list}'"
        )

        # Checking title and description for a repository that has both
        actual_complete_repo = self.page.get_repo_by_name(expected_complete_repo_title)
        actual_complete_repo_title = actual_complete_repo['link'].text
        actual_complete_repo_description = actual_complete_repo['description'].text
        self.assertEqual(
            actual_complete_repo_title,
            expected_complete_repo_title,
            f"Expected repo title: '{expected_complete_repo_title}', Actual: '{actual_complete_repo_title}'"
        )
        self.assertEqual(
            actual_complete_repo_description,
            expected_complete_repo_description,
            f"Expected description: '{expected_complete_repo_description}', Actual:'{actual_complete_repo_description}'"
        )

        # Checking title and description for a repository that does not have a description
        actual_incomplete_repo = self.page.get_repo_by_name(expected_incomplete_repo_title)
        actual_incomplete_repo_title = actual_incomplete_repo['link'].text
        actual_incomplete_repo_description = actual_incomplete_repo['description'].text
        self.assertEqual(
            actual_incomplete_repo_title,
            expected_incomplete_repo_title,
            f"Expected repo title: '{expected_incomplete_repo_title}', Actual: '{actual_incomplete_repo_title}'"
        )
        self.assertEqual(
            actual_incomplete_repo_description,
            expected_incomplete_repo_description,
            f"Expected: '{expected_incomplete_repo_description}', Actual: '{actual_incomplete_repo_description}'"
        )

        # Clicking on desired repository through its name
        self.page.click_on_repo_name(expected_complete_repo_title)

        # Switch driver focus from initial page to git repository page, in order to compare title
        for window in self.driver.window_handles:
            if window != initial_page_identifier:
                self.driver.switch_to.window(window)

        # Confirming that user is on git page after click
        current_page_title = self.page.get_page_title()
        current_page_url = self.driver.current_url
        self.assertIn(
            expected_complete_repo_title,
            current_page_title,
            f"Expected page title to have {expected_complete_repo_title}, got {current_page_title} instead"
        )
        self.assertIn(
            expected_page_url,
            current_page_url,
            f"Expected current page to have '{expected_page_url}', got '{current_page_url}' instead"
        )

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
