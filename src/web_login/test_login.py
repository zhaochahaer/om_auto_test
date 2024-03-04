import os
import sys
sys.path.append('./')

import unittest
from lib.getDriver import GetDriver
from page.page_om_login import PageOmLogin
from lib.JsonReader import JsonReader
from lib.Logger import logger
class TestLogin(unittest.TestCase):

    driver = None
    path_date = os.path.join(os.getcwd(), "data", "web_login","login_data.json")
    json_reader = JsonReader(path_date)

    @classmethod
    def setUpClass(cls):
        #获取driver
        cls.driver = GetDriver().get_web_driver()
        cls.driver.delete_all_cookies()
        cls.login = PageOmLogin(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_web_driver()
    
    def setUp(self):
        self.driver.refresh()

    def test_om_login_error_user_01(self):
        # 输入错误的用户名
        test_data01 = self.json_reader.get_test_data("test_om_login_error_user_01")
        username01 = test_data01.get("username")
        password01 = test_data01.get("password")
        expected_error_message = test_data01.get("expected_error_message")

        self.login.page_login(username01, password01)
        error_info = self.login.page_get_error_info()
        self.assertIn(expected_error_message, error_info)

    def test_om_login_error_pwd_02(self):
        # 输入错误的密码
        test_data02 = self.json_reader.get_test_data("test_om_login_error_pwd_02")
        username02 = test_data02.get("username")
        password02 = test_data02.get("password")
        expected_error_message = test_data02.get("expected_error_message")

        self.login.page_login(username02, password02)
        error_info = self.login.page_get_error_info()
        self.assertIn(expected_error_message, error_info)


    def test_om_login_success_03(self):
        #登录成功
        test_data03 = self.json_reader.get_test_data("test_om_login_success_03")
        username = test_data03.get("username")
        password = test_data03.get("password")
        expected_welcome_message = test_data03.get("expected_welcome_message")

        self.login.page_login(username, password)
        welcome_info = self.login.page_get_text()
        # self.login.page_get_img() #注：截屏占60KB
        logger.info("查找到的元素是：{}".format(welcome_info))
        self.assertIn(expected_welcome_message, welcome_info)
        self.login.page_get_img()

# if __name__ == '__main__':
#     unittest.main(exit=False)
