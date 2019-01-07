import requests
from urlextract import URLExtract
from DownloadImg import ImgDownloader
import urllib.parse


class BaiduImg:
    """
    爬取百度图片
    """

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

        # 关键词
        self.keyword = '胸器'
        # 下载的图片数量
        self.img_num = 100

        self.page_size = 30
        self.page = 0
        self.img_urls = set()

    def get_enter_url(self):
        encode_keyword = urllib.parse.quote(self.keyword)
        return "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&" \
               "queryWord=" + encode_keyword + "&cl=2&lm=-1&adpicid=&" \
               "st=-1&word=" + encode_keyword + "&face=0&istype=2&nc=1&pn=" \
               + str(self.page) + "&rn=30"

    def crawl_list(self):
        """
        爬取列表页面
        :return:
        """
        try:
            enter_url = self.get_enter_url()
            print("入口地址:" + enter_url)
            list_html = requests.get(enter_url, headers=self.header)
            # 抽取url
            extractor = URLExtract()

            url_set = set(extractor.gen_urls(list_html.text))
            if not url_set:
                print('没有要下载的链接!')
                return

            for url in url_set:
                if ImgDownloader.identifyImgUrl(url):
                    self.img_urls.add(url)

        except Exception:
            print("crawl fail!")
            raise Exception

    def crawl(self):

        while True:
            if len(self.img_urls) < self.img_num:
                self.page += self.page_size
                self.crawl_list()
            else:
                break

        for img_url in self.img_urls:
            print("正在下载：" + img_url)
            ImgDownloader.download(img_url)


if __name__ == '__main__':
    tencent = BaiduImg()
    tencent.crawl()
