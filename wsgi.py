import os

from src import create_app
from src.settings import DEBUG

config_name = 'production'
if DEBUG:
    config_name = 'development'

app = create_app(config_name)

if __name__ == '__main__':
    app.run()
