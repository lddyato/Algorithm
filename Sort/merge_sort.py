# -*- coding: utf-8 -*-

'''
归并排序
=======

时间复杂度：O(n * log(n))
空间复杂度：O(n)

是否稳定：是
'''


def merge(array1, array2):
    m, n, i, j, r = len(array1), len(array2), 0, 0, []
    while i < m and j < n:
        if array1[i] < array2[j]:
            r.append(array1[i])
            i += 1
        else:
            r.append(array2[j])
            j += 1
    r += array1[i:] or array2[j:]
    return r


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array

    mid = n >> 1
    return merge(*map(merge_sort, (array[:mid], array[mid:])))


"===================================================================="


def merge_sort(array):
    """算法思路：

    自底向上的写法, in replace
    """
    half, n = 1, len(array)

    while half < n:
        for start in xrange(0, n, half << 1):
            end = min(start + (half << 1) - 1, n - 1)
            i, j = start, start + half

            while i < j and j <= end:
                if array[i] < array[j]:
                    i += 1
                else:
                    num = array[j]
                    array[i + 1:j + 1] = array[i:j]
                    array[i] = num

                    i += 1
                    j += 1
        half <<= 1

    return array


import random

for _ in range(10):
    l = [random.randint(0, 100) for _ in xrange(random.randint(0, 100))]
    assert merge_sort(l) == sorted(l)
