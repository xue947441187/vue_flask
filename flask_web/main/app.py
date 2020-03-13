import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# print()
from flask_migrate import Migrate
from flask_web import app,db,manager
if __name__ == '__main__':
    # db.create_all()
    # manager.app.run()

    app.run(host="0.0.0.0",port=5000)