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


def find_value(source, target, value):
    grand = gcd(source.size, target.size)

    def empty(container):
        container.current = 0
        return container

    def fill(src, trg):
        if src.current == 0:
            src.current = src.size
        if trg.free == 0:
            trg.current = 0
        if src.current <= trg.free:
            trg.current += src.current
            empty(src)
        elif src.current > trg.free:
            src.current -= trg.free
            trg.current = trg.size
        return src, trg

    if value % grand == 0:
        if source.current != value and target.current != value:
            print source.current, target.current
            fill(source, target)
            return find_value(source, target, value)
        else:
            print u'DONE: ', source.current, target.current
            return
    else:
        print u'Sorry'

input_containers = map(int, raw_input(u'Enter volume of 2 containers: ').split(' '))
result = int(raw_input(u'Enter result value: '))

container_1 = Container(input_containers[0], 0)
container_2 = Container(input_containers[1], 0)

find_value(container_1, container_2, result)