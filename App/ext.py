from flask_cache import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session

# db = SQLAlchemy()
from App.models import db

migrate = Migrate()
mail = Mail()
cache = Cache(config={'CACHE_TYPE':'redis'})

#初始化
def init_app(app):
    db.init_app(app)
    migrate.init_app(app,db)
    Session(app)
    mail.init_app(app)
    cache.init_app(app)
