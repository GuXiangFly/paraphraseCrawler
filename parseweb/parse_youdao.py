import json
import codecs

all_word_list = []

base_word_fromchengzhi_path = 'D:/neteaseworkfile/paraphraseCrawler/datafromchenzhi'


def read_word_list_by_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f.readlines():
            split = line.split("&&")
            word = split[0]
            paraphrase_str = split[1]
            paraphrase = paraphrase_str.split("#")[0]
            paraphrase_list = [paraphrase]
            item = {
                "word": word,
                "src": "youdao",
                "paraphrase": paraphrase_list
            }
            all_word_list.append(item)


if __name__ == '__main__':
    read_word_list_by_file(base_word_fromchengzhi_path + "/1、匹配度小于0.4不合格中词典$0.4.txt")
    read_word_list_by_file(base_word_fromchengzhi_path + "/2、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5.txt")
    read_word_list_by_file(base_word_fromchengzhi_path + "/3、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5.txt")
    read_word_list_by_file(base_word_fromchengzhi_path + "/4、匹配度小于0.4不合格中词典$0.4（权威词典认为ok）.txt")
    read_word_list_by_file(base_word_fromchengzhi_path + "/5、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5（权威词典认为ok）.txt")
    read_word_list_by_file(base_word_fromchengzhi_path + "/6、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5（权威词典认为ok）.txt")
    json.dump(all_word_list, codecs.open("youdao_result.json", 'w', encoding='utf-8'), ensure_ascii=False)
