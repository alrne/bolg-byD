from flask import session, request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser


from App.models import BlogModel, UserModel, db

parser = RequestParser()
parser.add_argument('title',type=str,required=True,help='标题错误')


'''
执行博客操作必须需要用户登录
每进行增删改等操作需要对session[blog_id] 进行更改
'''

class BlogDoResource(Resource):
    # 创建博客
    def put(self):
        user_id = session.get('token')
        if user_id is None:
            data = {'msg':'未登录'}
            return {'returnCode':400,'returnValue':data}
        parser.add_argument('subject', type=str, required=True, help='主题错误')
        parser.add_argument('content', type=str, required=True, help='内容错误')
        par = parser.parse_args()
        title = par.get('title')
        subject = par.get('subject')
        content = par.get('content')
        blog = BlogModel()
        blog.b_title = title
        blog.b_subject = subject
        blog.b_content = content
        user = UserModel.query.filter_by(id=user_id).first()
        blog.b_user = user.id
        db.session.add(blog)
        db.session.commit()
        session['blog'] = blog.id
        print('完成博客保存')
        data = {'msg':'ok'}
        return {'returnCode': 200, 'returnValue': data}
    # 修改博客
    def get(self):
        token = session.get('token')
        if token is None:
            data = {'msg': '无权限修改'}
            return {'returnCode': 400, 'returnValue': data}
        blog_id = session.get('blog_id')
        blog = BlogModel.query.filter_by(id=blog_id).first()
        title = request.args.get('title')
        if title:
            blog.b_title = title
        subject = request.args.get('subject')
        if subject:
            blog.b_subject = subject
        content = request.args.get('content')
        if content:
            blog.b_content = content
        if not title and not subject and not content:
            data = {'msg':'未做任何修改'}
            return {'returnCode':200,'returnValue':data}
        db.session.commit()
        session['blog'] = blog.id
        data = {'msg': '修改成功'}
        return {'returnCode': 200, 'returnValue': data}
    # 博客删除  逻辑删除
    def delete(self):
        user_id = session.get('token')
        if user_id is None:
            data = {'msg':'未登录'}
            return {'returnCode':400,'returnValue':data}
        blog_id = session.get('blog_id')
        if not blog_id:
            data = {'msg': '无权限删除'}
            return {'returnCode': 400, 'returnValue': data}
        blog = BlogModel.query.filter_by(id=blog_id).first()
        blog.is_delete = True
        db.session.commit()
        # 删除blog后 清除session[blog]
        session.pop('blog')
        print('删除成功')
        data = {'msg': '删除成功'}
        return {'returnCode': 200, 'returnValue': data}