from decimal import Decimal
from enum import Enum


def to_serializable(val):
    if isinstance(val, bytes):
        return val.decode()
    if isinstance(val, Enum):
        return val.name
    if isinstance(val, Decimal):
        return float(val)
    return val


def filter_dict(conditions: callable, dic: dict):
    return {k: to_serializable(v) for k, v in dic.items() if conditions(k, v)}
