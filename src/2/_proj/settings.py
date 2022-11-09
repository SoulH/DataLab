import os
from flask import Flask


SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///sitio.db')

MIN_PROCESSES_QUANTITY=os.getenv('MIN_PROCESSES_QUANTITY', 4)

USE_ALL_CPU_CORES=os.getenv('USE_ALL_CPU_CORES', True)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI