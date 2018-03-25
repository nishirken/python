import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        return json.dumps(func(*args, **kwds))

    return wrapper

