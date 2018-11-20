import uuid

from flask_mail import Message
from flask import render_template, request, session
from flask_restful import Resource, reqparse

from App.ext import cache, mail
from App.models import UserModel, db


# 用户注册 登录
class UserDoResource(Resource):
    # 注册
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help='用户名格式不正确')
        parser.add_argument('password',type=str,required=True,help='密码格式不正确')
        parser.add_argument('email',type=str,required=True,help='邮箱格式不正确')
        parse = parser.parse_args()
        username = parse.get('username')
        password = parse.get('password')
        email = parse.get('email')
        user = UserModel.query.filter_by(u_name=username)
        if user.first() is not None:
            return {'returnCode':400,'msg':'用户名已存在'}
        user = UserModel.query.filter_by(u_email=email)
        if user.count() > 0:
            return {'returnCode':400,'msg':'邮箱被使用'}
        user = UserModel()
        # 对信息进行左右空格清除
        user.u_name = username.split()
        user.u_password = password.split()
        user.u_email = email.split()
        token = str(uuid.uuid4())
        user.u_token = token
        db.session.add(user)
        db.session.commit()
        # 设置缓存中存储 token
        cache.set(token,user.id,timeout=300)
        msg = Message(recipients=[email],subject='请激活你的账户',sender='13614872486@163.com')
        bodyHtml = render_template('email_model.html',username=username,token=token)
        msg.html = bodyHtml
        mail.send(msg)
        data = {
            'username':username,
            'email':email,
            'msg':'ok'
        }
        return {'returnCode':200,'returnValue':data}
    # 登录  登录后设置session key 为 token
    def post(self):
        username = request.form.get('username')
        password = request.form.get('username')
        name = username.split()
        passwd = password.split()[0]
        user = UserModel.query.filter_by(u_name=name).first()
        if user is not None:
            # 判断是否被激活或者删除
            if user.is_active and not user.is_delete:
                # 进入此处说明 用户激活并且未被删除
                if user.u_password==passwd:
                    # 设置session session key 是token
                    session['token'] = user.id
                    data = {'msg':'ok','username':name}
                    return {'returnCode':200,'returnValue':data}
            data = {'msg':'未激活'}
            return {'returnCode':400,'returnValue':data}
        data = {'msg': '用户名或密码不正确'}
        return {'returnCode': 200, 'returnValue': data}
    # 删除
    def delete(self):
        user_id = session.get('token')
        # parser = reqparse.RequestParser()
        # parser.add_argument('username',type=str,required=True,help='用户信息错误')
        # parse = parser.parse_args()
        # username = parse.get('username')
        user = UserModel.query.filter_by(id=user_id).first()
        data = {'msg': 'ok'}
        if user is not None:
            # 用户存在执行逻辑删除
            user.is_delete = True
            db.session.commit()
            return {'returnCode':200,'returnValue':data}
        data['msg']='bad'
        return {'returnCode': 200, 'returnValue': data}
    # 修改
    def get(self):
        # 使用缓存中存储的token进行数据修改
        user_id = request.args.get('token')
        user = UserModel.query.filter_by(id=user_id).first()
        username = request.args.get('username')
        if username:
            user.u_name = username
        password = request.args.get('password')
        if password:
            user.u_password =password
        email = request.args.get('email')
        if email:
            user.u_email = email
        db.session.commit()
        data = {'msg':'ok'}
        return {'returnCode':200,'returnValue':data}




# 激活用户状态
class AccountRescource(Resource):
    def get(self):
        token = request.args.get('token')
        user_id = cache.get(token)
        user = UserModel.query.filter_by(id=user_id).first()
        if user is not None:
            user.is_active = True
            db.session.commit()
            data = {'msg':user.u_name+' ok'}
            return {'returnCode':200,'returnValue':data}
        data = {'msg':  'bad'}
        return {'returnCode': 400, 'returnValue': data}

# 退出用户登录状态
class UserLogoRescource(Resource):
    def get(self):
        session.clear()
        # session.pop('token')
        # session.pop('blog_id')
        return {'return':200,'returnValue':'ok'}