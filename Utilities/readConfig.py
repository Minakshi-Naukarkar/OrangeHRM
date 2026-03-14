import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_username():
        return config.get("login", "username")

    @staticmethod
    def get_password():
        return config.get("login", "password")

    @staticmethod
    def get_login_url():
        return config.get("urls", "login_url")

    @staticmethod
    def get_employee_name():
        return config.get("login", "employee_name")

    @staticmethod
    def get_username1():
        return config.get("login", "username1")

    @staticmethod
    def get_password1():
        return config.get("login", "password1")

    @staticmethod
    def get_confirm_password1():
        return config.get("login", "confirm_password1")