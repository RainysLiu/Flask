from flask_migrate import Migrate, MigrateCommand
from flask_script import *
from migrateapp.models import *



migrate = Migrate(app,db)      # 实例化迁移对象
manager = Manager(app)
manager.add_command("db",MigrateCommand)          #添加迁移命令

if __name__ == '__main__':
    manager.run()



