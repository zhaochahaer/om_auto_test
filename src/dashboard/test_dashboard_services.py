#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import os
import sys
import time
sys.path.append('./')

from lib.Logger import logger
from lib.JsonReader import JsonReader
from lib.configInfo import *
import unittest
from lib.getDriver import GetDriver
from page.page_dashboard_services import DashboardServices
from server.serverOperations import *

class TestDashboardServices(unittest.TestCase):


    driver = None
    path_date = os.path.join(os.getcwd(), "data", "web_login","login_data.json")
    json_reader = JsonReader(path_date)

    @classmethod
    def setUpClass(cls):
        if not cls.driver:
            cls.driver = GetDriver().get_web_driver()
            cls.driver.delete_all_cookies()
            cls.dashboardservices = DashboardServices(cls.driver)
            cls.dashboardservices.page_login()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_web_driver()

    
    def test_dashboard_service_01(self):
        # 重启数据库
        self.dashboardservices.dashboard_service_all()
        time.sleep(1)
        self.dashboardservices.dashboard_service_database_restart()
        time.sleep(1)
        self.dashboardservices.dashboard_service_database_yes()
        time.sleep(3)
        self.dashboardservices.dashboard_service_global_recent_commands()
        time.sleep(3)
        # 获取重启数据库的命令信息
        command = None
        max_attempts = 10  # 最多重试10次，每次等待3秒
        for _ in range(max_attempts):
            command = self.dashboardservices.dashboard_service_global_option()
            logger.info(command)
            if command and command[2] == "成功":
                break
            time.sleep(10)
        
        # 页面端断言是否成功
        self.assertIsNotNone(command, "未能获取到数据库启动命令信息")
        self.assertEqual(command[2], "成功", "数据库启动命令状态不为成功")

        # 后端断言是否成功
        result_database_healthy = SPtions.check_database_xtp()
        self.assertTrue(result_database_healthy, "测试用例失败！")

# if __name__ == '__main__':
#     unittest.main(exit=False)
