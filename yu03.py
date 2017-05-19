#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:42:09 2017

@author: chenming
"""

import jieba
import jieba.posseg as pseg
print ("加载用户词典...")

jieba.load_userdict('')
jieba.load_userdict('')


# 查看python默认编码
import sys
print(sys.stdout.encoding)



# 分词，返回List
def segmentation(sentence):
    seg_list = jieba.cut(sentence)
    seg_result = []
    for w in seg_list:
        seg_result.append(w)
    #print seg_result[:]
    return  seg_result


# 例子
sentence = '黄鹤楼没有岳阳楼好看，因为岳阳楼看上去更加壮观。'
seg_result = segmentation(sentence)
print(seg_result)
for w in seg_result:
    print (w)
print ('\n')
jieba.add_word('更加壮观')


# 分词，词性标注，词和词性构成一个元组
def postagger(sentence):
    pos_data = pseg.cut(sentence)
    pos_list = []
    for w in pos_data:
        pos_list.append((w.word, w.flag))
    #print pos_list[:]
    return pos_list

# 例子
postagger(sentence)


# 句子切分
def cut_sentence(words):
    #words = words.decode('utf8')
    start = 0
    i = 0
    token = 'meaningless'
    sents = []
    #punt_list = ',.!?;~，。！？；～… '.decode('utf8')
    punt_list = ',.!?;~，。！？；～… '
    #print "punc_list", punt_list
    for word in words:
        #print "word", word
        if word not in punt_list:   # 如果不是标点符号
            #print "word1", word
            i += 1
            token = list(words[start:i+2]).pop()
            #print "token:", token
        elif word in punt_list and token in punt_list:  # 处理省略号
            #print "word2", word
            i += 1
            token = list(words[start:i+2]).pop()
            #print "token:", token
        else:
            #print "word3", word
            sents.append(words[start:i+1])   # 断句
            start = i + 1
            i += 1
    if start < len(words):   # 处理最后的部分
        sents.append(words[start:])
    return sents
# 备注：
#  a = 'Happy New Year' # Python 3
#  b = unicode('Happy New Year') # Python 2
#  the code before are same. So I think you should remove the .decode('utf-8'). 
#  Because you have already get the unicode object.


# #-*-coding:utf-8-*- 
s='中文'
print (type(s)) #查看s的字符类型
print (s)  
s.decode('utf8') #解码utf8，默认的编码方式是unicode
s.decode('gbk', "ignore") #解码utf8，忽略其中有异常的编码，仅显示有效的编码
s.decode('gbk', 'replace')
print (type(s))
print (s)

# 例子
test_sentence2 = "这款手机大小合适，配置也还可以，很好用，只是屏幕有点小。。。总之，戴妃+是一款值得购买的智能手机。"
cut_sentence(test_sentence2) 


###？？？
def read_lines(filename):
    fp = open(filename, 'r')
    lines = []
    for line in fp.readlines():
        line = line.strip()
        line = line.decode("utf-8")
        lines.append(line)
    fp.close()
    return lines

# 例子
file="/Users/chenming/Spyder/yu/dict.txt"
read_lines(file)







# 去除停用词
def del_stopwords(seg_sent):
    stopwords = read_lines("/Users/chenming/Spyder/yu/fenci.txt")  # 读取停用词表
    new_sent = []   # 去除停用词后的句子
    for word in seg_sent:
        if word in stopwords:
            continue
        else:
            new_sent.append(word)
    return new_sent


