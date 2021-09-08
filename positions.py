from random import randint
from typing import Iterable


def randpos(pos, offset=10, area=None, mode='center'):
    if isinstance(pos, Iterable):
        return [randpos(x) for x in pos]
    else:
        if mode == 'center':
            return pos + randint((-offset) // 2, offset // 2)
        elif mode == 'rectangle':
            p1, p2 = area
            ax, ay = p1
            bx, by = p2
            xs = [ax, bx]
            xs.sort()
            ys = [ay, by]
            ys.sort()
            return [randint(xs[0], xs[-1]), randint(ys[0], ys[-1])]
