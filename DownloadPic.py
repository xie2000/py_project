#coding:utf-8

import urllib
import urllib2
import re
import tool
import os

dir='result/'
imageIndex=0
class DownLoadPic:
    #页面初始化
    def __init__(self):
        self.siteURL = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=android'
        self.tool = tool.Tool()

    #获取索引页面的内容
    def getPage(self):
        request = urllib2.Request(self.siteURL)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def saveIcon(self,iconURL,index):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = dir+str(index)+'.' + fTail
        self.saveImg(iconURL,fileName)

    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
        print 'saveImg:'+imageURL
        print 'fileName:'+fileName
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

    #获取索引界面所有MM的信息，list格式
    def getContents(self):
        page = self.getPage()
        #<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>
        pattern = re.compile('"middleURL":"(.*?)",',re.S)
        items = re.findall(pattern,page)
        index=0;
        # for item in items:
        #     index=index+1;
        #     self.saveIcon(item,index)
        #https://gtd.alicdn.com/sns_logo/i2/TB1XZ1PQVXXXXaJXpXXSutbFXXX.jpg_60x60.jpg
        #http://img2.imgtn.bdimg.com/it/u=3576734052,1089580470&fm=26&gp=0.jpg
        self.saveIcon('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1498221179462&di=ec3cd2b636e31d8e0c1571444ce19e1e&imgtype=0&src=http%3A%2F%2Fupload.news.cecb2b.com%2F2014%2F1030%2F1414632930853.jpg',index)

spider = DownLoadPic()
spider.getContents()