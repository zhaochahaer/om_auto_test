from lib.Logger import logger
from lib.sshClient import *
from lib.execCmd import *
from lib.configInfo import *
from server.serverConfig import *

class ServerOptions:
    def __init__(self):
        self.case_path = Userinof.om_auto_test_path + '/shell/'

    def check_database_xtp(self):
        logger.info("check_database_xtp...")
        cmd = "sh " +  self.case_path + sh_check_env_xtp
        try:
            result = ssh_exec(sshclient.conn(Userinof.host_list[0]), cmd)
            # 处理命令执行结果
            if "Success" in result:
                logger.info("Database health check: Success!")
                return True
            else:
                logger.error("Database health check: False!" )
                return False
        finally:
            sshclient.close()




SPtions = ServerOptions()