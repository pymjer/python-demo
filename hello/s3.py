import requests
import re
from bs4 import BeautifulSoup


# 处理页面标签类
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class BDTB:

    def __init__(self):
        self.pageIndex = 1
        self.enable = False
        self.pageTotal = 0
        # 存放段子内容
        self.stores = []
        self.floorTag = '1'
        self.file = None
        self.floor = 1
        self.defaultTitle = u"百度贴吧"

    def getPage(self, pageIndex):
        try:
            bdtb_url = 'http://tieba.baidu.com/p/3138733512'
            params = {'see_lz': 1, 'pn': pageIndex}
            res = requests.get(bdtb_url, params=params)
            content = res.content.decode('utf-8')
            return content
        except Exception as e:
            print("连接糗百的时候发生异常：" + e.reasion)
            return None

    def getPageTotal(self, content):
        bs = BeautifulSoup(content, "html.parser")
        jumpInput = bs.find(class_='jump_input_bright')
        maxPage = jumpInput['max-page']
        return maxPage

    def parseContent(self, content):
        contents = []
        bs = BeautifulSoup(content, "html.parser")
        left = bs.find(class_='left_section')
        title = left.find(id='j_core_title_wrap').find('h3').text
        contents.append(title)
        postList = left.find(id='j_p_postlist').findAll(class_='l_post')
        for pl in postList:
            floor = pl.find(class_='d_post_content_main').find(
                class_='p_content').find('cc').text
            contents.append(floor)
        return contents

    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorLine = "\n" + \
                    str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+", encoding='utf-8')
        else:
            self.file = open(self.defaultTitle + ".txt", "w+", encoding='utf-8')

    def start(self):
        self.setFileTitle('BDTB')
        content = self.getPage(1)
        pageTotal = self.getPageTotal(content)
        for i in range(1, int(pageTotal) + 1):
            contents = self.parseContent(self.getPage(i))
            self.writeData(contents)

bdtb = BDTB()
bdtb.start()
