#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:24:30 2017

@author: chenming
"""

import numpy as np


#------------------------------------------------
# 1. Load dictionary and dataset

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

# Load dataset
#review = tp.get_excel_data("D:/code/review_set.xlxs", "1", "1", "data")
sentence='知识图是一种新的知识表示方法.本文从本体论的角度出发,将知识图的本体论分别与Aristotle、Kant和Peirce的三种知识表示的本体论进行了比较,表明知识图方法的有效性以及本原性,说明知识图是一种更为一般的知识表示方法.从知识图本体论的观点,研究了各类逻辑词的知识图表示.本文结合汉语的特点,从结构的角度,研究并揭示了逻辑词的共性和规律性.进一步阐明知识图"结构就是含义"的思想.逻辑词的知识图分析将为自然语言分析中词典的建立奠定基础.'


# 2. Sentiment dictionary analysis basic function
# Function of matching adverbs of degree and set weights
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

# 测试 OK
word='较为'
sentiment_value = 10
match(word, sentiment_value)
#
word='不丁点儿'
sentiment_value = 10
match(word, sentiment_value) 
#
word='备至'
sentiment_value = 10
match(word,sentiment_value) 
#----------------------------




# Function of transforming negative score to positive score
# Example: [5, -2] →  [7, 0]; [-4, 8] →  [0, 12]
def transform_to_positive_num(poscount, negcount):
    pos_count = 0
    neg_count = 0
    if poscount < 0 and negcount >= 0:
        neg_count += negcount - poscount
        pos_count = 0
    elif negcount < 0 and poscount >= 0:
        pos_count = poscount - negcount
        neg_count = 0
    elif poscount < 0 and negcount < 0:
        neg_count = -poscount
        pos_count = -negcount
    else:
        pos_count = poscount
        neg_count = negcount
    return [pos_count, neg_count]    
    
    
   
    
# 3.1 Single review's positive and negative score
# Function of calculating review's every sentence sentiment score
def sumup_sentence_sentiment_score(score_list):
	score_array = np.array(score_list) # Change list to a numpy array
	Pos = np.sum(score_array[:,0]) # Compute positive score
	Neg = np.sum(score_array[:,1])
	AvgPos = np.mean(score_array[:,0]) # Compute review positive average score, average score = score/sentence number
	AvgNeg = np.mean(score_array[:,1])
	StdPos = np.std(score_array[:,0]) # Compute review positive standard deviation score
	StdNeg = np.std(score_array[:,1])
    return [Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg] 
    
    
def single_review_sentiment_score(review):
	single_review_senti_score = []
	cuted_review = tp.cut_sentence_2(review)

	for sent in cuted_review:
		seg_sent = tp.segmentation(sent, 'list')
		i = 0 # word position counter
		s = 0 # sentiment word position
		poscount = 0 # count a positive word
		negcount = 0 # count a negative word

		for word in seg_sent:
		    if word in posdict:
		        poscount += 1
		        for w in seg_sent[s:i]:
		           poscount = match(w, poscount)
		        a = i + 1

		    elif word in negdict:
		        negcount += 1
		        for w in seg_sent[s:i]:
		        	negcount = match(w, negcount)
		        a = i + 1

		    # Match "!" in the review, every "!" has a weight of +2
		    elif word == "！".decode('utf8') or word == "!".decode('utf8'):
		        for w2 in seg_sent[::-1]:
		            if w2 in posdict:
		            	poscount += 2
		            	break
		            elif w2 in negdict:
		                negcount += 2
		                break                    
		    i += 1

		single_review_senti_score.append(transform_to_positive_num(poscount, negcount))
		review_sentiment_score = sumup_sentence_sentiment_score(single_review_senti_score)

	return review_sentiment_score

# Testing
print single_review_sentiment_score(review[0])
   
    
    
    