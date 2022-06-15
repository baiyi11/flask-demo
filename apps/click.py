'''
Description: 
Author: baiyi
Date: 2022-01-25 16:49:58
LastEditTime: 2022-01-26 09:56:23
LastEditors: baiyi
Reference: 
'''
from flask import Blueprint, request, render_template, jsonify

bp = Blueprint("click", __name__)


@bp.route("/getNum", methods=["GET", "POST"])
def get_num():
    name = request.values.get("name")
    score = request.values.get("score")
    print(f"name:{name},score:{score}")
    return jsonify(1000)


@bp.route("/num")
def click():
    return render_template('click.html')
