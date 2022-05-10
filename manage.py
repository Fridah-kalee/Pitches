from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch
from  flask_migrate import Migrate

# creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User=user,Pitch = Pitch )


if __name__=='__main__':
    manager.run()
