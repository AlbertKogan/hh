def partition(num, summands):
    if num == summands:
        return 1
    if summands == 1:
        return 1
    if summands > num:
        return 0
    return partition(num-1, summands-1) + partition(num-summands, summands)

n = int(raw_input(u'Enter n: '))
k = int(raw_input(u'Enter k: '))

print partition(n, k)