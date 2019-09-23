# -*- coding: utf-8 -*-
from util.common_utils import *
import setup_data
import codecs


class MainAnalysis:
    def __init__(self):
        self.xpath_baidu = "//strong[contains(@class,'dict-comment-mean')]//text()"

        self.final_data_list = []

        self.list_baidu = load_dict_from_json_file("baidu_result.json")
        self.list_iciba = load_dict_from_json_file("iciba_result.json")
        self.list_bing = load_dict_from_json_file("bing_result.json")
        self.list_youdao = load_dict_from_json_file("youdao_result.json")
        self.final_data_dict = {}

    def get_item_from_list_by_word(self, word, list):
        for item in list:
            if (item['word'] == word):
                return item


    def get_item_from_list_by_word_paraphrase(self, word, list):
        for item in list:
            if (item['word'] == word):
                return item['paraphrase']

    def get_all_data_word_item(self, word):
        baidu_item = self.get_item_from_list_by_word_paraphrase(word, self.list_baidu)
        iciba_item = self.get_item_from_list_by_word_paraphrase(word, self.list_iciba)
        bing_item = self.get_item_from_list_by_word_paraphrase(word, self.list_bing)
        youdao_item = self.get_item_from_list_by_word_paraphrase(word, self.list_youdao)

        item_dict = {
            word: {
                "youdao": youdao_item,
                "baidu": baidu_item,
                "iciba": iciba_item,
                "bing": bing_item
            }
        }
        print(item_dict)
        self.final_data_dict.update(item_dict)

    def get_all_json_list(self):
        word_list = read_word_list_by_file(setup_data.base_word_fromchengzhi_path + "/wordlist.txt")
        for word in word_list:
            self.get_all_data_word_item(word.strip())
        json.dump(self.final_data_dict, codecs.open("result_final.json", 'w', encoding='utf-8'), ensure_ascii=False)


if __name__ == '__main__':
    mainAnalysis = MainAnalysis()
    mainAnalysis.get_all_json_list()
