import smtplib
import os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from lib.Logger import logger
from lib.configInfo import *

class SendMail:
    smtpsrvr = "mail.esgyn.cn"  # SMTP server address
    smtpport = 587  # SMTP server port
    username = "publicuser@esgyn.cn"  # SMTP username
    password = "D85vR42tt2"  # SMTP password
    sender = "publicuser@esgyn.cn"  # Sender email address

    def read_email_config(cls):
        email_config = os.path.join(os.getcwd(),'config','email_config')
        with open(email_config,'r', encoding='utf-8') as f:
            content = f.read()
        
        return content
    
    # 构建邮件内容
    def make_html_content(cls):
        content = cls.read_email_config()
        html_content = f"""
        <html>
        <body>
            Hi all:<br>
            {content}
            <strong>3.  测试结果及报告:</strong><br>
            &emsp;&emsp;请查看附件: test_report.html <br>

            Best Regards,<br>
            xin<br>
        </body>
        </html>
    """
        return html_content

    def send(cls,filename):
        message=cls.make_html_content()
        recipient_list=Userinof.mail_list
        today = datetime.now().strftime('%Y%m%d')
        subject = f"[{today}] OM Auto Test "
        try:
            server = smtplib.SMTP(cls.smtpsrvr, cls.smtpport)  # Connect to the SMTP server
            server.starttls()  # Start TLS encryption
            server.login(cls.username, cls.password)  # Login to the SMTP server

            msg = MIMEMultipart()  # Create a new email message

            msg["From"] = cls.sender  # Set the sender of the email
            msg["To"] = ", ".join(recipient_list)  # Set the recipients of the email
            msg["Subject"] = subject  # Set the subject of the email

            msg.attach(MIMEText(message, "html"))  # Add the plain text message to the email

            # 添加附件
            with open(filename, 'rb') as f:
                attachment = MIMEApplication(f.read(), 'html')
                attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
                msg.attach(attachment)

            server.send_message(msg)  # Send the email
            server.quit()  # Disconnect from the SMTP server
            logger.info("Email sent successfully!")
            return True
        except smtplib.SMTPException as e:
            logger.error(e)
            return False
    

mail=SendMail()