import os
from _proj.settings import BASE_DIR
from jinja2 import Environment, FileSystemLoader, Template


template_ext = '.jinja2'


def get_template(template_name: str) -> Template:
    if not template_name.endswith(template_ext):
        template_name += template_ext
    path = os.path.join(BASE_DIR, "templates")
    env = Environment(loader=FileSystemLoader(path))
    return env.get_template(template_name)


def render_template(template_name: str, **kwargs: dict) -> str:
    return get_template(template_name).render(**kwargs)