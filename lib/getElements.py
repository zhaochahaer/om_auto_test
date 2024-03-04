from bs4 import BeautifulSoup
import requests

class GetElements:
    
    def get_elements(self,url):
        response = requests.get(url)
        content = response.text

        # 创建BeautifulSoup对象并指定解析器为lxml
        soup = BeautifulSoup(content, 'lxml')

        return soup