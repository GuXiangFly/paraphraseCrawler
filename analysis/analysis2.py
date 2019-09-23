from util.common_utils import *
from setup_data import base_word_fromchengzhi_path
import codecs


class MainTask:
    def __init__(self):
        self.main_dict = load_dict_from_json_file("result_final.json")
        self.removed_word = []
        self.all_list_line = []
        self.removed_word_item_dict = {}
        self.saved_word_item_dict = {}
        self.read_removed_word = read_word_list_by_file("removeedwordlist.txt")
        self.read_removed_word_item_dict = load_dict_from_json_file("removed_word_item_dict.json")
        self.read_saved_word_item_dict = load_dict_from_json_file("saved_word_item_dict.json")

    def find_word_in_list(self, word, list):
        if list is None:
            return False
        for list_word in list:
            list_word = str(list_word).replace(" ", "").replace("\n", "").lower()
            word = str(word).replace(" ", "").replace("\n", "").lower()
            if list_word.__eq__(word):
                return True
        return False

    def get_matched_word_item(self):
        for item_key in self.main_dict:
            print("item_key %s" % (item_key))
            youdao_para = self.main_dict[item_key]["youdao"][0]
            baidu_para_list = self.main_dict[item_key]["baidu"]
            iciba_para_list = self.main_dict[item_key]["iciba"]
            bing_para_list = self.main_dict[item_key]["bing"]
            count = 0
            if self.find_word_in_list(youdao_para, baidu_para_list):
                count += 1
            if self.find_word_in_list(youdao_para, bing_para_list):
                count += 1
            if self.find_word_in_list(youdao_para, iciba_para_list):
                count += 1

            item = {item_key: self.main_dict[item_key]}
            if count >= 2:
                print("==this match >2 item_key: %s -- %s" % (item_key, str(self.main_dict[item_key])))
                self.removed_word.append(item_key)
                self.removed_word_item_dict.update(item)
            else:
                self.saved_word_item_dict.update(item)

        with open("removeedwordlist.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(list(set(self.removed_word))))
        json.dump(self.saved_word_item_dict, codecs.open("saved_word_item_dict.json", 'w', encoding='utf-8'),
                  ensure_ascii=False)
        json.dump(self.removed_word_item_dict, codecs.open("removed_word_item_dict.json", 'w', encoding='utf-8'),
                  ensure_ascii=False)

    def handle_word_to_path(self, file_path):
        line_list = []
        print(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            cnt = 0
            for line in f.readlines():
                word = line.split("&&")[0]
                if self.find_word_in_list(word, self.read_removed_word):
                    continue
                line_list.append(line)
                print(word)
        with open(file_path.replace("datafromchenzhi", "datafromchenzhi/result"), 'w', encoding='utf-8') as f:
            f.write(''.join(list(line_list)))

    def get_all_list_line(self):
        self.handle_word_to_path(base_word_fromchengzhi_path + "/1、匹配度小于0.4不合格中词典$0.4.txt")
        self.handle_word_to_path(base_word_fromchengzhi_path + "/2、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5.txt")
        self.handle_word_to_path(base_word_fromchengzhi_path + "/3、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5.txt")
        self.handle_word_to_path(base_word_fromchengzhi_path + "/4、匹配度小于0.4不合格中词典$0.4（权威词典认为ok）.txt")
        self.handle_word_to_path(base_word_fromchengzhi_path + "/5、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5（权威词典认为ok）.txt")
        self.handle_word_to_path(base_word_fromchengzhi_path + "/6、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5（权威词典认为ok）.txt")

    def match_the_dict_strategy_02(self, youdao_para, para_list):
        if para_list is None:
            return False
        if list(para_list).__len__() == 1 and para_list[0] == youdao_para:
            return True
        return False

    def strategy_02_handle(self, item_dict):
        youdao_para = item_dict["youdao"][0]
        count = 0
        if self.match_the_dict_strategy_02(youdao_para, item_dict["baidu"]):
            count += 1
        if self.match_the_dict_strategy_02(youdao_para, item_dict["iciba"]):
            count += 1
        if self.match_the_dict_strategy_02(youdao_para, item_dict["bing"]):
            count += 1

        if count >= 2:
            return True
        else:
            return False

    def handle_word_strategy_02(self, file_path):
        line_list_need_review = []
        line_list_remove = []
        print(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                word = line.split("&&")[0]
                line_need = line.split("####")[0] + "\n"
                if self.strategy_02_handle(self.main_dict[word]):
                    line_list_remove.append(line_need)
                else:
                    line_list_need_review.append(line_need)
        with open(file_path.replace("removedjson", "strategy2Result/savedjson"), 'w', encoding='utf-8') as f:
            f.write(''.join(list(line_list_need_review)))
        with open(file_path.replace("removedjson", "strategy2Result/removedjson"), 'w', encoding='utf-8') as f:
            f.write(''.join(list(line_list_remove)))

    def get_all_list_json(self):
        self.handle_word_strategy_02(base_word_fromchengzhi_path + "/removedjson/1、匹配度小于0.4不合格中词典$0.4.txt")
        self.handle_word_strategy_02(base_word_fromchengzhi_path + "/removedjson/2、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5.txt")
        self.handle_word_strategy_02(base_word_fromchengzhi_path + "/removedjson/3、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5.txt")
        self.handle_word_strategy_02(base_word_fromchengzhi_path + "/removedjson/4、匹配度小于0.4不合格中词典$0.4（权威词典认为ok）.txt")
        self.handle_word_strategy_02(
            base_word_fromchengzhi_path + "/removedjson/5、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5（权威词典认为ok）.txt")
        self.handle_word_strategy_02(
            base_word_fromchengzhi_path + "/removedjson/6、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5（权威词典认为ok）.txt")


if __name__ == '__main__':
    mainTask = MainTask()
    mainTask.get_all_list_json()
