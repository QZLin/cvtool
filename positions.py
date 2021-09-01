from random import randint
from typing import Iterable


def randpos(pos, offset=10, mode='center'):
    if isinstance(pos, Iterable):
        return [randpos(x) for x in pos]
    else:
        if mode == 'center':
            return pos + randint((-offset)//2, offset//2)
