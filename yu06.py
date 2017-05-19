#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:38:13 2017

@author: chenming
"""


from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import SementicRoleLabeller
from pyltp import NamedEntityRecognizer
from pyltp import Parser

#分词
def segmentor(sentence):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('/Users/chenming/Spyder/3.3.1/ltp_data/cws.model')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    #默认可以这样输出
    print ('\t'.join(words))
    # 可以转换成List 输出
    words_list = list(words)
    segmentor.release()  # 释放模型
    return words_list

def posttagger(words):
    postagger = Postagger() # 初始化实例
    postagger.load('/Users/chenming/Spyder/3.3.1/ltp_data/pos.model')  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    for word,tag in zip(words,postags):
        print (word+'/'+tag)
    postagger.release()  # 释放模型
    return postags

#分句，也就是将一片文本分割为独立的句子
def sentence_splitter(sentence):
    sents = SentenceSplitter.split(sentence)  # 分句
    print ('\n'.join(sents))


#命名实体识别
def ner(words, postags):
    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load('/Users/chenming/Spyder/3.3.1/ltp_data/ner.model')  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    for word, ntag in zip(words, netags):
        print (word + '/' + ntag)
    recognizer.release()  # 释放模型
    return netags

#依存语义分析
def parse(words, postags):
    parser = Parser() # 初始化实例
    parser.load('/Users/chenming/Spyder/3.3.1/ltp_data/parser.model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    print ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()  # 释放模型
    return arcs

#角色标注
def role_label(words, postags, netags, arcs):
    labeller = SementicRoleLabeller() # 初始化实例
    labeller.load('/Users/chenming/Spyder/3.3.1/ltp_data/srl/')  # 加载模型
    roles = labeller.label(words, postags, netags, arcs)  # 语义角色标注
    for role in roles:
        print (role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
    labeller.release()  # 释放模型
    
    
sentence='你好，你觉得这个例子从哪里来的？是我修改了别人的，再加以完善后得到的。我的微博是Minggggggggg，转载请注明来自Minggggggggg！'
#测试分句子
print('******************测试将会顺序执行：**********************')
sentence_splitter(sentence)
print('###############以上为分句子测试###############')

#测试分词
words = segmentor(sentence)
print('###############以上为分词测试###############')

#测试标注
tags = posttagger(words)
print('###############以上为词性标注测试###############')

#命名实体识别
netags = ner(words,tags)
print('###############以上为命名实体识别测试###############')

#依存句法识别
arcs = parse(words,tags)
print('###############以上为依存句法测试###############')

#角色标注
roles = role_label(words,tags,netags,arcs)
print('###############以上为角色标注测试###############')




#---------- jieba使用 -----------

# jieba 入门
import jieba
#全模式
text = "我来到北京清华大学"
seg_list = jieba.cut(text, cut_all=True)
print (u"[全模式]: ", "/ ".join(seg_list) )
#精确模式
seg_list = jieba.cut(text, cut_all=False)
print (u"[精确模式]: ", "/ ".join(seg_list))
#默认是精确模式
seg_list = jieba.cut(text)
print (u"[默认模式]: ", "/ ".join(seg_list) )
#新词识别 “杭研”并没有在词典中,但是也被Viterbi算法识别出来了
seg_list = jieba.cut("他来到了网易杭研大厦") 
print (u"[新词识别]: ", "/ ".join(seg_list))
#搜索引擎模式
seg_list = jieba.cut_for_search(text) 
seg_list[2]
print (u"[搜索引擎模式]: ", "/ ".join(seg_list))



# jieba 添加自定义词典
import jieba
#导入自定义词典
jieba.load_userdict("/Users/chenming/Spyder/yu/dict.txt")
jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
#全模式
text = "故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等"
seg_list = jieba.cut(text, cut_all=True)
#精确模式
seg_list = jieba.cut(text, cut_all=False)
print (u"[精确模式]: ", "/ ".join(seg_list))
#搜索引擎模式
seg_list = jieba.cut_for_search(text) 
print (u"[搜索引擎模式]: ", "/ ".join(seg_list))

# list
seg_list =jieba.lcut(text, cut_all=False)
# list
jieba.lcut_for_search(text, cut_all=False) 


# jieba 关键词提取
import jieba
import jieba.analyse
#导入自定义词典
jieba.load_userdict("/Users/chenming/Spyder/yu/dict.txt")
#精确模式
text = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门，午门居中向阳。"
seg_list = jieba.cut(text, cut_all=False)
print (u"分词结果:")
print ("/".join(seg_list))
#获取关键词
tags = jieba.analyse.extract_tags(text, topK=3, withWeight=False, allowPOS=())
print (u"关键词:")
print (" ".join(tags))




# Tokenize：返回词语在原文的起止位置
result = jieba.tokenize(u'永和服装饰品有限公司')
for tk in result:
    print("word %s  \t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
# 搜索模式
result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))




#-------------------  完整  ---------------------
import jieba
text = "故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等"
seg_list =jieba.lcut(text, cut_all=False)

