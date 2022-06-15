'''
Description: 
Author: baiyi
Date: 2022-01-26 13:26:39
LastEditTime: 2022-02-11 11:31:28
LastEditors: baiyi
Reference: 
'''
from flask import jsonify,render_template,Blueprint
from .utils import get_now,sql_query

bp=Blueprint("dashboard",__name__)

@bp.route('/getTime')
def get_time():
    """获取当前时间"""
    now=get_now()
    return jsonify(now)

@bp.route('/getLabel')
def get_label():
    """获取指标卡数据"""
    res=sql_query("select  column1,column2,column3,column4 from num")
    data=res[0]
    return jsonify({"label1":data[0],"label2":data[1],"label3":data[2],"label4":data[3]})

@bp.route('/getL1')
def get_l1():
    """获取折线图数据"""
    res=sql_query("select timeid, num from l1")
    timeid,num=[],[]
    for i in res:
        timeid.append(i[0])
        num.append(i[1])
    return jsonify({"timeid":timeid,"num":num})

@bp.route('/getChinaMap')
def get_china_map():
    """"获取地图分布数据"""
    
    res=sql_query("select province ,num from map")
    data=[]
    for i in res:
        data.append({"name":i[0],"value":i[1]})
    return  jsonify({"data":data})

@bp.route('/getWordCloud')
def get_word_cloud():
    """获取词云图数据"""
    
    res=sql_query("select  word,num from  word_cloud wc ")
    data=[]
    for i in res:
        data.append({"name":i[0],"value":i[1]})
    return jsonify(data)

@bp.route('/getPie')
def get_pie():
    """获取饼图数据"""
    
    res=sql_query("select  name,num from  pie ")
    data=[]
    for i in res:
        data.append({"name":i[0],"value":i[1]})
    return jsonify(data)

@bp.route('/getBar')
def get_bar():
    """获取柱形图数据"""
    
    res=sql_query("select  area,num from  bar ")
    name,value=[],[]
    for i in res:
        name.append(i[0])
        value.append(i[1])
    return jsonify({"name":name,"value":value})

@bp.route('/dashboard')
def index():
    return render_template('dashboard.html')