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
import json
from io import BytesIO
import pymysql
import random
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
from scipy.misc import imread
import jieba.analyse as analyse
from wordcloud import WordCloud
import numpy as np
import matplotlib.image as img
import time
from pyecharts import Map, Geo
import os
import logging
logging.basicConfig(filename='log_examp.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
pymysql.install_as_MySQLdb()
#连接数据库
db=pymysql.connect(host='localhost',
                        user='root',
                        port=3306,
                        password='520000ww',
                        db='legalbook',
                        charset='utf8')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data) # 结果表明已经连接成功      

num = 0
data2 = 'E:/毕设项目/结果2/'
#从文本文件中提取json数据
for info in range(4990):
    # domain = os.path.abspath("E:/毕设项目/文本处理最终结果/")
    # file_string = os.path.join(domain,info)
    print('...............')
    file_string = data2+"/"+str(num)+".json"
    print(file_string)
    read_data = open(file_string,'r',encoding="gb18030").read()
    if read_data=="":
        num+=1
        print(" read_data is empty")
    else:
        #if RB.startswith(u'\ufeff'):
        #RB = RB.encode('ANSI')[3:].decode('ANSI')
        RB_json = json.loads(read_data)         #RB_json为字典
        # print(type(RB_json["标题"]))
        # print(RB_json["标题"],en)
        #print(read_data)
        
        result = (num,RB_json["标题"],RB_json["地区"],RB_json["法院"],RB_json["文书类型"],RB_json["年份"],RB_json["文书编号"],RB_json["涉案人员信息"],RB_json["正文"],RB_json["判决部分"],RB_json["其他"],RB_json["关键字"])
        # inesrt_re = "insert into new_table1(ID,标题,地区,法院,文书类型,年份,文书编号,涉案人员信息,正文,判决部分,其他,关键字) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%result
        inesrt_re = "insert into legal_instrument(ID,title,region,court,document_Type,year,document_number,information_people,text_part,referee_part,other,keyword) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%result
        cursor.execute(inesrt_re)
        db.commit()
        print("success")
        num = num + 1
cursor.close()
db.close()