import os
import sys
import paramiko
from lib.Logger import logger

_XFER_FILE = 1
_XFER_DIR = 2

class SFTPClient:
    def __init__(self, remote_path, host, user, password, port=22):
        """
        初始化SFTP客户端。
        param remote_path: 将文件上传到的远程路径。
        param host: SFTP服务器主机。
        param user: SFTP用户名。
        param password: SFTP密码。
        param port: SFTP服务器端口(默认为22)。
        """
        self.host = host
        self.remote_path = remote_path

        self.transport = paramiko.Transport((self.host, port))
        self.transport.connect(username=user, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def uploadDir(self, local_dir='./', remote_dir='./'):
        """
        将本地目录上传到远程SFTP服务器。
        param local_dir: 要上传的本地目录路径。
        param remote_dir: 要上传到的远程目录路径。
        """
        if not os.path.isdir(local_dir):
            return

        for file in os.listdir(local_dir):
            src = os.path.join(local_dir, file)
            if os.path.isfile(src):
                self.uploadFile(src, file, os.path.join(self.remote_path, remote_dir))
            elif os.path.isdir(src):
                try:
                    logger.info('子路径 ==', file)
                    self.sftp.mkdir(os.path.join(self.remote_path, remote_dir, file))
                except Exception as e:
                    sys.stderr.write(f'创建目录时出错：{e}')

                self.uploadDir(src, os.path.join(remote_dir, file, '/'))

    def uploadFile(self, local_path, remote_filename, remote_path):
        """
        将本地文件上传到远程SFTP服务器。

        param local_path: 要上传的本地文件路径。
        param remote_filename: 远程文件名。
        param remote_path: 远程目录路径。
        """
        if not os.path.isfile(local_path):
            return

        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../', local_path)
        logger.info('+++ 上传 {} 到 {}:{}'.format(file_path, self.host, os.path.join(remote_path, remote_filename)))
        try:
            self.sftp.put(file_path, os.path.join(remote_path, remote_filename))
        except Exception as e:
            sys.stderr.write(f'上传文件时出错：{e}')

    def __filetype(self, src):
        """
        确定源文件类型（文件或目录）。

        param src: 源文件路径。
        return: 包含文件类型（文件或目录）和文件名的元组。
        """
        if os.path.isfile(src):
            index = src.rfind('\\') if '\\' in src else src.rfind('/')
            return _XFER_FILE, src[index + 1:]
        elif os.path.isdir(src):
            return _XFER_DIR, ''

    def upload(self, src):
        """
        将文件或目录上传到远程SFTP服务器。

        param src: 源文件或目录路径。
        """
        filetype, filename = self.__filetype(src)
        logger.info("文件类型 =={},文件名 =={}" .format(filetype,filename))
        if filetype == _XFER_DIR:
            self.srcDir = src
            self.uploadDir(self.srcDir)
        elif filetype == _XFER_FILE:
            self.uploadFile(src, filename, self.remote_path)
        self.close()

    def close(self):
        """关闭SFTP连接。"""
        self.sftp.close()
        self.transport.close()

# sftp_client = SFTPClient('/opt/om_auto_test', '10.14.40.184', 'root', 'esg123.com')
# sftp_client.upload('../shell')
