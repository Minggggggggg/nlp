#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:17:39 2017
/Users/chenming/anaconda/lib/python3.6/site-packages/nltk/downloader.py", line 974, in _interactive_download
@author: chenming
"""



import numpy as np
import pandas as pd
import nltk

import re
import os
import codecs
from sklearn import feature_extraction
import mpld3

from nltk import corpus
from nltk.corpus import stopwords




#----- 读取片名 -----
f = open("/Users/chenming/Spyder/yu/title01.txt","r")
lines = f.readlines()#读取全部内容  
titles=[]
for line in lines  :
    line = line.strip('\n')  
    titles.append(line),
    print (line ) 

print (titles[:10] )#前 10 个片名
#----------


#nltk.download()
#载入 nltk 的英文停用词作为“stopwords”变量
import nltk
stopwords = nltk.corpus.stopwords.words('english')
print (stopwords[:10])
#
from nltk.corpus import sinica_treebank
print(sinica_treebank.words())


import nltk
stopwords = nltk.corpus.stopwords.words('english')
print (stopwords[:10])


#-------  snownlp ---------
import snownlp
from snownlp import SnowNLP
s=SnowLP('这东西真心很赞')














import os  # 为了使用 os.path.basename 函数
 
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from sklearn.manifold import MDS
 
MDS()
 
# 将二位平面中绘制的点转化成两个元素（components）
# 设置为“precomputed”是因为我们提供的是距离矩阵
# 我们可以将“random_state”具体化来达到重复绘图的目的
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
 
pos = mds.fit_transform(dist)  # 形如 (n_components, n_samples)
 
xs, ys = pos[:, 0], pos[:, 1]





#-------- 可视化文档聚类 ---------
# 用字典设置每个聚类的颜色
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}
 
# 用字典设置每个聚类名称
cluster_names = {0: 'Family, home, war', 
                 1: 'Police, killed, murders', 
                 2: 'Father, New York, brothers', 
                 3: 'Dance, singing, love', 
                 4: 'Killed, soldiers, captain'}


# 在 ipython 中内联（inline）演示 matplotlib 绘图
%matplotlib inline 
 
 
# 用 MDS 后的结果加上聚类编号和绘色创建 DataFrame
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=titles)) 
 
# 聚类归类
groups = df.groupby('label')
 
 
# 设置绘图
fig, ax = plt.subplots(figsize=(17, 9)) # 设置大小
ax.margins(0.05) # 可选项，只添加 5% 的填充（padding）来自动缩放（auto scaling）。
 
# 对聚类进行迭代并分布在绘图上
# 我用到了 cluster_name 和 cluster_color 字典的“name”项，这样会返回相应的 color 和 label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
            label=cluster_names[name], color=cluster_colors[name], 
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params(
        axis= 'x',          # 使用 x 坐标轴
        which='both',      # 同时使用主刻度标签（major ticks）和次刻度标签（minor ticks）
        bottom='off',      # 取消底部边缘（bottom edge）标签
        top='off',         # 取消顶部边缘（top edge）标签
        labelbottom='off')
    ax.tick_params(
        axis= 'y',         # 使用 y 坐标轴
        which='both',      # 同时使用主刻度标签（major ticks）和次刻度标签（minor ticks）
        left='off',      # 取消底部边缘（bottom edge）标签
        top='off',         # 取消顶部边缘（top edge）标签
        labelleft='off')
 
ax.legend(numpoints=1)  # 图例（legend）中每项只显示一个点
 
# 在坐标点为 x,y 处添加影片名作为标签（label）
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)  
 
 
 
plt.show() # 展示绘图
 
# 以下注释语句可以保存需要的绘图
#plt.savefig('clusters_small_noaxes.png', dpi=200)