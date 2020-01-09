from flask import Flask, request, render_template, jsonify, json,send_file,make_response
from sqlalchemy import text
from sqlalchemy import or_,and_
from sqlalchemy.sql.expression import func
from flask_sqlalchemy  import SQLAlchemy
from flask_paginate import Pagination,get_page_parameter
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
import matplotlib
import numpy as np 
from io import BytesIO
import pymysql
import random
import jieba
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import jieba.analyse as analyse
from wordcloud import WordCloud
from scipy.misc import imread
from os import path
import jieba.posseg as pseg
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
from scipy.misc import imread
import jieba.analyse as analyse
from wordcloud import WordCloud
import numpy as np
import matplotlib.image as img
import time
from pyecharts import Map, Geo
import logging
import os
# txt是原文书
data_1 = r"E:\毕设项目\txt文本"
# 转化后的json文件
data_2 = "E:/毕设项目/结果2"
# 对json特殊处理（去除特殊符号）
char_3=r"E:\毕设项目\文本处理最终结果"

info =4465

for k in range(4999):#("C:/Users/admin/Desktop/未处理的文本2"):
    print("=====================================next===========================================================")
    # domain = os.path.abspath(data_1)#("C:/Users/admin/Desktop/未处理的文本2")
    # file_string = os.path.join(domain,info)
    
    string_txt = data_1 + "/" +str(info)+".txt"
    read_data = open(string_txt,'r',encoding='utf-8')
    # read_data = open(data_1,'rb',encoding='utf-8')
    char = "/"
    char_txt = data_2+char+str(info)+".json" #"C:/Users/admin/Desktop/测试文本/"+char+info+".json"
    # 对json特殊处理（去除特殊符号）
    char_json=char_3+"/"+str(info)+".json"
    write_data = open(char_txt,'a',encoding="gb18030")
    RB_buffer = read_data.read()
    oldlist = ['']
    json_dictory = {}


    oldlist = list(RB_buffer)
    print("长度：")
    
    print(len(oldlist))
    #去除干扰项，保留index所指位置
    index = 0
    """
    while oldlist[index] == " ":
        index += 1
    """
    flag = index

    #print("****************001*******************")

    # 0.取标题
    print("0.取标题:")
    while oldlist[index] != "书":
        index += 1
    tmp = "".join(oldlist[flag:index+1])
    print("----")
    tmp = tmp.replace('\t','')
    tmp = tmp.replace(' ','')
    json_dictory["标题"] = tmp
    

    #print("***************002*******************")

    #去除干扰项，保留index所指位置
    #while oldlist[index] == " ":
    index += 1
    flag = index
    # 取法院，文书标号等
    while oldlist[index] != '号':
        print(oldlist[index])
        index += 1

    #细化分割
    sublist = oldlist[flag:index+1]
    print(sublist)
    index_1 = 0
    flag_1 = 0
    # 1.地区
    print("1.地区:")
    print(index_1)
    print(index_1+1)
    print(index_1)
    #北京，天津，上海， 重庆 内蒙古自治区，新疆维吾尔自治区，西藏自治区，宁夏回族自治区， 广西壮族自治区 香港特别行政区， 澳门特别行政区。
    # 黑龙江省，吉林省，辽宁省，河北省， 山西省， 青海省，山东省，河南省，江苏省，安徽省，浙江省，福建省，江西省，湖南省，湖北省，广东省，台湾省，海南省， 甘肃省，陕西省， 四川省， 贵州省，云南省。 
    while True:  
        #and sublist[index_1] != '上海市' and sublist[index_1] != '天津市'
        if sublist[index_1]+sublist[index_1+1] + sublist[index_1+2] + sublist[index_1+3] != '乌鲁木齐':
            index_1 += 3
            break
        if sublist[index_1]+sublist[index_1+1] +sublist[index_1+2] != '内蒙古' and sublist[index_1]+sublist[index_1+1] + sublist[index_1+2] != '黑龙江':
            index_1 += 2
            break
        if  sublist[index_1]+sublist[index_1+1]!= '北京' and sublist[index_1]+sublist[index_1+1] != '天津' and sublist[index_1]+sublist[index_1+1] != '上海' \
            and sublist[index_1]+sublist[index_1+1] != '重庆' and sublist[index_1]+sublist[index_1+1] != '新疆' and sublist[index_1]+sublist[index_1+1] != '西藏' \
            and sublist[index_1]+sublist[index_1+1] != '宁夏' and sublist[index_1]+sublist[index_1+1] != '广西' and sublist[index_1]+sublist[index_1+1] != '河北' \
            and sublist[index_1]+sublist[index_1+1] != '香港' and sublist[index_1]+sublist[index_1+1] != '澳门' \
            and sublist[index_1]+sublist[index_1+1] != '吉林' and sublist[index_1]+sublist[index_1+1] != '辽宁' \
            and sublist[index_1]+sublist[index_1+1] != '山西' and sublist[index_1]+sublist[index_1+1] != '青海' \
            and sublist[index_1]+sublist[index_1+1] != '山东' and sublist[index_1]+sublist[index_1+1] != '河南' \
            and sublist[index_1]+sublist[index_1+1] != '江苏'  and sublist[index_1]+sublist[index_1+1] != '安徽' \
            and sublist[index_1]+sublist[index_1+1] != '浙江' and sublist[index_1]+sublist[index_1+1] != '江西' \
            and sublist[index_1]+sublist[index_1+1] != '湖南' and sublist[index_1]+sublist[index_1+1] != '湖北' \
            and sublist[index_1]+sublist[index_1+1] != '广东' and sublist[index_1]+sublist[index_1+1] != '台湾' \
            and sublist[index_1]+sublist[index_1+1] != '甘肃' and sublist[index_1]+sublist[index_1+1] != '陕西' \
            and sublist[index_1]+sublist[index_1+1] != '四川' and sublist[index_1]+sublist[index_1+1] != '贵州' \
            and  sublist[index_1]+sublist[index_1+1] != '云南' and sublist[index_1]+sublist[index_1+1] != '兵团':
            index_1 += 2
            break
        if  sublist[index_1] != '治'  and sublist[index_1] != '省':
            index_1 += 1
            break
        if sublist[index_1] != '市' and sublist[index_1] != '县' and sublist[index_1] != '洲' or sublist[index_1] != '区' and sublist[index_1] == '铁' and sublist[index_1] != '旗' and  index_1 < len(sublist)-4:
                index_1 += 1
        # index_1 += 1
        if index_1 >= len(sublist)-4:
            break
    print(index_1)
    tmp_0 = "".join(sublist[flag_1:index_1])
    print(tmp_0)
    tmp_0 = tmp_0.replace('\t','')
    tmp_0 = tmp_0.replace(' ','')
    # 2.案件类型
    print("2.法院:")
    while True:
        index_1 += 1
        # print("index_1:")
        # print(index_1)
        if "".join(sublist[index_1:index_1+2]) in "法院":
            index_1 += 2
            break
        if "".join(sublist[index_1:index_1+2]) in ["民事","刑事","行政","赔偿","执行","刑"]:
            break
        if "".join(sublist[index_1:index_1+3]) in ["民 事","刑 事","行 政","赔 偿","执 行"]:
            break
        
    tmp_1 = "".join(sublist[flag_1:index_1])
    print(tmp_1)
    tmp_1 = tmp_1.replace('\t','')
    tmp_1 = tmp_1.replace(' ','')
    flag_1 = index_1
    # 3.文书类型
    print("3.文书类型：")
    print(len(sublist))
    while True:
        index_1 += 1
        print(index_1)
        if index_1 >= len(sublist) or sublist[index_1] == '（' or sublist[index_1] == '(' or sublist[index_1] == '['  :
            break

    tmp_2 = "".join(sublist[flag_1:index_1])
    print(tmp_2)
    tmp_2 = tmp_2.replace('\t','')
    tmp_2 = tmp_2.replace(' ','')
    flag_1 = index_1
    # 4.年份
    print("4.年份:")
    while True:
        index_1 += 1
        if index_1 >= len(sublist) or sublist[index_1] == '）' or sublist[index_1] == ')' or sublist[index_1] == ']' :
            break
    tmp_3 = "".join(sublist[flag_1+1:index_1])
    print(tmp_3)
    tmp_3 = tmp_3.replace('\t','')
    tmp_3 = tmp_3.replace(' ','')
    tmp_4 = "".join(sublist[flag_1:index+1])
    tmp_4 = tmp_4.replace('\t','')
    tmp_4 = tmp_4.replace(' ','')
    print("--------------------")
    print("地区：")
    print(tmp_0)
    print("法院：")
    print(tmp_1)
    print("文书类型：")
    print(tmp_2)
    print("年份：")
    print(tmp_3)
    print("文书编号：")
    print(tmp_4)
    json_dictory["地区"] = tmp_0
    json_dictory["法院"] = tmp_1
    json_dictory["文书类型"] = tmp_2
    json_dictory["年份"] = tmp_3
    json_dictory["文书编号"] = tmp_4
    
    #tmp = "".join(oldlist[flag:index+1])
    #json_dictory["法院及文书编号"] = tmp

    #print("****************003******************")

    #取涉案人员信息
    flag = index+1
    while True:
        index += 1    
        if ("".join(oldlist[index:index+2])) == "本院":
            break
    tmp = "".join(oldlist[flag:index])
    tmp = tmp.replace('\t','')
    tmp = tmp.replace(' ','')
    json_dictory["涉案人员信息"] = tmp

    #print("****************004******************")

    """
    #正文
    flag = index
    while True:
        index += 1
        if ("".join(oldlist[index:index+2])) == "综上":
            if "综上，本院认定如下事实" in "".join(oldlist[index:index+20]):
                break
    tmp = "".join(oldlist[flag:index])
    write_data.write(tmp)
    write_data.write("\n\n")
    """

    #print("*****************005*****************")

    #取涉案人员到判决依据之间的信息
    flag = index
    while index < len(oldlist):
        index += 1
        #if oldlist[index] == "依":
        if '依据' in "".join(oldlist[index:index+2]) or '依照' in "".join(oldlist[index:index+2]) or '根据' in "".join(oldlist[index:index+2]):
            if "《中华人民共和国" in "".join(oldlist[index:index+30]): 
                if "判决如下" in "".join(oldlist[index:index+100]) or "裁定如下" in "".join(oldlist[index:index+100]):
                    break
    """
    while True:
        index += 1
        if "".join(oldlist[index:index+2]) == '依据' or "".join(oldlist[index:index+2]) == '依照':
            if "《中华人民共和国" in "".join(oldlist[index:index+30]) and ( "判决如下" in "".join(oldlist[index:index+50]) or "裁定如下" in "".join(oldlist[index:index+100])):
                break
    """
    tmp = "".join(oldlist[flag:index])
    tmp = tmp.replace('\t','')
    tmp = tmp.replace(' ','')
    json_dictory["正文"] = tmp

    #print("****************006******************")

    #判决部分（含法律依据）
    flag = index
    label = 0
    while index < len(oldlist):
        index += 1
        if ("".join(oldlist[index:index+3])) == "审判长" or ("".join(oldlist[index:index+3])) == "审判员":
            break
        if ("".join(oldlist[index:index+5])) == "代理审判长" or ("".join(oldlist[index:index+5])) == "代理审判员":
            break
        if ("".join(oldlist[index:index+5])) == "审　判　长":
            break

            """
            elif ("".join(oldlist[index:index+6])) == "代理审判":
                break 
            elif ("".join(oldlist[index:index+6])) == "审　判　":
                break
            """
    tmp = "".join(oldlist[flag:index])
    tmp = tmp.replace('\t','')
    tmp = tmp.replace(' ','')
    json_dictory["判决部分"] = tmp

    #print("*****************007*****************")
    print("判决部分:")
    
    #其他
    flag = index
    print("flag:")
    print(flag)
    while index<len(oldlist):
        index += 1
        if ("".join(oldlist[index:index+1])) == ",":
            print(index)
            print("".join(oldlist[index:index+1]))
            print("break")
            break
    print("index:")
    print(index)
    tmp = "".join(oldlist[flag:index])
    
    # tmp = tmp.replace('\t','')
    # print(tmp)
    #tmp = tmp.replace(' ')
    json_dictory["其他"] = tmp

    print("关键字:")
    flag = index+1
    while index < len(oldlist):
        index += 1
    tmp = "".join(oldlist[flag:index+1])
    print(tmp)
    # tmp = tmp.replace('\t','')
    # print(tmp)
    # tmp = tmp.replace('(','')
    # print("==")
    # print(tmp)
    json_dictory["关键字"] = tmp

    #print(json_dictory)
    json.dump(json_dictory,write_data,ensure_ascii=False)
    
   
    print(info)

    info = info + 1
        #print("*****************008*****************")

    # read_data.close()
    # write_data.close()

  