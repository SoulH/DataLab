import importlib
import inspect
from types import ModuleType


def get_module(name: str) -> ModuleType:
    return importlib.import_module(name)


def get_classes(module: ModuleType) -> list[tuple[str, type]]:
    return inspect.getmembers(module, inspect.isclass)


def get_class(module: ModuleType, name: str) -> type:
    return [m for n, m in get_classes(module) if n.endswith(name)][0]