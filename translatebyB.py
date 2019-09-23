#!/usr/bin/env python
# encoding: utf-8

import csv
import hashlib
import http.client
import json
import random
import time
import urllib.parse
import urllib.request
import util.common_utils
import setup_data


# 读取文件


def translateByBaidu(q):
    fromLang = "zh"
    toLang = "en"
    appid = '20181228000253069'  # 你的appid(这里是必填的, 从百度 开发者信息一览获取)
    secretKey = 'Bd3ggjrhTjLahqkAerrQ'  # 你的密钥(这里是必填的, 从百度 开发者信息一览获取)

    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode())
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    result = ""
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result = response.read()
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return result


def main():
    word_list = util.common_utils.read_word_list_by_file(setup_data.base_word_fromchengzhi_path + "/wordlist.txt")
    i = 0
    for line in word_list:
        content = line
        i = i + 1
        try:
            response_baidu = json.loads(str(translateByBaidu(content), encoding="utf-8"))['trans_result'][0]['dst']
        except Exception as e:
            time.sleep(60)
            response_baidu = json.loads(str(translateByBaidu(content), encoding="utf-8"))['trans_result'][0]['dst']
        fo1 = open("baidu.txt", "a")
        fo1.write(response_baidu + "\n")
        fo1.close()
        print(i)
        print(line)


if __name__ == '__main__':
    # main()
    response_baidu = json.loads(str(translateByBaidu("澳洲木材"), encoding="utf-8"))
    print(response_baidu)
