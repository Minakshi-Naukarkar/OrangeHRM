import time
import allure
import pytest

from Utilities.XLUtils import XLUtils_class
from Utilities.logger import Logger
from Utilities.readConfig import ReadConfig
from pageObjects.Login_Page import Login_Page_Class


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_DDT_002:
    driver = None
    login_url = ReadConfig.get_login_url()
    log = Logger.get_logger()
    excel_file = ".\\Test_Data\\OrangeHRM_Login_Data.xlsx"
    sheet = "Sheet1"

    def test_OrangeHRM_Login_DDT_003(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Functionality")
        rows_count = XLUtils_class.get_row_count(self.excel_file, self.sheet)
        self.log.info(f"Total Rows: {rows_count}")
        result = []
        for i in range(2, rows_count + 1):
            username = XLUtils_class.read_data(self.excel_file, self.sheet, i, 2)
            password = XLUtils_class.read_data(self.excel_file, self.sheet, i, 3)
            expected_result = XLUtils_class.read_data(self.excel_file, self.sheet, i, 4)
            self.log.info(f"Test Data: Username = {username}, Password = {password}, Expected Result = {expected_result}")
            self.log.info("Test Case: Verify OrangeHRM Login")
            self.driver.get(self.login_url)
            self.log.info("OrangeHRM Login page Loaded")
            lp = Login_Page_Class(self.driver)
            self.log.info(f"Entering Username={username}")
            lp.Enter_Username(username)
            self.log.info(f"Entering Password={password}")
            lp.Enter_Password(password)
            self.log.info("Clicking Login Button")
            lp.Click_Login_Button()
            if lp.verify_login() == "Login Successfull":
                self.log.info(f"Login Successful for Username = {username}")
                self.log.info("Screenshot saved: Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png")
                self.driver.save_screenshot(f"Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png")
                allure.attach.file(f"Screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png",name=f"test_OrangeHRM_Login_DDT_003_pass_{username}",attachment_type=allure.attachment_type.PNG)
                self.log.info("Clicking Menu Button")
                lp.Click_Menu_Button()
                self.log.info("Clicking Logout Button")
                lp.Click_Logout_Button()
                actual_result = "Login Successfull"
            else:
                self.log.error(f"Login Failed for Username = {username}")
                self.log.info("Screenshot saved: Screenshots\\test_OrangeHRM_Login_DDT_003_fail_{username}.png")
                self.driver.save_screenshot(f"Screenshots\\test_OrangeHRM_Login_DDT_003_fail_{ username}.png")
                allure.attach.file(f"Screenshots\\test_OrangeHRM_Login_DDT_003_fail_{username}.png",name=f"test_OrangeHRM_Login_DDT_003_fail_{username}",attachment_type=allure.attachment_type.PNG)
                actual_result = "Login Failed"

            if actual_result == expected_result:
                self.log.info(f"Test Passed for Username = {username}")
                test_case_status = "Pass"
                self.log.info("Test Case Passed")
                result.append("Pass")
            else:
                self.log.error(f"Test Failed for Username = {username}")
                test_case_status = "Fail"
                self.log.info("Test Case Failed")
                result.append("Fail")

            XLUtils_class.write_data(self.excel_file, self.sheet, i, 5, actual_result)
            XLUtils_class.write_data(self.excel_file, self.sheet, i, 6, test_case_status)
        self.log.info(f"Test Results: {result}")

        assert "Fail" not in result
        self.log.info("Test Case test_OrangeHRM_Login_DDT_003 Completed")
        self.log.info("=============================================================")

# pytest -v -s -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome