from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin:

    def setup_class(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown_class(self):
        self.driver.quit()

    def test_abc(self):
        self.driver.get("https://www.google.com.ar")