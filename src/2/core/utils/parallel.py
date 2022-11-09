import multiprocessing as mp
from _proj.settings import MIN_PROCESSES_QUANTITY, USE_ALL_CPU_CORES


cores = mp.cpu_count()
mpqty = cores if USE_ALL_CPU_CORES and cores >= MIN_PROCESSES_QUANTITY else MIN_PROCESSES_QUANTITY


def map(fn: callable, li: list, processes: int = mpqty):
    return mp.Pool(processes).map(fn, li)


def foreach(fn: callable, li: list, processes: int = mpqty):
    return mp.Pool(processes).apply(fn, li)
