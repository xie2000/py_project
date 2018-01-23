# -*- coding:utf-8 -*-
#baidu图片
import requests
import os

class BaiduImages:
    def getManyPages(selft,keyword,pages):
        params=[]
        for i in range(30,30*pages+30,30):
            params.append({
                'tn': 'resultjson_com',
                'ipn': 'rj',
                'ct': 201326592,
                'is': '',
                'fp': 'result',
                'queryWord': keyword,
                'cl': 2,
                'lm': -1,
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': '',
                'st': -1,
                'z': '',
                'ic': 0,
                'word': keyword,
                's': '',
                'se': '',
                'tab': '',
                'width': '',
                'height': '',
                'face': 0,
                'istype': 2,
                'qc': '',
                'nc': 1,
                'fr': '',
                'pn': i,
                'rn': 30,
                'gsm': '1e',
                '1488942260214': ''
            })
        url = 'https://image.baidu.com/search/acjson'
        urls = []
        for i in params:
            urls.append(requests.get(url,params=i).json().get('data'))

        return urls


    def getImg(selft,dataList, localPath):
        if not os.path.exists(localPath):  # 新建文件夹
            os.mkdir(localPath)

        x = 0
        for list in dataList:
            for i in list:
                if i.get('thumbURL') != None:
                    print u"正在下载:"+i.get('thumbURL')
                    ir = requests.get(i.get('thumbURL'))
                    open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
                else:
                    print('图片链接不存在')

baiduImages = BaiduImages();
dataList = baiduImages.getManyPages('王尼玛', 10)  # 参数1:关键字，参数2:要下载的页数
baiduImages.getImg(dataList, 'baidu/') # 参数2:指定保存的路径