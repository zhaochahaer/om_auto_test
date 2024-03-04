#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import paramiko
from lib.configInfo import *

class sshClient:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.username = Userinof.ssh_name
        self.password = Userinof.ssh_passwd
        self.port = Userinof.port

    def conn(self,ip):
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=ip, port=self.port, username=self.username, password=self.password)
            return self.ssh
        except:
            print("ssh链接失败!!!")
            return False

    def close(self):
        if self.ssh :
            self.ssh.close()


sshclient = sshClient()