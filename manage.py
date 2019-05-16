from flask_migrate import MigrateCommand, Migrate
from flask_script import Server, Manager

from src import create_app

manager = Manager(create_app('development'))
manager.add_command("runserver", Server())
manager.add_option("-c", "--config", dest="config_module", required=False)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
