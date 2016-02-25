# -*- coding: utf-8 -*-

'''
基数排序
=======

时间复杂度：O(k*n)
空间复杂度：O(n)

是否稳定：是
'''


def radix_sort(array):
    array = map(str, array)
    k = max(map(len, array))

    array = ['0' * (k - len(num)) + num for num in array]
    for i in xrange(k - 1, -1, -1):
        buckets = [[] for _ in xrange(10)]
        for num in array:
            buckets[ord(num[i]) - 48].append(num)
        array = sum(buckets, [])

    return map(int, array)


print radix_sort([23, 4, 5, 1, 345, 89, 7])
