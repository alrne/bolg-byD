from flask import session, request
from flask_restful import Resource

# 收藏和搜索信息
from App.models import UserModel, CollectionModel, BlogModel, db


# 收藏关系
class CollectResource(Resource):
    # 收藏
    def put(self):
        user_id = session.get('token')
        if user_id is None:
            data = {'msg':'未登录'}
            return {'returnCode':400,'returnValue':data}
        blog_id = session.get('blog')
        collection = CollectionModel()
        collection.user = user_id
        collection.blog = blog_id
        db.session.add(collection)
        db.session.commit()
        print('收藏成功')
        data = {'msg':'ok'}
        return {'returnCode':200,'returnValue':data}
    # 根据传入info 判断查找 目标 【收藏，用户】
    def get(self):
        info = request.args.get('info')
        if not info:
            data = [{'msg': '未传输info'}]
            return {'returnCode':403,'returnValue':data}
        if info == 'blog':
            blog_id = session.get('blog')
            if blog_id:
                collections = CollectionModel.query.filter_by(blog=int(blog_id))
                if collections.count()>0:
                    user_list = []
                    for collection in collections:
                        username = UserModel.query.filter_by(id=collection.user).first().u_name
                        user_list.append(username)
                    return {'returnCode':200,'returnValue':user_list}
            data = [{'msg':'null'}]
            return {'returnCode':400,'returnValue':data}
        if info == 'user':
            user_id = session.get('token')
            if user_id:
                collections = CollectionModel.query.filter_by(user=int(user_id))
                if collections.count()>0:
                    blog_list = []
                    for collection in collections:
                        blog_title = BlogModel.query.filter_by(id=collection.blog).first().b_title
                        blog_list.append(blog_title)
                    return {'returnCode': 200, 'returnValue': blog_list}
            data = [{'msg': 'null'}]
            return {'returnCode': 400, 'returnValue': data}
        else:
            return {'returnCode': 400, 'returnValue': ['error']}
