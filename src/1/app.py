from flask import Flask
from commands.cat import cat_cli


app = Flask(__name__)
app.cli.add_command(cat_cli)
