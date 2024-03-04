#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import configparser

class omInfo:
    om_auto_test_path=None
    host_list=None
    port = None
    ssh_name=None
    ssh_passwd=None
    web_path=None
    license=None
    mail_list=None

    def __init__(self):
        sys_config_path = "config/sys_config.ini"
        config = configparser.RawConfigParser()
        config.read(sys_config_path)
        
        #omAutoTest
        self.om_auto_test_path = config.get('omAutoTest','om_auto_test_path')
        #sshConnection
        self.host_list = config.get('sshConnection','host_list').split(',')
        self.port = config.get('sshConnection','port')
        self.ssh_name = config.get('sshConnection','ssh_name')
        self.ssh_passwd = config.get('sshConnection','ssh_passwd')
        self.mail_list = config.get('sshConnection','mail_list').split(',')
        #omclient
        self.web_path = config.get('omclient','web_path')
        self.license = config.get('omclient','license')
        self.webdriver = config.get('omclient','webdriver')
         
Userinof = omInfo()