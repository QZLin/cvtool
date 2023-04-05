import math
import warnings
from random import randint
from typing import Iterable


def randpos(pos=None, offset=10, area=None, mode='center'):
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


def remove_similar_vec(vector_list, distance):
    """
    attention! each of vec size must be same
    """
    vectors = vector_list.copy()
    if len(vectors) <= 1:
        return vectors
    for vec in vectors:
        others = vectors.copy()
        others.remove(vec)
        for vec2 in others:
            temp = 0
            for i, v in enumerate(vec):
                temp += (v - vec2[i]) ** 2
            dis_ = math.sqrt(temp)
            if dis_ > distance:
                vectors.remove(vec)
                break

    return vectors


rm_cpt = remove_similar_vec
