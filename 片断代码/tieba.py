#coding=utf-8
#贴吧
#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re
import os

#定义一个getHtml()函数
def getHtml(url):
    page = urllib.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html,localPath):
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)

    reg = r'img class="BDE_Image" src="(.+?\.jpg)" size='    #正则表达式，得到图片地址
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
        urllib.urlretrieve(imgurl,localPath+'\%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/5155229484")
print getImg(html,'tieba/')