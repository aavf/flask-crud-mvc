import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://user:password@127.0.0.1/db_name' # MYSQL
SQLALCHEMY_TRACK_MODIFICATIONS = False