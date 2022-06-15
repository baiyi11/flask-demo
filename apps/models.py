'''
Description: 
Author: baiyi
Date: 2022-02-21 14:23:57
LastEditTime: 2022-02-22 11:27:20
LastEditors: baiyi
Reference: 
'''
from  app import db

# 定义ORM模型
class  Article(db.Model):
    """文章ORM"""
    __tablename__ = 'article'
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    title=db.Column(db.String(10),nullable=False)
    content=db.Column(db.Text,nullable=False)
    # 外键
    author_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    author=db.relationship("User",backref="articles")

class User(db.Model):
    """作者ORM"""
    __tablename__ = 'user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)