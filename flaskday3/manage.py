from flask import Flask
from flask_script import Manager
from lantu.functions import new_app

app = new_app()
manager = Manager(app)


if __name__ == '__main__':
    manager.run()





