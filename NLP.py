#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:00:38 2017

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
        if word in stopwords and word not in notList and word not in degreeList and word not in senDict:
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




"""
2. 情感定位
"""
def classifyWords(wordDict):
    # (1) 情感词
    f = open("/Users/chenming/Spyder/dict/Boson/BosonNLP_sentiment_score.txt",encoding='utf-8')
    lines = f.readlines()#读取全部内容   
    senList=[]
    for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        senList.append(line) 
    # senDict文本部分
    senDict=[]
    for s in senList:
        #senDict[s.split(' ')[0]] = s.split(' ')[1]
        #senDict.append(s.split(' ')[:1]) 
        a=s.split(' ')
        b=a[0]
        senDict.append(b) 
    # senDict数字部分
    senDict02=[]
    for s in senList:
        a=s.split(' ')
        c=a[-1]
        senDict02.append(c) 

    # (2) 否定词
    f = open("/Users/chenming/Spyder/dict/Boson/notDICT.txt",encoding='utf-8')
    lines = f.readlines()#读取全部内容   
    notList=[]
    for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        notList.append(line) 
    
    # (3) 程度副词
    f = open("/Users/chenming/Spyder/dict/Boson/degreeDICT.txt",encoding='utf-8')
    lines = f.readlines()#读取全部内容   
    degreeList=[]
    for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        degreeList.append(line) 
    #   
    degreeDict = degreeList
    #
    senWord = []
    notWord = []
    degreeWord = []

    for word in wordDict:
        if word in senDict and word not in notList and word not in degreeDict:
            senWord.append(word)
        elif word in notList and word not in degreeDict:
            notWord.append(-1)
        elif word in degreeDict:
            degreeWord.append(word)
    return senWord, notWord, degreeWord



# 测试 OK
newsent=sent2word(sentence)
[senWord, notWord, degreeWord]=classifyWords(newsent)




f = open("/Users/chenming/Spyder/dict/Boson/BosonNLP_sentiment_score.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
senList=[]
for line in lines  :
        line=line.strip('\n')
        line=line.strip(',')    
        senList.append(line) 
    # senDict文本部分
senDict=[]
for s in senList:
        #senDict[s.split(' ')[0]] = s.split(' ')[1]
        #senDict.append(s.split(' ')[:1]) 
        a=s.split(' ')
        b=a[0]
        senDict.append(b) 
    # senDict数字部分
senDict02=[]
for s in senList:
        a=s.split(' ')
        c=a[-1]
        senDict02.append(c) 

"""
3. 情感聚合
"""
# Load sentiment dictionary: positive, negative
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
    
    
# Load adverbs of degree dictionary
# most
f = open("/Users/chenming/Spyder/dict/sentiments/degree/most.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
most=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    most.append(line)
# very
f = open("/Users/chenming/Spyder/dict/sentiments/degree/very.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
very=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    very.append(line)
# more
f = open("/Users/chenming/Spyder/dict/sentiments/degree/more.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
more=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    more.append(line)
# ish
f = open("/Users/chenming/Spyder/dict/sentiments/degree/ish.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
ish=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    ish.append(line)
# insufficiently
f = open("/Users/chenming/Spyder/dict/sentiments/degree/insufficiently.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
insufficiently=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    insufficiently.append(line)
# inverse
f = open("/Users/chenming/Spyder/dict/sentiments/degree/inverse.txt",encoding='utf-8')
lines = f.readlines()#读取全部内容   
inverse=[]
for line in lines  :
    line=line.strip('\n')
    line=line.strip(',')    
    inverse.append(line)
    
    
def match(word, sentiment_value):
	if word in most:
		sentiment_value *= 2.0
	elif word in very:
	    sentiment_value *= 1.5
	elif word in more:
	    sentiment_value *= 1.25
	elif word in ish:
	    sentiment_value *= 0.5
	elif word in insufficiently:
	    sentiment_value *= 0.25
	elif word in inverse:
	    sentiment_value *= -1
	return sentiment_value

# function
def scoreSent(senWord, notWord, degreeWord, segResult):
    W = 1
    score = 0
    # 存所有情感词的位置的列表
    senloc = -1
    point_total=[]
    # notloc = -1
    # degreeloc = -1
    # 遍历句中所有单词segResult，i为单词绝对位置
    for mot in segResult:
        
        # 如果该词为情感词
        if mot in senWord:
            # loc为情感词位置列表的序号
            senloc += 1
            # 直接添加该情感词分数
            ind01=senDict.index(mot)
            point=float(senDict02[ind01])
            score += W * point
            print(point)
            # print "score = %f" % score
            if senloc < len(senWord) - 1:
                # 判断该情感词与下一情感词之间是否有否定词或程度副词
                # j为绝对位置
                ind = senWord.index(mot)
                word1=senWord[ind]
                word2=senWord[ind+1]
                ind1=segResult.index(word1)
                ind2=segResult.index(word2)
                for j in range(ind1, ind2):
                    # 如果有否定词
                    if segResult[j] in notWord:
                        W *= -1
                    # 如果有程度副词
                    elif segResult[j] in degreeWord:
                        point_sen=float(match(senWord[j], 1))
                        print(point_sen)
                        W *= point_sen
            point_total.append(score)
        # i定位至下一个情感词
        #if senloc < len(senWord) - 1:
        #    mot = senWord[senloc + 1]
    return point_total

# 测试 OK
sentence='我非常不喜欢你,但是我和喜欢他。'
[newsent,segResult]=sent2word(sentence)
[senWord, notWord, degreeWord]=classifyWords(newsent)
scoreSent(senWord, notWord, degreeWord, segResult)


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

point(s1) #-1
point(s2) #1
point(s3) #2
point(s4) #3
point(s5) #5
point(s6) #2

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

#
dd=''