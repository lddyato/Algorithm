# -*- coding: utf-8 -*-

'''
插入排序
=======

时间复杂度：O(n^2)
空间复杂度：O(1)

是否稳定：是
'''


def insertion_sort(array):
    n = len(array)
    for i in xrange(n):
        for j in xrange(i, 0, -1):
            if array[j] >= array[j - 1]:
                break
            array[j], array[j - 1] = array[j - 1], array[j]
    return array


a = [23, 4, 5, 1, 345, 89, 7]
print insertion_sort(a)
