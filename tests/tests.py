import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.GetGitReposPage import GetGitReposPage


class GetGitReposPageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver: webdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.page: GetGitReposPage = GetGitReposPage(self.driver)
        self.page.visit()

    def test_verify_initial_state(self):
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

        expected_no_repos_text: str = "No repos"
        actual_page_title_text: str = self.page.get_page_title()
        actual_page_header_text: str = self.page.get_header().text
        actual_no_repos_text: str = self.page.get_no_repos().text

        self.assertTrue(
            self.page.get_header_visibility(),
            "Page header should be visible"
        )
        self.assertEqual(
            actual_page_title_text,
            actual_page_header_text,
            "The content of the header should be equal to the page title"
        )
        self.assertTrue(
            self.page.get_search_input_visibility(),
            'Search form should be visible'
        )
        self.assertTrue(
            self.page.get_no_repos_visibility(),
            'Search result should be visible'
        )
        self.assertEqual(
            actual_no_repos_text,
            expected_no_repos_text,
            f"Expected results section to display '{expected_no_repos_text}', it is displaying '{actual_no_repos_text}'"
        )

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
