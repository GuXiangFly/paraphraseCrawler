import requests
from lxml import etree
import telnetlib
import time
from util.common_utils import do_get

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}


def request_with_proxy(url, item):
    httptype = str(item['type']).lower()
    ipport = httptype + "://" + item['ip'] + ":" + item['port']
    proxy = {'http': ipport}
    try:
        response = requests.get(url, proxies=proxy, headers=headers, timeout=1)
        result = str(ipport) + " " + str(response.status_code)
        print(result)
    except Exception as e:
        print(e)


def get_content_list(html_str):
    html = etree.HTML(html_str)
    # print(etree.tostring(html).decode())
    tr_list = html.xpath('//*[@id="ip_list"]//tr')
    ip_item_list = []
    for tr in tr_list:
        try:
            if len(tr.xpath('./td[2]/text()')) == 0:
                continue
            item = {}
            item['ip'] = tr.xpath('./td[2]/text()')[0]
            item['port'] = tr.xpath('./td[3]/text()')[0] if len(tr.xpath('./td[3]/text()')) > 0 else None
            item['address'] = tr.xpath('./td[4]/text()')[0] if len(tr.xpath('./td[4]/text()')) > 0 else None
            item['type'] = tr.xpath('./td[6]/text()')[0] if len(tr.xpath('./td[6]/text()')) > 0 else None
            item['keep_time'] = tr.xpath('./td[7]/text()')[0] if len(tr.xpath('./td[7]/text()')) > 0 else None
            ip_item_list.append(item)
            print("get proxy:" + item)
        except Exception as e:
            print("except:", e)
    return ip_item_list


def get_xici_proxy_list():
    html_str = do_get("https://www.xicidaili.com/")
    ip_item_list = get_content_list(str(html_str))
    return ip_item_list
