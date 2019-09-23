from analysis.main import MainTask
from setup_data import base_word_fromchengzhi_path

if __name__ == '__main__':
    mainTask = MainTask()
    mainTask.handle_word_to_path(base_word_fromchengzhi_path + "/3、匹配度大于0.5合格去掉小于0.5不合格中词典检测$=0.5.txt")
