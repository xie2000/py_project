# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import os
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webelement import WebElement

class DownPicOfWeb:
    def __init__(self):
        pass

    def paserWeb(self, url, dirPath):
        # 新建文件夹
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        driver = webdriver.Ie()
        driver.get(url)
        # 打印加载完成的html
        # print 'page:'+driver.page_source
        # page = etree.HTML(driver.page_source)

        #方法1
        for element in driver.find_elements_by_xpath("//div[@id='J_DivItemDesc']/p/img"):
            #打印所有字段
            # print element.get_attribute('outerHTML')
            self.saveImg(element.get_attribute('src'), dirPath)

        #方法2
        # for element in page.xpath(u"//div/div/img[@class='ELazy-loading']"):
        #     print element.attrib['data-lazyload']
        driver.quit()

    # 保存图片
    def saveImg(self, iconURL, dirPath):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        splitName =splitPath.pop().split('/')
        name = splitName.pop()
        iconPath=dirPath + name + '.' + fTail;
        if os.path.exists(iconPath):
            print name+' is exist'
        else:
            self.downImg(iconURL, iconPath)

    #传入图片地址，文件名，保存单张图片
    def downImg(self, imageURL, fileName):
        print 'imgUrl:'+imageURL+",fileName:"+fileName
        if not imageURL.startswith('http'):
            imageURL='http:'+imageURL
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

downPicOfWeb =  DownPicOfWeb()
downPicOfWeb.paserWeb("https://item.taobao.com/item.htm?spm=a219r.lm874.14.1.uvLL8N&id=540017924481&ns=1&abbucket=20","downpic/")
