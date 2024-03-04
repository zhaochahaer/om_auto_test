from selenium.webdriver.common.by import By


"""
page_om_login页面
"""
#用户名
web_login_username = By.CSS_SELECTOR,".ant-input#userName"
#密码
web_login_pwd = By.CSS_SELECTOR,".ant-input#password"
#登录
web_login_btn = By.CSS_SELECTOR, ".ant-btn.antd-pro-pages-user-login-components-login-index-submit.ant-btn-primary.ant-btn-lg.ant-btn-two-chinese-chars"
#登录成功信息
web_success_login = By.CSS_SELECTOR,"#root > div > section > aside > div > ul > li.ant-menu-submenu.ant-menu-submenu-inline.ant-menu-submenu-selected > div > span > span:nth-child(2)"
#异常信息
web_login_error = By.CSS_SELECTOR, "#root > div > div.antd-pro-layouts-user-layout-content > div.antd-pro-pages-user-login-style-main > div > form > div.ant-alert.ant-alert-error > span.ant-alert-message" 


"""
global
"""
components_global_header = By.CSS_SELECTOR, '.antd-pro-components-global-header-index-action .antd-pro-components-global-header-index-badge'
components_global_header_option = By.CSS_SELECTOR, 'div.ant-modal-content'


"""
page_deploy_clustlist页面
"""
deploy_clustlist= By.CSS_SELECTOR , "div.ant-table-content"






"""
page_dashboard_services页面
"""
#监控
dashboard_page = By.XPATH, '//*[@id="root"]/div/section/aside/div/ul/li[2]/div/span/span[2]'
#服务
dashboard_services_page = By.XPATH, '//a[contains(@href, "/xtp/dashboard/services")]'
#刷新节点数
dashboard_services_Refresh_node_count_button = By.XPATH, '//*[@id="root"]/div/section/section/div[1]/main/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/button/span'
#服务管理
dashboard_services_management_button = By.XPATH, '//*[@id="root"]/div/section/section/div[1]/main/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/button/span'
#主机
dashboard_services_host_button = By.XPATH, "//button[contains(@class, 'ant-btn-default') and contains(@class, 'ant-btn-two-chinese-chars')]"
#database stop
dashboard_service_database_stop_button = By.XPATH, "//button[@class='ant-btn ant-btn-sm' and contains(span/@class, 'antd-pro-pages-v2-services-index-stop-disabled')]"
#database start
dashboard_service_database_start_button = By.XPATH, "//button[@class='ant-btn ant-btn-sm' and contains(span/@class, 'antd-pro-pages-v2-services-index-start-icon')]"
#database restart
dashboard_service_database_restart_button = By.XPATH, "//button[@class='ant-btn ant-btn-sm' and contains(span/@class, 'antd-pro-pages-v2-services-index-restart-icon')]"
#确认是否重启：
dashboard_service_database_yes = By.XPATH,"//div[@class='ant-modal-confirm-btns']//button[@class='ant-btn ant-btn-primary']/span[text()='是']"
# 主机数
dashboard_service_hosts = By.XPATH, "//div[@class='antd-pro-pages-v2-services-index-cluster-item-label' and contains(text(), '主机数')]"
#获取实例数
dashboard_service_instances = By.XPATH, "//div[@class='antd-pro-pages-v2-services-index-cluster-item-label' and contains(text(), '实例数')]"
#角色表
dashboard_service_role = By.XPATH, '//*[@id="ant-design-pro-table"]/div/div/div[2]/div/div/div/div/div/table/tbody'
dashboard_service_role_thead = By.XPATH,'//*[@id="ant-design-pro-table"]/div[1]/div/div[2]/div/div/div/div/div/table/thead/tr'
dashboard_service_role_tbody = By.XPATH, '//*[@id="ant-design-pro-table"]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td'
#选中的操作（需要选择角色，才能操作，按钮默认是disable）
dashboard_service_role_dropdown = By.CSS_SELECTOR,"#ant-design-pro-table > div.ant-card > div > div.ant-pro-table-toolbar > div.ant-pro-table-toolbar-title"

