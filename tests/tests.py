import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.GetGitReposPage import GetGitReposPage


class GetGitReposPageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.page = GetGitReposPage(self.driver)
        self.page.visit()

    def test_visit_page(self):
        print("start")
        self.page.click_on_go_button()
        time.sleep(5)
        print("end")
        assert True
        self.assertEqual(True, True)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
