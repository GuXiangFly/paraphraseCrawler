import os
import time
import urllib.parse
import util.common_utils
import setup_data
import util.proxy_util


# -*- coding: utf-8 -*-
class CrawlerWebWithProxy:

    def __init__(self):
        self.web_config_dict = {
            "bing": "https://cn.bing.com/dict/search?q=",
            "baidu": "https://fanyi.baidu.com/#zh/en/",
            "iciba": "http://www.iciba.com/"
        }
        self.proxy_item_list = util.proxy_util.get_xici_proxy_list()
        self.base_path = setup_data.base_word_fromchengzhi_path + "/bing/"
        self.base_url = "https://cn.bing.com/dict/search?q="

    def save_html_by_request_word_with_proxy(self, word, proxy_item):
        word = word.replace("\n", "")
        url = self.base_url + word
        file_path = self.base_path + word + ".html"
        if os.path.exists(file_path):
            print("has exist:" + file_path)
            return
        print("request url:" + url)
        url = urllib.parse.quote(url, safe='/:?=')
        try:
            result = util.proxy_util.request_with_proxy(url, proxy_item)
            util.common_utils.mkdir(self.base_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(result)
                print("save:" + file_path)
            time.sleep(0.3)
        except Exception as e:
            return

    def save_the_html_by_list(self, word_list):
        return

    def run(self, web_type):
        self.base_path = setup_data.base_word_fromchengzhi_path + "/" + web_type + "/"
        self.base_url = self.web_config_dict[web_type]
        word_list = util.common_utils.read_word_list_by_file(setup_data.base_word_fromchengzhi_path + "/wordlist.txt")
        for word in word_list:
            if len(self.proxy_item_list) <= 1:
                self.proxy_item_list = util.proxy_util.get_xici_proxy_list()
            proxy_item = self.proxy_item_list.pop(1)
            self.save_html_by_request_word_with_proxy(word, proxy_item)
