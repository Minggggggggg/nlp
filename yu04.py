#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:47:21 2017

@author: chenming
"""

#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("/Users/chenming/Spyder/yu/dict.txt")
import jieba.posseg as pseg

jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
jieba.del_word('自定义词')

test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print('/'.join(words))

print("="*40)

result = pseg.cut(test_sent)

for w in result:
    print(w.word, "/", w.flag, ", ", end=' ')

print("\n" + "="*40)

# cut 例子
terms = jieba.cut('easy_install is great')
print('/'.join(terms))
terms = jieba.cut('python 的正则表达式是好用的')
print('/'.join(terms))

print("="*40)
# test frequency tune
testlist = [
('今天天气不错', ('今天', '天气')),
('如果放到post中将出错。', ('中', '将')),
('我们中出了一个叛徒', ('中', '出')),
]

for sent, seg in testlist:
    print('/'.join(jieba.cut(sent, HMM=False)))
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print('/'.join(jieba.cut(sent, HMM=False)))
    print("-"*40)
    
   
    
    
##
import pynlpir  
import codecs  
import math  
  
pynlpir.open()  
  
#文本分词  
typelist = [u"财经",u"IT",u"健康",u"体育",u"旅游",u"教育",u"招聘",u"文化",u"军事"]  
  
typetxt = codecs.open('C:\\Users\\Administrator\\Desktop\\txttype.txt', 'a', encoding='utf-8')  
wordseg_result = codecs.open('C:\\Users\\Administrator\\Desktop\\wordseg_result.txt', 'a',encoding='utf-8')  
    
#过滤停用词  
stopwords = []  
delstopwords_alltxt = []  
  
st = codecs.open('/Users/chenming/Spyder/yu/dict.txt')  
delstopwords_result = codecs.open('/Users/chenming/Spyder/yu/dict.txt , 'a',encoding='utf-8')  
  
for line in st:  
    line = line.strip()  
    stopwords.append(line) 
    
    
    
    
    