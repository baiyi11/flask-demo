'''
Description: 
Author: baiyi
Date: 2022-02-11 11:06:41
LastEditTime: 2022-02-18 16:36:30
LastEditors: baiyi
Reference: 
'''
from flask import render_template,jsonify,Blueprint,request
from .utils import sql_query

bp = Blueprint("areasale",__name__)

@bp.route('/area')
def area():
    """区域列表"""
    data=[]
    res=sql_query("select province  from map")
    for i in res:
        data.append(i[0])
    return jsonify(data)

@bp.route("/sale")
def sale():
    """获取区域销售接口"""
    area=request.args.get("area")
    data=[]
    sql="select province ,num from map"
    if area:
        sql+=f" where province = '{area}'"
    res=sql_query(sql)
    for i in res:
        data.append({"area":i[0],"sale":i[1]})
    return jsonify(data)

@bp.route('/areasale')
def areasale():
    area1=request.args.get("area1")
    return render_template("areasale.html",area1=area1,ls="dad")
    
