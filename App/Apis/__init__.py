from flask_restful import Api

from App.Apis.CollectionApis import CollectResource
from App.Apis.UserApi import UserDoResource, AccountRescource, UserLogoRescource
from App.Apis.BlogApis import BlogDoResource

api = Api()
# 初始化
def init_api(app):
    api.init_app(app)


# 用户注册 登录 修改  删除
api.add_resource(UserDoResource,'/user/')
# 用户激活
api.add_resource(AccountRescource,'/acc/')
# 博客创建 修改 删除
api.add_resource(BlogDoResource,'/blog/')
# 收藏博客 查找
api.add_resource(CollectResource,'/collect/')
# 退出登录
api.add_resource(UserLogoRescource,'/logout/')