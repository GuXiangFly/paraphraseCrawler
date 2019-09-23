from analysis.main import MainTask
from setup_data import base_word_fromchengzhi_path

if __name__ == '__main__':
    mainTask = MainTask()
    mainTask.handle_word_to_path(base_word_fromchengzhi_path + "/2、匹配度阈值为0.5去掉0.4部分中检测不合格词典$0.5.txt")
