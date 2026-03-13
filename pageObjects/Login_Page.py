import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:
    text_username_xpath = "//input[@placeholder='Username']"
    text_password_xpath = "//input[@placeholder='Password']"
    login_button_xpath = "//button[@type='submit']"
    menu_button_xpath = "//p[@class='oxd-userdropdown-name']"
    logout_button_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_username_xpath)))
        self.driver.find_element(By. XPATH, self.text_username_xpath).send_keys(username)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_password_xpath)))
        self.driver.find_element(By. XPATH, self.text_password_xpath).send_keys(password)

    def Click_Login_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.login_button_xpath)))
        self.driver.find_element(By. XPATH, self.login_button_xpath).click()

    def Click_Menu_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.menu_button_xpath)))
        self.driver.find_element(By. XPATH, self.menu_button_xpath).click()

    def Click_Logout_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.logout_button_xpath)))
        self.driver.find_element(By. XPATH, self.logout_button_xpath).click()

    def verify_login(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.menu_button_xpath)))
            self.driver.find_element(By.XPATH, self.menu_button_xpath)
            return "Login Successfull"
        except:
            return "Login Failed"

