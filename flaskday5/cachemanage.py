from flask_script import Manager
from cacheapp import *


app = createapp()
manager = Manager(app)


if __name__ == "__main__":
    manager.run()



