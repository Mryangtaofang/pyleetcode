import os
from urllib.request import urlretrieve
import re
import time


class ImgDownloader:
    """
    图片下载器
    """
    save_path = 'D://image/'

    @staticmethod
    def download(url):
        if not os.access(ImgDownloader.save_path, os.F_OK):
            os.makedirs(ImgDownloader.save_path, exist_ok=True)

        img_url = ImgDownloader.__generate_img_name(url)

        times = 3
        while True:
            if times > 0:
                urlretrieve(url, img_url)
                if os.access(img_url, os.F_OK):
                    print(img_url + " 下载成功!")
                    break
                else:
                    print(img_url + " 重试!")
                    times -= 1
            else:
                print(img_url + " 下载失败!")
                break

    @staticmethod
    def __generate_img_name(url):

        return ImgDownloader.save_path + str(int(time.time())) + os.path.basename(url)

    @staticmethod
    def identifyImgUrl(url):
        if not url:
            return False

        pattern = re.compile(r'\w(\.gif|\.jpeg|\.png|\.jpg|\.bmp)')
        return pattern.search(url) is not None


if __name__ == '__main__':
    ImgDownloader.download('https://ss3.bdstatic.com/70cFv8Sh_'
                           'Q1YnxGkpoWK1HF6hhy/it/u=474815744,3565723171&fm=200&gp=0.jpg')
