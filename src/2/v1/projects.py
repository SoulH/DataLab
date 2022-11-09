from flask import Blueprint, jsonify
from _proj.database import db_factory


db, url_base = db_factory(), '/proyecto'
project_api_v1 = Blueprint('project_api_v1', __name__)


@project_api_v1.route(f'{url_base}/<id_proyecto>')
def get_by_project_id(id_proyecto: str):
    proyectos = db.projects.find(project_name__like=f'%{id_proyecto}%')
    usuarios = db.users.user_roles()
    return jsonify({'proyectos': proyectos, 'usuarios': usuarios})
