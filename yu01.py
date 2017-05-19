#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:24:07 2017

@author: chenming
"""


import pymysql   #这里是python3  如果你是python2.x的话，import MySQLdb

host='192.168.0.115'
port=3306
user='root'
passwd='oseasy@0333'
db='crawler'
charset='utf8'

def select_data(sql):
        result = []
        try:
             connect = pymysql.connect(host=host,
                                port=port,
                                user=user,
                                passwd=passwd,
                                db=db,
                                charset='utf8', )
             cursor = connect.cursor()
             cursor.execute(sql)
             alldata = cursor.fetchall()
             # print(alldata)
             for rec in alldata:
                 result.append(rec[2])
        except Exception as e:
             print('Error msg: ' + e)
        finally:
             cursor.close()
             connect.close()
        return result
    
    
    
# 从mysql里取数据 
sql='select * from Table03'
name01=select_data(sql)


# 单个
p1=name01[1].replace('"','')
p2=p1[:0]+'"'+p1[0:]
print(p2)
l=len(p2)
p3=p2[:l]+'"'+p2[l:]
print(p3) #p3=p
import json
json.loads(p3)



# 总体
import json
n=len(name01)
name02=[]
for  i in range(0,n-1):
    name_nbr=name01[i]
    p1=name_nbr.replace('"','')
    p2=p1[:0]+'"'+p1[0:]
    #print(p2)
    l=len(p2)
    p3=p2[:l]+'"'+p2[l:]
    #print(p3) #p3=p
    name02.append(json.loads(p3))
print(name02)

# 查看第二个名字
print(name02[1])
