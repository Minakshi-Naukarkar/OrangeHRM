import time
import allure
import pytest

from Utilities.logger import Logger
from Utilities.readConfig import ReadConfig
from pageObjects.Login_Page import Login_Page_Class


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_001:
    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    log = Logger.get_logger()

    @allure.title("Verify OrangeHRM Login Page URL")
    @allure.description("This test case verifies the URL of the OrangeHRM login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.step("Verify URL")
    @allure.epic("OrangeHRM Login")
    @allure.feature("Login Page")
    @allure.story("Verify Login Page URL")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/OrangeHRM/OrangeHRM/issues/1234", name="Issue #1234")
    @allure.testcase("https://github.com/OrangeHRM/OrangeHRM/issues/5678", name="Test Case #5678")
    @allure.tag("Regression")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @pytest.mark.order(1)

    def test_verify_url_001(self):
        self.log.info("Test Case: Verify OrangeHRM Login Page URL")
        self.driver.get(self.login_url)
        self.log.info("Navigated to OrangeHRM Login Page")
        if self.driver.title == "OrangeHRM":
            self.log.info("Test Passed")
            self.log.info("Screenshot saved: Screenshots\\test_verify_url_pass.png")
            self.driver.save_screenshot("Screenshots\\test_verify_url_pass.png")
            allure.attach.file("Screenshots\\test_verify_url_pass.png", name = "Pass", attachment_type = allure.attachment_type.PNG)
            assert True
        else:
            self.log.info("Test Failed")
            self.log.info("Screenshot saved: Screenshots\\test_verify_url_fail.png")
            self.driver.save_screenshot("Screenshots\\test_verify_url_fail.png")
            allure.attach.file("Screenshots\\test_verify_url_fail.png", name = "Fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Test Case Completed")
        self.log.info("============================================================")

    @allure.title("Verify OrangeHRM Login")
    @allure.description("This test case verifies the login functionality of OrangeHRM")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.step("Enter Username")
    @allure.step("Enter Password")
    @allure.step("Click Login Button")
    @allure.step("Verify Login")
    @allure.epic("OrangeHRM Login")
    @allure.feature("Login Functionality")
    @allure.story("Verify Login")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/OrangeHRM/OrangeHRM/issues/1234", name="Issue #1234")
    @allure.testcase("https://github.com/OrangeHRM/OrangeHRM/issues/5678", name="Test Case #5678")
    @allure.tag("Regression")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @pytest.mark.order(2)
    def test_OrangeHRM_Login_002(self):
        self.log.info("Test Case: Verify OrangeHRM Login")
        self.driver.get(self.login_url)
        self.log.info("Navigated to OrangeHRM Login Page")
        lp = Login_Page_Class(self.driver)
        self.log.info("Entering Username")
        lp.Enter_Username(self.username)
        self.log.info("Entering Password")
        lp.Enter_Password(self.password)
        self.log.info("Clicking Login Button")
        lp.Click_Login_Button()
        self.log.info("Verifying Login")
        if lp.verify_login() == "Login Successfull":
            self.log.info("Test Passed")
            self.log.info("Screenshot saved: Screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.driver.save_screenshot("Screenshots\\test_OrangeHRM_Login_002_pass.png")
            allure.attach.file("Screenshots\\test_OrangeHRM_Login_002_pass.png", name = "Pass", attachment_type = allure.attachment_type.PNG)
            self.log.info("Clicking Menu Button")
            lp.Click_Menu_Button()
            self.log.info("Clicking Logout Button")
            lp.Click_Logout_Button()
            assert True
        else:
            self.log.info("Test Failed")
            self.log.info("Screenshot saved: Screenshots\\test_OrangeHRM_Login_002_fail.png")
            self.driver.save_screenshot("Screenshots\\test_OrangeHRM_Login_002_fail.png")
            allure.attach.file("Screenshots\\test_OrangeHRM_Login_002_fail.png", name = "Fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Test Case Completed")
        self.log.info("============================================================")

# pytest -v -s -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome