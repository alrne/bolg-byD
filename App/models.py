
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 用户
'''以最少属性定义model'''

# 用户表
class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    u_name = db.Column(db.String(50),unique=True)
    u_password = db.Column(db.String(50))
    u_email = db.Column(db.String(20),unique=True)
    u_token = db.Column(db.String(256))
    is_active = db.Column(db.Boolean,default=False)
    is_delete = db.Column(db.Boolean,default=False)

class BlogModel(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    b_title = db.Column(db.String(50))       # 博客标题
    b_subject = db.Column(db.String(20))    # 博客主题
    b_content = db.Column(db.Text)          # 博客内容
    is_delete =db.Column(db.Boolean,default=False)
    b_user = db.Column(db.ForeignKey(UserModel.id))  # 一个用户可以拥有多个博客

# 博客用户收藏表
class CollectionModel(db.Model):
    __tablename__ = 'collect_relation'  # 收藏关系
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    user = db.Column(db.ForeignKey(UserModel.id))    # 收藏用户
    blog = db.Column(db.ForeignKey(BlogModel.id))   # 被收藏博客

