from selenium import webdriver
import time
import unittest
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.HomePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Jyoti/Documents/PythonTestProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Entering username password on login page
    def test_login_valid(self):
        driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(2)

    def test_login_invalid_username(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid credentials123")


        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Jyoti/Documents/PythonTestProject/reports'))



