#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup


class Novel:
    """
    小说爬取器
    """
    def __init__(self):
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': '',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://www.xbiquge6.com/76_76270/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/59.0.3071.115 Safari/537.36'
        }

        self.domain_url = "https://www.bequge.com"
        self.char_set = "gbk"

    def crawl_detail(self, crawl_url):
        """
        爬取列表页面
        :return:
        """
        try:
            list_html = requests.get(self.domain_url + crawl_url, headers=self.header)
            soup = BeautifulSoup(list_html.content.decode(self.char_set), 'lxml')

            print(" " + soup.select('div.bookname>h1')[0].text)
            # 正文部分
            essay = soup.select('div#content')[0].prettify()

            new_soup = BeautifulSoup(essay, 'lxml')
            print(new_soup.select('div#content')[0].text)

            for link in soup.select('div.bottem2')[0].findAll('a'):
                if link.text == '下一章':
                    return link.get('href')

        except Exception:
            print("crawl fail!")
            raise Exception

    def crawl(self, crawl_url, num):
        next_page = ''
        while num > 0:
            next_page = self.crawl_detail(crawl_url)
            num -= 1
            crawl_url = next_page
            print("------------------------------------------------")

        print("最后一章的地址：" + next_page)


if __name__ == '__main__':
    novel = Novel()
    novel.crawl('/11_11343/2608154.html', 10)
