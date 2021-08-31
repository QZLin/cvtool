from random import randint
from typing import Iterable


def randpos(pos, offset=10):
    if isinstance(pos, Iterable):
        return [randpos(x) for x in pos]
    else:
        return pos + randint(0, offset)
