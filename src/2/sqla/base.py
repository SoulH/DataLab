import re
import inspect
from typing import List
from sqlalchemy import text
from _proj.settings import app
from flask_sqlalchemy import SQLAlchemy
from core.data.mappers import filter_dict


def session_maker():
    db = SQLAlchemy()
    db.init_app(app)
    return db.session


def get_fields(cls: type) -> List[str]:
    members = inspect.getmembers(cls, lambda x: not inspect.isroutine(x))
    return [name for name, obj in members if '_' not in name and name != 'metadata']


def get_field_map(cls: type) -> dict:
    return {field: getattr(cls, field).__dict__['key'] for field in get_fields(cls)}


def to_dict(instance, exclude: list = []):
    def conditions(k, v):
        return not k.startswith('_') and k not in exclude
    return filter_dict(conditions, instance.__dict__)


def map_filters(cls: type, **kwargs):
    def translate(expr: str, val):
        op = re.findall(r'__\w+', expr)
        op = op[0][2:] if op else '='
        pr = expr.replace(f"__{op}", "").replace("__", ".")
        if isinstance(val, str):
            val = f"'{val}'"
        if isinstance(val, list):
            if all([isinstance(v, str) for v in val]):
                val = [f"'{v}'" for v in val]
            val = f"({', '.join(val)})"
        if op == 'lt':
            op = '<'
        if op == 'lte':
            op = '<='
        if op == 'gt':
            op = '>'
        if op == 'gte':
            op = '>='
        if op == 'neq':
            op = '!='
        return text(f"{pr} {op} {val}")
    return [translate(k, v) for k, v in kwargs.items()]

