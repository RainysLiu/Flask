from flask import Flask
from flask_script import Manager
from mydbapp.settings import *

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
