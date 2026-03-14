from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Admin_Page_Class:
    click_admin_xpath = "//a[@class='oxd-main-menu-item active']"
    click_add_xpath = "//button[normalize-space()='Add']"
    user_role_xpath = "//div[@class='oxd-select-text oxd-select-text--focus']//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']"
    employee_name_xpath = "//input[@placeholder='Type for hints...']"
    status_xpath = "//div[3]//div[1]//div[2]//div[1]//div[1]//div[1]"
    user_name_xpath = "//input[@class='oxd-input oxd-input--focus']"
    password_css_selector = ".user-password-cell > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
    confirm_password_xpath = "div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
    save_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Click_Admin_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_admin_xpath)))
        self.driver.find_element(By.XPATH, self.click_admin_xpath).click()

    def Click_Add_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.click_add_xpath)))
        self.driver.find_element(By.XPATH, self.click_add_xpath).click()

    def Select_User_Role(self, role):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.user_role_xpath)))
        Select(self.driver.find_element(By.XPATH, self.user_role_xpath)).select_by_visible_text("Admin")

    def Enter_Employee_Name(self, employee_name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.employee_name_xpath)))
        self.driver.find_element(By.XPATH, self.employee_name_xpath).send_keys(employee_name)

    def Select_Status(self, status):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.status_xpath)))
        Select(self.driver.find_element(By.XPATH, self.status_xpath)).select_by_visible_text("Enabled")

    def Enter_User_Name(self, username1):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.user_name_xpath)))
        self.driver.find_element(By.XPATH, self.user_name_xpath).send_keys(username1)

    def Enter_Password(self, password1):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.password_css_selector)))
        self.driver.find_element(By.CSS_SELECTOR, self.password_css_selector).send_keys(password1)

    def Enter_Confirm_Password(self, confirm_password1):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.confirm_password_xpath)))
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_password1)

    def Click_Save_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.save_button_xpath)))
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

