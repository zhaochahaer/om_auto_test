from lib.base import Base
import page

class PageOmLogin(Base):

    #输入用户名
    def page_input_username(self,username):
        self.base_input(page.web_login_username,username)

    #输入密码
    def page_input_password(self,password):
        self.base_input(page.web_login_pwd,password)

    #点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.web_login_btn)
    
    #获取信息
    def page_get_text(self):
        welcome_info = self.base_get_text(page.web_success_login)
        return welcome_info

    #点击异常信息
    def page_get_error_info(self):
        return self.base_get_text(page.web_login_error)

    #截屏
    def page_get_img(self):
        self.base_get_img()
    
    #组合操作
    def page_login(self,username="admin", pwd="admin"):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()