from flask_migrate import Migrate
from flask_web import app,db,manager


if __name__ == '__main__':
    db.create_all()
    manager.app.run()