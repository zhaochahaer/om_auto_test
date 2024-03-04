from selenium import webdriver
from lib.configInfo import *
from lib.Logger import logger
class GetDriver:

    __web_driver = None

    @classmethod
    def get_web_driver(cls, browser=Userinof.webdriver):
        if cls.__web_driver is None :
            try:
                if browser.lower() == "chrome":
                    cls.__web_driver = webdriver.Chrome()
                elif browser.lower() == "firefox":
                    cls.__web_driver = webdriver.Firefox()
                else:
                    raise ValueError("Invalid browser name. Supported browsers: Chrome, Firefox")

                cls.__web_driver.maximize_window()
                cls.__web_driver.get(Userinof.web_path)
            except Exception as e:
                logger.error(f"Error creating WebDriver: {str(e)}")

        return cls.__web_driver
    
    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            try:
                cls.__web_driver.quit()
            except Exception as e:
                logger.warning(f"Error quitting WebDriver: {str(e)}")
            finally:
                cls.__web_driver = None