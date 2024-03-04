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
from page.page_deploy_clustlist import PageDeployClustlist
from server.serverOperations import *

class TestDeployClusterlist(unittest.TestCase):

    driver = None
    path_date = os.path.join(os.getcwd(), "data", "deploy","deploy_clusterlist.json")
    json_reader = JsonReader(path_date)

    @classmethod
    def setUpClass(cls):
        if not cls.driver:
            cls.driver = GetDriver().get_web_driver()
            cls.driver.delete_all_cookies()
            cls.deployclustlist = PageDeployClustlist(cls.driver)
            cls.deployclustlist.page_login()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_web_driver()

    def test_deploy_clusterlist_01(self):
        logger.info("测试集群页面的集群名称...")
        result = self.deployclustlist.deploy_clustlist_information()
        test1 = self.json_reader.get_test_data("test_deploy_clusterlist_01")
        expected_clust_name = test1.get("expected_clust_name")
        self.assertIn(expected_clust_name, result[10])
        if expected_clust_name in result[10]:
            logger.info("测试用例执行成功!")
    
    def test_deploy_clusterlist_02(self):
        logger.info("测试集群页面的集群类型...")

    def test_deploy_clusterlist_03(self):
        logger.info("测试集群页面的部署状态...")

    def test_deploy_clusterlist_04(self):
        logger.info("测试集群页面的版本...")

    def test_deploy_clusterlist_05(self):
        logger.info("测试集群页面的主机数...")

    def test_deploy_clusterlist_06(self):
        logger.info("测试集群页面的角色数...")


# if __name__ == '__main__':
#     unittest.main(exit=False)