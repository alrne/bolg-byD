from flask import Flask

from App import setting
from App.Apis import init_api
from App.ext import init_app

env_info = 'develop'

def creatApp():
    app = Flask(__name__)
    app.config.from_object(setting.env.get(env_info))
    init_app(app)
    init_api(app)
    return app