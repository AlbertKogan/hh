# -*- coding: utf-8 -*-
from fractions import gcd
from multiprocessing import Pool


class Container(object):
    def __init__(self, size, current):
        self.size = size
        self.current = current

    @property
    def free(self):
        return self.size - self.current


def empty(container):
        container.current = 0
        return container


def fill(src, trg, res):
    if src.current == 0:
        src.current = src.size
        res.append([src.current, trg.current])
    if trg.free == 0:
        trg.current = 0
        res.append([src.current, trg.current])
    if src.current <= trg.free:
        trg.current += src.current
        empty(src)
        res.append([src.current, trg.current])
    elif src.current > trg.free:
        src.current -= trg.free
        trg.current = trg.size
        res.append([src.current, trg.current])
    return src, trg, res


def transfusion(source, target, value, res):
    grand = gcd(source.size, target.size)
    if value % grand == 0:
        if source.current != value and \
                target.current != value and \
                source.current + target.current != value:

            fill(source, target, res)
            return transfusion(source, target, value, res)
    else:
        print u'Sorry, can\'t get correct result'
    return res


input_containers = map(int, raw_input(u'Enter volume of 2 containers separated '
                                      u'by a space: ').split(' '))
result_value = int(raw_input(u'Enter result value: '))

container_1 = Container(input_containers[0], 0)
container_2 = Container(input_containers[1], 0)

args = [
    [container_1, container_2, result_value, []],
    [container_2, container_1, result_value, []],
]

pool = Pool()
result = [
    pool.apply_async(transfusion, args[0]),
    pool.apply_async(transfusion, args[1]),
]

pool.close()
pool.join()

result_1 = result[0].get()
result_2 = result[1].get()

min_length = min(len(result_1), len(result_2))

if min_length == len(result_1):
    for i in result_1:
        print i
else:
    for j in result_2:
        print j
