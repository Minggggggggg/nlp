#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:18:11 2017

@author: chenming
"""

from collections import defaultdict
import os
import re
import jieba
import codecs


"""
1. 文本切割
"""

def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = jieba.cut(sentence)
    segResult = []
    for w in segList:
        segResult.append(w)
    # 读取停用词
    f = open("/Users/chenming/Spyder/dict/stopwords/zh.txt",encoding='utf8')
    lines = f.readlines()#读取全部内容   
    stopwords=[]
    for line in lines  :
        line = line.strip('\n')  
        stopwords.append(line) 
    #return None
    newSent = []
    for word in segResult:
        if word in stopwords:
            # print "stopword: %s" % word
            continue
        else:
            newSent.append(word)

    return newSent
#

# 测试 sent2word：OK
sentence='知识图是一种新的知识表示方法.本文从本体论的角度出发,将知识图的本体论分别与Aristotle、Kant和Peirce的三种知识表示的本体论进行了比较,表明知识图方法的有效性以及本原性,说明知识图是一种更为一般的知识表示方法.从知识图本体论的观点,研究了各类逻辑词的知识图表示.本文结合汉语的特点,从结构的角度,研究并揭示了逻辑词的共性和规律性.进一步阐明知识图"结构就是含义"的思想.逻辑词的知识图分析将为自然语言分析中词典的建立奠定基础.'
jieba.add_word('知识图')
sent2word(sentence)
#  



"""
2. 情感定位
"""
def classifyWords(wordDict):
    # (1) 情感词
    senList = readlines('BosonNLP_sentiment_score.txt')
    senDict = defaultdict()
    for s in senList:
        senDict[s.split(' ')[0]] = s.split(' ')[1]
    # (2) 否定词
    notList = readlines("/Users/chenming/Spyder/dict/stopwords/zh.txt",encoding='utf8')
    # (3) 程度副词
    degreeList = readlines("/Users/chenming/Spyder/dict/sentiments/degreedDICT.txt",encoding='utf8')
    degreeDict = defaultdict()
    for d in degreeList:
        degreeDict[d.split(',')[0]] = d.split(',')[1]

    senWord = defaultdict()
    notWord = defaultdict()
    degreeWord = defaultdict()

    for word in wordDict.keys():
        if word in senDict.keys() and word not in notList and word not in degreeDict.keys():
            senWord[wordDict[word]] = senDict[word]
        elif word in notList and word not in degreeDict.keys():
            notWord[wordDict[word]] = -1
        elif word in degreeDict.keys():
            degreeWord[wordDict[word]] = degreeDict[word]
    return senWord, notWord, degreeWord


    senList = readlines('BosonNLP_sentiment_score.txt')
    senDict = defaultdict()
    for s in senList:
        senDict[s.split(' ')[0]] = s.split(' ')[1]
    f = open("/Users/chenming/Spyder/dict/sentiments/.txt",encoding='utf8')
    lines = f.readlines()#读取全部内容   


