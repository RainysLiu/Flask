
from flask_script import Manager
from restapp.rest import *

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
