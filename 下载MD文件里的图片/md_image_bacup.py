# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MyTest
   Description :
   Author :       xiechengfa
   date：          2017/12/19
-------------------------------------------------
"""
import sys
import os
import re
import requests
import urllib

def search(path, word):
    print('*********search path:',path,',word:',word)

    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print('fp')
            download(str(fp))
        elif os.path.isdir(fp):
            search(fp, word)

def download(file_path):
    print('*********download path:',file_path)
    # filename = "test"
    name = file_path.split(u"/")
    filename = name[-1]
    f_md = open(file_path,'rb')

    # all text of md file
    text = f_md.read().decode('utf-8')
    print('text:',text)
    # regex
    img_reg = r'\!{1}\[(.*?)\]\((.*?)\)'
    result = re.findall('!\[(.*)\]\((.*)\)', text)

    filenamearr=filename.split(u'.')
    filename=filenamearr[0]

    for i in range(len(result)):
        img_quote = result[i][0]
        img_url = result[i][1]
        # download img
        request = urllib.request.Request(img_url)
        response = urllib.request.urlopen(request)
        img_contents = response.read()
        # img name spell
        urlname = img_url.split(u"/")
        img_name = filename + '_' + \
                   str(i) + '_' + img_quote + str(urlname[len(urlname) - 1])+'.png'
        print(img_name, ',', img_url)
        # write to file
        f_img = open(img_name, 'wb')
        f_img.write(img_contents)
        f_img.close()
    f_md.close()

instr=input('请输入文件所在文件夹:')
search(instr, '.md')

