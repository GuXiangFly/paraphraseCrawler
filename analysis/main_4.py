from analysis.main import MainTask
from setup_data import base_word_fromchengzhi_path

if __name__ == '__main__':
    mainTask = MainTask()
    mainTask.handle_word_to_path(base_word_fromchengzhi_path + "/4、匹配度小于0.4不合格中词典$0.4（权威词典认为ok）.txt")
