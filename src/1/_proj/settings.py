import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MIN_PROCESSES_QUANTITY=os.getenv('MIN_PROCESSES_QUANTITY', 4)

USE_ALL_CPU_CORES=os.getenv('USE_ALL_CPU_CORES', True)
