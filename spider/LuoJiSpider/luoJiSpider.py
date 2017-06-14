import sys
import importlib
import time
import urllib
import urllib.parse
import numpy as np
import urllib.request
import es
from bs4 import BeautifulSoup

importlib.reload(sys)

# Some User Agents
hds = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
       {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]


def book_spider():
    # first 3057 secend 2275
    page_num = 4487
    book_list = []
    try_times = 0

    while(1):
        page_num += 1
        url = 'http://www.luojiji.com/thread-' + str(page_num) + '-1-1.html'
        # time.sleep(np.random.rand() * 2)
        print('page_num: {}, request: {}'.format(page_num, url))
        # Last Version
        try:
            req = urllib.request.Request(url, headers=hds[page_num % len(hds)])
            source_code = urllib.request.urlopen(req).read()
            plain_text = str(source_code.decode('utf-8'))
            soup = BeautifulSoup(plain_text, "html.parser")
            list_soup = soup.find('td', {'class': 't_f'})

            try_times += 1
            if list_soup is None and try_times < 100:
                continue
            elif list_soup is None or len(list_soup) < 1:
                print("list_soup is None！break!")
                break  # Break when no informatoin got after 200 times requesting

            title = list_soup.find('div').text
            content = list_soup.text

            try_times = 0  # set 0 when got valid information
            print('Downloading Information From Page %d' % page_num)
            save_book_to_es(page_num, title, content)
        except urllib.request.HTTPError as e:
            print(e)
            continue
        except AttributeError:
            print("web page error！continue!")
            continue

    return book_list


def save_book(page_num, title, content):
    fileName = './{}-{}.txt'.format(page_num, title)
    f = open(fileName, 'w', encoding='utf-8')
    f.write(content)
    f.close()
    print('write file %s success!' % fileName)


def save_book_to_es(page_num, title, content):
    es.es_index(page_num, title, title, content)
    print('write file %s success!' % title)


if __name__ == '__main__':
    book_spider()
