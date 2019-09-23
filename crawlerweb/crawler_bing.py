
# -*- coding: utf-8 -*-
import os
import time
import urllib.parse
import util.common_utils
import setup_data


# -*- coding: utf-8 -*-
class CrawlerWeb:

    def __init__(self):
        self.web_config_dict = {
            "bing": "https://cn.bing.com/dict/search?q=",
            "baidu": "https://fanyi.baidu.com/#zh/en/",
            "iciba": "http://www.iciba.com/"
        }
        self.base_path = setup_data.base_word_fromchengzhi_path + "/bing/"
        self.base_url = "https://cn.bing.com/dict/search?q="

    def save_html_by_request_word(self, word):
        word = word.replace("\n", "")
        url = self.base_url + word
        file_path = self.base_path + word + ".html"
        if os.path.exists(file_path):
            print("has exist:" + file_path)
            return
        print("request url:" + url)
        url = urllib.parse.quote(url, safe='/:?=')
        try:
            result = util.common_utils.do_get(url)
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
            self.save_html_by_request_word(word)
