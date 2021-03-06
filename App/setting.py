

def getDataUri(data):
    dialect = data.get('dialect') or 'mysql'
    driver = data.get('driver') or 'pymysql'
    name = data.get('name') or 'root'
    password = data.get('password') or '1234'
    host = data.get('host') or 'localhost'
    port = data.get('port') or '3306'
    database = data.get('database') or 'test'
    return "{}+{}://{}:{}@{}:{}/{}" .format(dialect,driver,name,password,host,port,database)

class Config():
    DEBUG = False
    TEST = False
    SECRET_KEY = '100'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'
    # 配置邮箱
    MAIL_SERVER = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class DevelopConfig(Config):
    DEBUG = True
    database_info = {
        'dialect'  :  'mysql',
        'driver'   :  'pymysql',
        'name'     :  'root',
        'password' :  '1234',
        'host'     :  'localhost',
        'port'     :  '3306',
        'database' :  'test',
    }
    SQLALCHEMY_DATABASE_URI = getDataUri(database_info)

env = {
    'develop':DevelopConfig
}