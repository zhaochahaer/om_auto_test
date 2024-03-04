from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.Logger import logger
import os
import time

class Base:
    # 初始化方法
    def __init__(self, driver):
        """
        初始化函数，接收 WebDriver 对象。
        :param driver: WebDriver 对象
        """
        logger.info("正在初始化,driver对象:{}".format(driver))
        self.driver = driver

    # 查找元素方法
    def base_find(self, loc, timeout=15, poll=0.5):
        logger.info("正调查找击元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        logger.info("正调用点击元素：{}".format(loc))
        element = self.base_find(loc)
        element.click()

    # 输入方法
    def base_input(self, loc, value):
        logger.info("正调用输入元素方法：{} 输入内容：{}".format(loc,value))
        # 获取元素
        el = self.base_find(loc)
        # 清空
        logger.info("输入框清空前的值：{}".format(el.get_attribute("value")))
        # self.driver.execute_script("arguments[0].value = '';", el) # 使用 JavaScript 清空输入框
        time.sleep(1)
        el.clear()
        # 输入
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        logger.info("正调用获取元素信息方法：{}".format(loc))
        return self.base_find(loc).text

    # 截图方法
    def base_get_img(self):
        logger.info("正调用截图方法")
        img_path = os.path.join(os.getcwd(), "img","{}.png".format(time.strftime("%Y-%m-%d_%H-%M-%S")))
        self.driver.get_screenshot_as_file(img_path)

 
    # 判断元素是否存在
    def base_element_is_exist(self, loc, timeout=5):

        try:
            self.base_find(loc, timeout=timeout)
            logger.info("元素{}, 存在!".format(loc))
            return True
        except:
            logger.warning("元素{}, 不存在!".format(loc))
            return False

