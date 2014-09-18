import collections
import functools


class memoized(object):
    # https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
        # uncacheable. a list, for instance.
        # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


@memoized
def partition(num, summands):
    if num == summands:
        return 1
    if summands == 1:
        return 1
    if summands > num:
        return 0
    return partition(num-1, summands-1) + partition(num-summands, summands)

n = int(raw_input(u'Enter number (n): '))
k = int(raw_input(u'Enter number of summands (k): '))

print partition(n, k)
