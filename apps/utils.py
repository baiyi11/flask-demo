'''
Description: 
Author: baiyi
Date: 2022-02-08 14:45:41
LastEditTime: 2022-02-10 14:24:13
LastEditors: baiyi
Reference: 
'''
import time 
import pymysql
def get_now():
    now=time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())
    return now

def get_conn():
    """创建连接,游标
    """
    conn =pymysql.connect(host="127.0.0.1", 
                        user="mysql", 
                        password="123456",
                        db="testdb", 
                        charset="utf8")

    cursor=conn.cursor()
    return conn,cursor

def close_conn(conn,cursor):
    """关闭连接"""
    cursor.close()
    conn.close()


def sql_query(sql,*args):
    """SQL语句执行"""
    try:
        conn,cursor = get_conn()
        cursor.execute(sql,args)
        res=cursor.fetchall()
        close_conn(conn,cursor)
        return res
    except Exception as e:
        print(e)


