import requests
import re


class QSBK:

    def __init__(self):
        self.pageIndex = 2
        self.enable = False
        # 存放段子内容
        self.stores = []

    def getPage(self, pageIndex):
        try:
            qsbk_url = 'http://www.qiushibaike.com/8hr/page/'
            res = requests.get(qsbk_url + str(pageIndex))
            content = res.content.decode('utf-8')[500:10000]
            return content
        except Exception as e:
            print("连接糗百的时候发生异常：" + e.reasion)
            return None

    def getPageItems(self, pageIndex):
        content = self.getPage(pageIndex)
        if not content:
            print("页面加载失败！")
            return None
        pattern = re.compile(
            '<div.*?article.*?h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>', re.S)
        items = re.findall(pattern, content)
        print("解析出段子：%s 个" % len(items))
        return items

    def loadStores(self):
        if not self.enable:
            return None

        if len(self.stores) < 2:
            items = self.getPageItems(self.pageIndex)
            if items:
                for item in items:
                    self.stores.append(item)
                self.pageIndex += 1

    def start(self):
        self.enable = True
        while True:
            self.loadStores()
            if len(self.stores) < 1:
                return None
            print("欢迎查看段子，按Q退出")
            inChar = input()
            if inChar == 'Q':
                return None
            item = self.stores[0]
            print("标题：" + item[0].strip())
            print("内容：" + item[1].strip())
            del self.stores[0]

splider = QSBK()
splider.start()
