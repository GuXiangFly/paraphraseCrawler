import os
import time
import urllib.parse
import util.common_utils
import setup_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--dns-prefetch-disable")

class DriverCrawler:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.web_config_dict = {
            "bing": "https://cn.bing.com/dict/search?q=",
            "baidu2": "https://fanyi.baidu.com/#zh/en/",
            "iciba": "http://www.iciba.com/"
        }
        self.base_path = setup_data.base_word_fromchengzhi_path + "/baidu2/"
        self.base_url = "https://fanyi.baidu.com/#zh/en/"

    def save_html_by_request_word(self, word):

        word = word.replace("\n", "")
        url = self.base_url + word
        file_path = self.base_path + word + ".html"
        if os.path.exists(file_path):
            print("has exist:" + file_path)
            return
        print("request url:" + url)
        url = urllib.parse.quote(url, safe='#/:?=')
        self.driver.get("chrome://apps/")
        self.driver.get(url)
        time.sleep(3)
        result = self.driver.page_source
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(result)
            print("save:" + file_path)


    def save_the_html_by_list(self, word_list):
        return

    def run(self, web_type):
        self.base_path = setup_data.base_word_fromchengzhi_path + "/" + web_type + "/"
        self.base_url = self.web_config_dict[web_type]
        word_list = util.common_utils.read_word_list_by_file(setup_data.base_word_fromchengzhi_path + "/wordlist.txt")
        for word in word_list:
            self.save_html_by_request_word(word)


if __name__ == '__main__':
    selenium = DriverCrawler()
    selenium.run("baidu2")