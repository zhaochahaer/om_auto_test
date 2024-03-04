import sys
import unittest
from src.web_login.test_login import TestLogin
from src.dashboard.test_dashboard_services import TestDashboardServices
from htmltestreport import HTMLTestReport
from lib.sendMail import *
from lib.sftpClient import SFTPClient
from lib.configInfo import *
from lib.sshClient import *
from lib.execCmd import *


class OM_test:
    
    report_path = "html/test_report.html"
    
    def run_tests(self,test_suite):
        # 创建测试套件
        test_suites = unittest.TestLoader().loadTestsFromTestCase(test_suite)

        # 运行测试用例
        result = HTMLTestReport(self.report_path).run(test_suites)
        return result

    #上传后端执行代码到所有节点
    def transport_test_files(self):
        remote_path = Userinof.om_auto_test_path + '/shell/'
        logger.info(remote_path)
        #记录一下：这里需要写一个创建目录，如果目录存在，需要清空目录
        cmd = 'rm -rf {} && mkdir -p {}'.format(remote_path,remote_path)
        for ip in Userinof.host_list:
            ssh_exec(sshclient.conn(ip),cmd)
            sftp_client = SFTPClient(remote_path, ip, Userinof.ssh_name, Userinof.ssh_passwd)
            sftp_client.upload('shell/')

    
if __name__ == "__main__":
    om_test = OM_test()
    om_test.transport_test_files()
    module_choice = input("请选择要测试的模块: web_login|dashboard|all: ").strip().lower()

    if module_choice == 'dashboard':
        om_test.run_tests(TestDashboardServices)
    elif module_choice == 'web_login':
        om_test.run_tests(TestLogin)
    elif module_choice == 'all':
        om_test.run_tests(TestLogin)
        om_test.run_tests(TestDashboardServices)
    else:
        logger.error("无效的选择！")
        sys.exit()
    mail.send(om_test.report_path)
