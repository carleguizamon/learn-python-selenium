from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec


class TestLogin:
    TITLE = (By.ID, "welcomeMsg")

    def setup_class(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://practis.co.il/automation/")
        input_username = self.driver.find_element(By.NAME, "username")
        input_password = self.driver.find_element(By.NAME, "password")
        button_login = self.driver.find_element(By.NAME, "login")
        input_username.send_keys("admin")
        input_password.send_keys("admin")
        button_login.click()
        title = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.TITLE))
        assert title.text == "Welcome to the Main page!", "The title is no correct"
