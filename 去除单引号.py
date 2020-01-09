import jieba
from collections import Counter
import json
import matplotlib.pyplot as plt
import jieba.analyse as analyse
from wordcloud import WordCloud
from scipy.misc import imread
from os import path
import jieba.posseg as pseg
import re

#记录文件中有多少行标题 记录在count中

num=2
for k in range(4999):
    count=0
    string = r"E:\毕设项目\5000"
    string_txt = string+"/"+str(num)+".txt"
    r=open(string_txt,'r',encoding="utf-8").read()
    
    char=r"E:\毕设项目\txt文本"
    char_txt=char+"/"+str(num)+".txt"
    h=r.replace("'","")
    
    
    
    
    #r = "\'"      
    m=open(char_txt,'w',encoding='utf-8')
    m.write(str(h))
    # print(word_list)
    m.close()

    
    #分词

    
    num+=1
