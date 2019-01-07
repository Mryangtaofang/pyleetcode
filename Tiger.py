import requests
from bs4 import BeautifulSoup
import time


class Tiger:
    def __init__(self):
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': '',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/59.0.3071.115 Safari/537.36'
        }

        self.domain_url = "https://www.laohu8.com"
        self.enter_url = self.domain_url + "/news/all?f=itiger"

    def crawl_list(self):
        """
        爬取列表页面
        :return:
        """
        try:
            list_html = requests.get(self.enter_url, headers=self.header)
            soup = BeautifulSoup(list_html.text, 'lxml')

            detail_url = self.get_detail_url(soup)
            Tiger.download_detail(detail_url)
        except Exception:
            print("crawl fail!")
            raise Exception

    def get_detail_url(self, soup):
        detail_url = []
        for link in soup.find_all('a', "link ellipsis"):
            news = News(title=link.get('title'), url=self.domain_url + link.get('href'))
            detail_url.append(news)
        return detail_url

    @staticmethod
    def download_detail(detail_url):
        if not detail_url:
            return

        try:
            for news in detail_url:
                detail_reuqest = requests.get(news.url)
                detail_soup = BeautifulSoup(detail_reuqest.text, 'lxml')
                print("--------------------------------------------------------")
                print("标题:", news.title)
                print()
                print(detail_soup.select('div.article-content')[0].text)
                print("--------------------------------------------------------")
                time.sleep(1)
        except:
            print("crawl detail fail!")


class News:
    """
    定义新闻对象
    """
    def __init__(self, title, url, pub_time=None):
        self.title = title
        self.url = url
        self.pub_time = pub_time


if __name__ == '__main__':
    tiger = Tiger()
    tiger.crawl_list()
