#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:31:45 2017

@author: chenming
"""

import jieba

"""
1. 文本切割
"""

def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    jieba.add_word('喜不')
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
    # 读取否定词
    f = open("/Users/chenming/Spyder/dict/Boson/notDICT.txt",encoding='utf-8')
    lines = f.readlines()#读取全部内容   
    notList=[]
    for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        notList.append(line) 
    # 读取程度副词
    f = open("/Users/chenming/Spyder/dict/Boson/degreeDICT.txt",encoding='utf-8')
    lines = f.readlines()#读取全部内容   
    degreeList=[]
    for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        degreeList.append(line) 
    # 读取情感词
    f = open("/Users/chenming/Spyder/dict/Boson/BosonNLP_sentiment_score.txt",encoding='utf-8')
    lines = f.readlines()#读取全部内容   
    senList=[]
    for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        senList.append(line) 
    #
    senDict=[]
    for s in senList:
        #senDict[s.split(' ')[0]] = s.split(' ')[1]
        #senDict.append(s.split(' ')[:1]) 
        a=s.split(' ')
        b=a[0]
        senDict.append(b) 
    #######   
    #return None
    newsent = []
    for word in segResult:
        if word in stopwords and word not in notList and word not in degreeList :
            # print "stopword: %s" % word
            continue
        else:
            newsent.append(word)
    return newsent,segResult
#

# 测试 sent2word：OK
#sentence='知识图是一种新的知识表示方法.本文从本体论的角度出发,将知识图的本体论分别与Aristotle、Kant和Peirce的三种知识表示的本体论进行了比较,表明知识图方法的有效性以及本原性,说明知识图是一种更为一般的知识表示方法.从知识图本体论的观点,研究了各类逻辑词的知识图表示.本文结合汉语的特点,从结构的角度,研究并揭示了逻辑词的共性和规律性.进一步阐明知识图"结构就是含义"的思想.逻辑词的知识图分析将为自然语言分析中词典的建立奠定基础.最尼玛真无语不好看.百分之百好看.'
sentence='我爱武汉，但是我极其不喜欢武汉的天气。'
jieba.add_word('武汉的天气')
[newsent,segResult]=sent2word(sentence)
#  




#----------------  编写diy
f = open("/Users/chenming/Spyder/dict/sentiments/sent/sent_pos.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
sent_pos=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    sent_pos.append(line) 
# negdict
f = open("/Users/chenming/Spyder/dict/sentiments/sent/sent_neg.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
sent_neg=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    sent_neg.append(line)
# 否定词
f = open("/Users/chenming/Spyder/dict/Boson/notDICT.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
notDICT=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    notDICT.append(line)
# posdict
f = open("/Users/chenming/Spyder/dict/sentiments/neg_pos/posdict.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
posdict=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    posdict.append(line) 
# negdict
f = open("/Users/chenming/Spyder/dict/sentiments/neg_pos/negdict.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
negdict=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    negdict.append(line) 
#    
f = open("/Users/chenming/Spyder/dict/Boson/degreeDICT.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
degreeDICT=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    degreeDICT.append(line)             



#-----------------------------------------  
def point(sentence)  :   
 score=0
 ind=0
 scores=[]
 point_total=0
 [newsent,segResult]=sent2word(sentence)
 for mot in segResult:    
    if mot in posdict or mot in sent_pos:
        p=1
        ind=segResult.index(mot)
        print(mot)
        if  segResult[ind-1] in notDICT:
            q=-1
            score = p*q
        elif segResult[ind-1] not in notDICT:
            q=1
            score = p*q
        print(score)
        scores.append(score)
    elif mot  in negdict or mot in sent_neg:
        p=-1
        ind=segResult.index(mot)
        print(mot)
        if  segResult[ind-1] in notDICT:
            q=-1
            score = p*q
        elif segResult[ind-1] not in notDICT:
            q=1
            score = p*q
        print(score)
        scores.append(score)
 point_total=sum(scores)
 return(point_total)

# 测试
sentence='我非常不喜欢你,但是我很喜欢他，我很讨厌他的一个朋友，我现在不得不出去。'
point(sentence) 
        
s1='我非常不喜欢你,但是我很喜欢他，我很讨厌他的一个朋友，我现在不得不出去。'
s2='人巨多，排队上，排队下，一直在排队。但是貌似这个是经典的代表，还必须去，门票也不便宜，老外都排队上呢，咱中国人还是上去看看比较好。沙盘里展了各个时期黄鹤楼的模型，看来名气大的不是一点'
s3='夜景很美，也很壮观，欲穷千里目更上一层楼！'
s4='黄鹤楼虽然不是古建筑，是在原址复建的，但是凭借着名望还是招揽的八方游客，值得一看，特别是站在桥上看长江大桥，很是壮美，就是小长假时候容易堵人。。。。塞得慢慢的'
s5='眼前就是此行必打卡的地方——黄鹤楼。以前小时候喜欢被景点类的“三大楼”、“四大山”，到现在也忘记地差不多了。不过黄鹤楼肯定是其中之一。楼本身没有什么特别的地方，主要是集聚在它身上的各种传说，以及文人墨客在这里留下的各种轶事。'
s6='没去过黄鹤楼就等于没去过武汉。在黄鹤楼顶可以鸟瞰武汉长江大桥。虽然黄鹤楼是上世纪80年代修复的（因为由于战乱，本尊多次烧毁），但是并不影响它在游人心中的地位。80元的门票略贵。'
#
point(s1) #-3
point(s2) #-1
point(s3) #2
point(s4) #3
point(s5) #1
point(s6) #0
#
s7='我也不知道我喜不喜欢黄鹤楼。'
jieba.add_word('喜不')
jieba.load_userdict("/Users/chenming/Spyder/nlp/dict.txt")
[newsent,segResult]=sent2word(s7)
point(s7)

sentence='我爱武汉，但是我极其不喜欢武汉的天气。'
jieba.add_word('极其')
[newsent,segResult]=sent2word(sentence)
point(sentence)

s8='我不确定我是否喜欢黄鹤楼。'
point(s8)


s9='人太多了，天气又热，后悔来这里。'
[newsent,segResult]=sent2word(s9)
point(s9)

s10='真他妈的热，再也不想来了。'
[newsent,segResult]=sent2word(s10)
point(s10)


s11='什么垃圾地方，又脏又乱。'
[newsent,segResult]=sent2word(s11)
point(s11)

