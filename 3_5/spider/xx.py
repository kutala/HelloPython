# coding : UTF-8
import csv
import random
import socket
import time
import http.client
import requests
from bs4 import BeautifulSoup
import types

def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    data = body.find('table', {'summary': 'forum_12'})  # 找到id为7d的div
    tbody = data.find_all('tbody')  # 获取ul部分
    for t in tbody: # 对每个li标签中的内容进行遍历
        
        temp = []
        span = t.find('span', id=True)
        a = span.find('a')
        print(a.string)
#         temp.append(.find('a').string)  # 添加到temp中
#         final.append(temp)   #将temp加到final中
 
    return final


def get_content(url , data = None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'gbk'
            # req = urllib.request.Request(url, data, header)
            # response = urllib.request.urlopen(req, timeout=timeout)
            # html1 = response.read().decode('UTF-8', errors='ignore')
            # response.close()
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))
        except socket.timeout as e:
            print( '3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print( '4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print( '6:', e)
            time.sleep(random.choice(range(5, 15)))
            
    return rep.text 
    # return html_text


if __name__ == '__main__':
    url ='http://bbs.hd62.com/forum-12-1.html'
    html = get_content(url)
    result = get_data(html)
    write_data(result, 'weather.csv')
    
    
##python setup.py install
##https://www.crummy.com/software/BeautifulSoup/#Download
##https://github.com/kennethreitz/requests
