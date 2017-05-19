#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:12:40 2017

@author: chenming
"""



  

# -*- coding: utf-8 -*-
from pyltp import SentenceSplitter
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
print ('\n'.join(sents))




#分词
# -*- coding: utf-8 -*-
from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load('/Users/chenming/Spyder/3.3.1/ltp_data/cws.model')  # 加载模型
words = segmentor.segment('元芳你怎么看')  # 分词
print ('\n'.join(words))
segmentor.release()  # 释放模型



#使用分词外部词典
# -*- coding: utf-8 -*-
from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon('/Users/chenming/Spyder/3.3.1/ltp_data/cws.model', '/Users/chenming/Spyder/3.3.1/ltp_data/lexicon.txt') # 加载模型
words = segmentor.segment('亚硝酸盐是一种化学物质')
print ('\t'.join(words))
segmentor.release()



#使用个性化分词模型
# -*- coding: utf-8 -*-
from pyltp import CustomizedSegmentor
customized_segmentor = CustomizedSegmentor()  # 初始化实例
customized_segmentor.load_with_lexicon('/Users/chenming/Spyder/3.3.1/ltp_data/cws.model', '/Users/chenming/Spyder/3.3.1/ltp_data/customized_model','/Users/chenming/Spyder/3.3.1/ltp_data/lexicon.txt') # 加载模型
words = customized_segmentor.segment('亚硝酸盐是一种化学物质')
print ('\t'.join(words))
customized_segmentor.release()






# -*- coding: utf-8 -*-
from pyltp import Segmentor
#分词
def segmentor(sentence):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('/Users/chenming/Spyder/3.3.1/ltp_data/cws.model')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    #默认可以这样输出
    # print '\t'.join(words)
    # 可以转换成List 输出
    words_list = list(words)
    for word in words_list:
        print (word)
    segmentor.release()  # 释放模型
    #return words_list
    
    
#测试分词
sentence='你好，你觉得这个例子从哪里来的？当然还是直接复制官方文档，然后改了下这里得到的。我的微博是MebiuW，转载请注明来自MebiuW！'
ok = segmentor(sentence)







