from pymysql import *


class SqlAction:
    def __init__(self):
        self.conn = connect(host='tb003x.corp.youdao.com', port=3306, user="dictedit", password="dictedit123outfox",
                            database='dictedit')
        self.word_db_list = []

    def find_word_in_list(self, word, list):
        if list is None:
            return False
        for list_word in list:
            list_word = str(list_word).replace(" ", "").replace("\n", "").lower()
            word = str(word).replace(" ", "").replace("\n", "").lower()
            if list_word.__eq__(word):
                return True
        return False

    def get_the_data(self):
        cur = self.conn.cursor()
        count = cur.execute('select entry from dict_entry_temp where status!=1')
        list_word_tuple = cur.fetchall()
        for tuple_item in list_word_tuple:
            self.word_db_list.append(tuple_item[0])

        print(str(self.word_db_list))

    def handle_word_to_path(self):
        line_list_edited = []
        line_list_not = []

        with open("D:\\neteaseworkfile\paraphraseCrawler\datafromchenzhi\\result\\1、匹配度小于0.4不合格中词典$0.4.txt", 'r',
                  encoding='utf-8') as f:
            cnt = 0
            for line in f.readlines():
                word = line.split("&&")[0]
                if self.find_word_in_list(word, self.word_db_list):
                    line_list_edited.append(line)
                    continue
                line_list_not.append(line)
                print(word)
        with open("D:\\neteaseworkfile\paraphraseCrawler\datafromchenzhi\\result\\1、匹配度小于0.4不合格中词典$0.4_edited.txt", 'w',
                  encoding='utf-8') as f:
            f.write(''.join(list(line_list_edited)))
        with open("D:\\neteaseworkfile\paraphraseCrawler\datafromchenzhi\\result\\1、匹配度小于0.4不合格中词典$0.4_not_edited.txt",
                  'w', encoding='utf-8') as f:
            f.write(''.join(list(line_list_not)))


if __name__ == '__main__':
    sqlaciton = SqlAction()
    sqlaciton.get_the_data()
    sqlaciton.handle_word_to_path()
