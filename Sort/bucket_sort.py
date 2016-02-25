# -*- coding: utf-8 -*-

'''
桶排序
=====

桶排序与桶大小有关，桶越小，效率越高

时间复杂度：O(n)
空间复杂度：O(n)

是否稳定：是
'''


import math


def bucket_sort(array):
    n, start, end = len(array), min(array), max(array)

    size = int(math.ceil(float(end - start + 1) / n))
    n, size = max(n, size), min(n, size)

    buckets = [[] for _ in xrange(n)]
    for num in array:
        i = (num - start) / size
        buckets[i].append(num)

    i = 0
    for bucket in buckets:
        array[i:i + len(bucket)] = sorted(bucket)
        i += len(bucket)

    return array


print bucket_sort([1900, 1, 10, 14, 16, 4, 900, 9, 3, 2, 8, 200, 11, 10])
