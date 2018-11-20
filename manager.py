from flask_migrate import MigrateCommand
from flask_script import Manager

from App import creatApp

app = creatApp()
manager = Manager(app)

@app.route('/')
def hello_world():
    return 'Hello World!'
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
