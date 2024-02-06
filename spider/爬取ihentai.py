import shutil
from lxml import etree
import urllib.request
import os
import pyttsx3


# xpath解析
# （1）解析本地文件
# （2）服务器相应数据 response.read().decode('utf-8') ********
def setDirName(dirName):
    if os.path.exists(f"D:\爬虫\\{dirName}"):
        shutil.rmtree(f"D:\爬虫\\{dirName}")

    os.mkdir(f"D:\爬虫\\{dirName}")


def setMangaUrl(dirName, finPage, keyUrl):
    flag = 0
    for i in range(1, finPage + 1):
        # https://ios.zyy54.top/107950/3/?pline=1
        # url = 'https://img.youwuqu.com/09e8fb0d4dcf0ee2257078f49df44267.jpg'
        url = f'https://i.nhentai.net/galleries/2689804/24.jpg'
        headers = {
            'sec-ch-ua': ' "Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': ' ?0',
            'sec-ch-ua-platform': ' "Windows"',
            'sec-fetch-dest': ' document',
            'sec-fetch-mode': ' navigate',
            'sec-fetch-site': ' none',
            'sec-fetch-user': ' ?1',
            'upgrade-insecure-requests': ' 1',
            'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'

        }

        request = urllib.request.Request(url=url, headers=headers)

        response = urllib.request.urlopen(request)

        coll = response.read().decode("utf-8")
        opener = urllib.request.build_opener()
        opener.addheaders = [('user-agent',
                              ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78')]

        # 解析网页源码
        # 解析服务器响应的文件
        tree = etree.HTML(coll)
        # print(coll)
        # 获取想要的数据
        result = tree.xpath('//p/img/@src')
        # https://img.youwuqu.com/09e8fb0d4dcf0ee2257078f49df44267.jpg
        for line in result:
            line = str(line)

            if "xxx.14a.xyz" in str(line):

                url = line.replace("t.jpg", '.jpg').replace("t.png", '.png').replace("xxx.14a.xyz",
                                                                                     "xxx.z0000000a1.top")
            else:
                url = line.replace("t.jpg", '.jpg').replace("t.png", '.png')

            print(url)
            url1 = url.replace("i0.wp.com/", "").replace('xxx.z0000000a1.top', 'xxx.z0000000a5.top').replace('uploads',
                                                                                                             'g').replace(
                'img.youwuqu.com', 'img111.top')
            print(url)

            name = url.replace("t", "").replace(':', "").replace(".", '').replace('jpg',
                                                                                  '.jpg')
            #
            print(name)
            print(url)
            opener = urllib.request.build_opener()

            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

            urllib.request.install_opener(opener)

            urllib.request.urlretrieve(url1, f"D:/爬虫/{dirName}/{flag + 1}.png")

            flag = flag + 1

        print(f"第{i}页已经下载完成！")

        pyttsx3.speak(f"第{i}页已经下载完成！")


if __name__ == '__main__':
    dirName = 'hh22'
    finPage = 14
    keyUrl = 337202
    # https://img111.top/21fd25b4e5238c4028e2f5397a75119d.jpg

    setDirName(dirName=dirName)
    setMangaUrl(dirName=dirName, finPage=finPage, keyUrl=keyUrl
                )
    pyttsx3.speak(f"全部下载完成")
