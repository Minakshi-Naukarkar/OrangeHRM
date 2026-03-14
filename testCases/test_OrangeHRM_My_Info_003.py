from Utilities.logger import Logger
from Utilities.readConfig import ReadConfig
from pageObjects.Admin_Page import Admin_Page_Class
from pageObjects.Login_Page import Login_Page_Class


class test_OrangeHRM_Admin_003:
    driver = None
    log = Logger.get_logger()
    login_url = ReadConfig.get_login_url()
    employee_name = ReadConfig.get_employee_name()
    username1 = ReadConfig.get_username1()
    password1 = ReadConfig.get_password1()
    confirm_password1 = ReadConfig.get_confirm_password1()

    def test_Admin_004(self):
        self.log.info("Starting Test: Verify OrangeHRM Admin Page")
        self.driver.get(self.login_url)
        self.log.info("Navigated to OrangeHRM Login Page")
        lp = Login_Page_Class(self.driver)
        self.log.info("Entering Username")
        lp.Enter_Username(self.username)
        self.log.info("Entering Password")
        lp.Enter_Password(self.password)
        self.log.info("Clicking Login Button")
        lp.Click_Login_Button()
        self.log.info("Clicking Admin Button")
        Ad = Admin_Page_Class(self.driver)
        Ad.Click_Admin_Button()
        self.log.info("Clicking Add Button")
        Ad.Click_Add_Button()
        self.log.info("Selecting User Role")
        Ad.Select_User_Role("Admin")
        self.log.info("Entering Employee Name")
        Ad.Enter_Employee_Name(self.employee_name)
        self.log.info("Selecting Status")
        Ad.Select_Status("Enabled")
        self.log.info("Entering Username")
        Ad.Enter_User_Name(self.username1)
        self.log.info("Entering Password")
        Ad.Enter_Password(self.password1)
        self.log.info("Entering Confirm Password")
        Ad.Enter_Confirm_Password(self.confirm_password1)
        self.log.info("Clicking Save Button")
        Ad.Click_Save_Button()
