import inspect
import logging
class Logger:
    @staticmethod
    def get_logger():
        name = inspect.stack()[1][1]
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('.\\Logs\\OrangeHRM_Login.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger