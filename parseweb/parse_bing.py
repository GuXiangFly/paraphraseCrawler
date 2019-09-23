from lxml import etree
from setup_data import base_word_fromchengzhi_path
import os
from util.common_utils import get_english_str
import codecs, json


class ParseBing:
    def __init__(self):
        self.xpath_bing = "//div[contains(@class,'qdef')]//span[contains(@class,'def')]//text()"
        self.xpath_bing = "//div[contains(@class,'qdef')]//li"

    def get_string_for_bing(self, items):
        result = ""
        for item in items:
            result += item
        return result

    def get_paraphrase_list(self, html_str, word):
        paraphrase_list = []
        html = etree.HTML(html_str)
        li_xpath_list = html.xpath(self.xpath_bing)
        for li in li_xpath_list:
            span_pos_text = li.xpath("./span[contains(@class,'pos')]//text()")
            span_def_text = li.xpath("./span[contains(@class,'def')]//text()")
            array_str = self.get_string_for_bing(span_def_text).split(";")
            for item in array_str:
                item = get_english_str(item)
                if item.strip() == "":
                    continue
                paraphrase_list.append(str(item).strip())
        return paraphrase_list

    def get_paraphrase_list_by_word(self, word):
        file_path = base_word_fromchengzhi_path + "/bing/" + word + ".html"
        with open(file_path, "r", encoding="utf-8") as f:
            html_str = f.read()
        paraphrase_list = self.get_paraphrase_list(html_str, word)
        item = {
            "word": word,
            "src": "bing",
            "paraphrase": paraphrase_list
        }
        return item

    def run(self):
        base_dir = base_word_fromchengzhi_path + "/bing/"
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
    parseBing = ParseBing()
    result_list = parseBing.run()
    print(result_list)
    json.dump(result_list, codecs.open("bing_result.json", 'w', encoding='utf-8'), ensure_ascii=False)


#if __name__ == '__main__':
#    parseBing = ParseBing()
#    result_list = parseBing.get_paraphrase_list_by_word("一亲芳泽")
#    print(result_list)