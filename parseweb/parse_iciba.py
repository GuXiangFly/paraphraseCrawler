from lxml import etree
from setup_data import base_word_fromchengzhi_path
import os
from util.common_utils import get_english_str
import codecs, json


class ParseIciba:
    def __init__(self):
        self.xpath_iciba = "//ul[contains(@class,'base-list switch_part')]//li[contains(@class,'clearfix')]//p//span//text()"

    def get_paraphrase_list(self, html_str):
        paraphrase_list = []
        html = etree.HTML(html_str)
        result_str = html.xpath(self.xpath_iciba)
        array_str = str(result_str).split("；")
        for item in array_str:
            item = get_english_str(item)
            if item.strip() == "":
                continue
            paraphrase_list.append(str(item).strip())
        return paraphrase_list

    def get_paraphrase_list_by_word(self, word):
        file_path = base_word_fromchengzhi_path + "/iciba/" + word + ".html"
        with open(file_path, "r", encoding="utf-8") as f:
            html_str = f.read()
        paraphrase_list = self.get_paraphrase_list(html_str)
        item = {
            "word": word,
            "src": "iciba",
            "paraphrase": paraphrase_list
        }
        return item

    def run(self):
        base_dir = base_word_fromchengzhi_path + "/iciba/"
        result_list = []
        for list in os.listdir(base_dir):
            path = os.path.join(base_dir, list)
            if os.path.isfile(path):
                word = list.replace(".html", "")
                item = self.get_paraphrase_list_by_word(word)
                result_list.append(item)
                print("get the word: %15s  item: %s" % (word, str(item)))
        return result_list


if __name__ == '__main__':
    parseIciba = ParseIciba()
    result_list = parseIciba.run()
    print(result_list)
    json.dump(result_list, codecs.open("iciba_result.json", 'w', encoding='utf-8'), ensure_ascii=False)
