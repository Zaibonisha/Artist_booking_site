import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
import psycopg2

conn = psycopg2.connect('host=127.0.0.1 dbname=fyyur user=postgres port=3000')


cur = conn.cursor()





# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@127.0.0.1:3000/fyyur'

