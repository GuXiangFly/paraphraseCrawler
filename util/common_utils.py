import urllib.parse
import urllib.request
import os
import socket
import json

socket.setdefaulttimeout(3.0)


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_word_list_by_file(file_path):
    word_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f.readlines():
            word = line.split("&&")[0]
            word_list.append(word)

    return word_list


def do_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req).read()
    page = page.decode('utf-8')
    return page


def is_english_char(ch):
    ch = ch.lower()
    if 97 <= ord(ch) & ord(ch) <= 122:
        return True
    return False


def get_english_str(item):
    item = str(item).lower()
    firstAlpha = ""
    endAlpha = ""
    has_english = False
    for char in item:
        if is_english_char(char):
            firstAlpha = char
            has_english = True
            break
    for char in item:
        if is_english_char(char):
            endAlpha = char
    if (has_english == False):
        return ""
    index = item.index(firstAlpha)
    indexend = item.rindex(endAlpha)
    result = item[index:indexend + 1]
    return result


def load_dict_from_json_file(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    return json_data


def save_the_list_in_file(file_path,list):
    mkdir(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(''.join(list(list)))

if __name__ == '__main__':
    get_english_str("[")
