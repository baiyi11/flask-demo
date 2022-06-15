'''
Description: 
Author: baiyi
Date: 2022-01-13 15:30:36
LastEditTime: 2022-02-22 10:46:44
LastEditors: baiyi
Reference: 
'''


# JSON_AS_ASCII
JSON_AS_ASCII=False


# DB
HOSTNAME="127.0.0.1"
PORT="3306"
DATABASE="testdb"
USERNAME="mysql"
PASSWORD="123456"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False