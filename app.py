'''
Description: 
Author: baiyi
Date: 2022-01-13 15:17:43
LastEditTime: 2022-02-22 15:53:53
LastEditors: baiyi
Reference: 
'''
from flask import Flask
import config
from apps.exts import db
from apps.dashboard import bp as dbd_bp
from apps.areasale  import bp as as_bp


app = Flask(__name__)

# app.config.from_object(config)

# 把app绑定到db上
# db.init_app(app)



# 创建表
# db.drop_all()
# db.create_all()


# @app.route('/otm')
# def one_to_many():
#     """ 作者/文章 一对多写入场景"""
#     article=Article(title="红楼梦",content="yyy")
#     user=User(username="曹雪芹")
#     article.author=user
#     print(article.author,article.author_id)
#     db.session.add(article)
#     db.session.commit()

#     return "数据操作成功"

# @app.route('/article')
# def article_view():
    # 添加数据
    # article=Article(title="钢铁是怎样炼成的",content="XX")
    # db.session.add(article)
    # db.session.commit()

    # # 查询数据
    # article=Article.query.filter_by(id=1)[0]
    # print(article.title)

    # #修改数据
    # article=Article.query.filter_by(id=1)[0]
    # article.title="书籍1"
    # db.session.commit()
    # print(article.title)

    # #删除数据
    # Article.query.filter_by(id=2).delete()
    # db.session.commit()
    # return "数据操作成功"



# 注册dashboard模块蓝图
app.register_blueprint(dbd_bp)
# 注册areasale模块蓝图
app.register_blueprint(as_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

