import page
from page.page_om_login import PageOmLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.Logger import logger

class DashboardServices(PageOmLogin):

    #点击监控
    def dashboard_page(self):
        self.base_click(page.dashboard_page)
    
    #点击服务
    def dashboard_service_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(page.dashboard_services_page)
        )
        self.base_click(page.dashboard_services_page)
    
    #刷新节点数
    def dashboard_service_Refresh_node_count(self):
        self.base_click(page.dashboard_services_Refresh_node_count_button)

    #服务管理
    def dashboard_service_management(self):
        self.base_click(page.dashboard_services_management_button)

    #主机 
    def dashboard_service_host(self):
        self.base_click(page.dashboard_services_host_button)

    # DB server stop
    def dashboard_service_database_stop(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(page.dashboard_service_database_stop_button)
        )
        button_element = self.base_find(page.dashboard_service_database_stop_button)
        if button_element and not button_element.is_enabled():
            logger.info("DB server stop button is disabled.")
            return False  # 返回 False 表示按钮不可点击
        self.base_click(page.dashboard_service_database_stop_button)

    # DB server start
    def dashboard_service_database_start(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(page.dashboard_service_database_start_button)
        )
        button_element = self.base_find(page.dashboard_service_database_start_button)
        if button_element and not button_element.is_enabled():
            logger.info("DB server start button is disabled.")
            return False  # 返回 False 表示按钮不可点击
        self.base_click(page.dashboard_service_database_start_button)

    # DB server restart
    def dashboard_service_database_restart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(page.dashboard_service_database_restart_button)
        )
        button_element = self.base_find(page.dashboard_service_database_restart_button)
        if button_element and not button_element.is_enabled():
            logger.info("DB server restart button is disabled.")
            return False  # 返回 False 表示按钮不可点击
        self.base_click(page.dashboard_service_database_restart_button)

    #操作数据库点击确定
    def dashboard_service_database_yes(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(page.dashboard_service_database_yes)
        )
        self.base_click(page.dashboard_service_database_yes)

    #获取主机数
    def dashboard_service_hosts_num(self):
        return self.base_get_text(page.dashboard_service_hosts)

    #获取实例数
    def dashboard_service_instances_num(self):
        return self.base_get_text(page.dashboard_service_instances)

    #角色信息
    def dashboard_service_relo(self):

        # 获取特定tr元素内的td元素
        td_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(page.dashboard_service_role_tbody)
        )

        role_info_list = []  # 用于存储角色信息的列表
        current_row_data = []

        for td in td_elements:
            row_data = td.text
            if row_data:
                current_row_data.append(row_data)
            else:
                # 当 row_data 为空时，将 current_row_data 添加到 role_info_list，并重置 current_row_data
                if current_row_data:
                    role_info_list.append(current_row_data)
                    current_row_data = []


        logger.info(role_info_list)
        return role_info_list
    
    #角色表名
    def dashboard_service_relo_name(self):
         # 获取特定tr元素
        td_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(page.dashboard_service_role_thead)
        )

        role_name_list = []  # 用于存储角色信息的列表

        # print(td_elements)
        for td in td_elements:
            role_name_list += td.text.split('\n')

        logger.info(role_name_list)
        return role_name_list

    
    #点击最近的命令
    def dashboard_service_global_recent_commands(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(page.components_global_header)
        )
        self.base_click(page.components_global_header)

    # 获取正在运行的命令
    def dashboard_service_global_option(self):
        table_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(page.components_global_header_option)
        )

        commands_info = []
        for td in table_element:
            commands_info += td.text.split('\n')

        # logger.info(commands_info)
        if commands_info:
            latest_command_info = commands_info[9:13]
            logger.info("最新执行的命令：{}".format(latest_command_info))
            return latest_command_info
        else:
            logger.error("没有找到任何命令信息")
            return None

    #选择操作（需要选择角色，才能操作，按钮默认是disable）
    def dashboard_service_relo_operation(self):
        pass

    #组合
    def dashboard_service_all(self):
        self.dashboard_page()
        self.dashboard_service_page()


    

