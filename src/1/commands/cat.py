import click
import requests
import multiprocessing as mp
from itertools import chain
from templates.utils import render_template
from flask.cli import AppGroup


cat_cli = AppGroup("cat")


def get_facts(page: int = 1):
    return requests.get(f'https://catfact.ninja/facts?page={page}').json()

def get_facts_li(page: int = 1):
    return get_facts(page)['data']

def get_all_facts(parallel_requests: int = None):
    if not parallel_requests:
        parallel_requests = mp.cpu_count() if mp.cpu_count() > 4 else 4
    first, pool = get_facts(), mp.Pool(parallel_requests)
    li, last_page = first['data'], first['last_page']
    return list(chain(li, *pool.map(get_facts_li, range(2, last_page))))


@cat_cli.command("facts")
@click.argument('parallel-requests', nargs=-1, type=int)
def command(parallel_requests: int = None):
    kwargs = {'facts': get_all_facts(parallel_requests)}
    print(render_template('catfacts', **kwargs))
