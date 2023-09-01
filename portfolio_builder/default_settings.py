import os


basedir = os.path.abspath(os.path.dirname(__file__))
db_user = os.environ.get('DB_USER')
db_passwd = os.environ.get('DB_PASSWD')
db_host = os.environ.get('DB_HOST')


class Config:
    # Database Configurations
    DB_URL = f'mysql://{db_user}:{db_passwd}@{db_host}'
    SQLALCHEMY_DATABASE_URI = f'{DB_URL}/main'
    SQLALCHEMY_BINDS = {
        "Security_Prices": (f'{DB_URL}/prices')
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
