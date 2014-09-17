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

res = []


def transfusion(source, target, value):
    global res
    grand = gcd(source.size, target.size)

    def empty(container):
        container.current = 0
        return container

    def fill(src, trg):
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

    if value % grand == 0:
        if source.current != value and target.current != value and source.current + target.current != value:
            fill(source, target)
            return transfusion(source, target, value)
    else:
        print u'Sorry, can\'t get correct result'
    return res

input_containers = map(int, raw_input(u'Enter volume of 2 containers: ').split(' '))
result_value = int(raw_input(u'Enter result value: '))

pool = Pool()
container_1 = Container(input_containers[0], 0)
container_2 = Container(input_containers[1], 0)
args = [[container_1, container_2, result_value], [container_2, container_1, result_value]]
result_1 = pool.apply_async(transfusion, args[0]).get()
result_2 = pool.apply_async(transfusion, args[1]).get()
result = min(result_1, result_2)

for item in result:
    print item