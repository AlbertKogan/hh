# -*- coding: utf-8 -*-
from fractions import gcd
from multiprocessing import Pool


class Container(object):

    def __init__(self, size=None, current=None):
        self.size = size
        self.current = current

    @property
    def free(self):
        return self.size - self.current

    def empty(self):
        self.current = 0
        return self


def fill(src, trg, res):
    if src.current == 0:
        src.current = src.size
        res.append([src.current, trg.current])

    if trg.free == 0:
        trg.current = 0
        res.append([src.current, trg.current])

    if src.current <= trg.free:
        trg.current += src.current
        src.empty()
        res.append([src.current, trg.current])
    elif src.current > trg.free:
        src.current -= trg.free
        trg.current = trg.size
        res.append([src.current, trg.current])
    return src, trg, res


def transfuse(source, target, value, res):
    if (source.current != value and
            target.current != value and
            source.current + target.current != value):

        fill(source, target, res)
        return transfuse(source, target, value, res)
    return res


def main(source, target, value):
    if result_value % gcd(source.size, target.size) == 0:
        args = [
            [source, target, value, []],
            [target, source, value, []],
        ]
        pool = Pool()
        result = [
            pool.apply_async(transfuse, args[0]),
            pool.apply_async(transfuse, args[1]),
        ]
        pool.close()
        pool.join()

        result_1 = result[0].get()
        result_2 = result[1].get()

        if len(result_1) == min(len(result_1), len(result_2)):
            min_result = result_1
        else:
            min_result = result_2

        for i in min_result:
            print i
    else:
        print u'Sorry, can\'t get correct result'


if __name__ == '__main__':
    input_containers = map(int, raw_input(u'Enter volume of 2 containers '
                                          u'separated by space: ').split(' '))
    result_value = int(raw_input(u'Enter result value: '))

    container_1 = Container(input_containers[0], 0)
    container_2 = Container(input_containers[1], 0)

    main(container_1, container_2, result_value)
