import page
from page.page_om_login import PageOmLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.Logger import logger

class PageDeployClustlist(PageOmLogin):
    
    #集群列表信息
    def deploy_clustlist_information(self):
        td_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(page.deploy_clustlist)
        )

        clust_name_list = []
        for td in td_elements:
            clust_name_list += td.text.split('\n')

        logger.info(clust_name_list)
        return clust_name_list