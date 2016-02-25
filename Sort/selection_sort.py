# -*- coding: utf-8 -*-

'''
选择排序
=======

时间复杂度：O(n^2)
空间复杂度：O(1)

是否稳定：否
'''


def selection_sort(array):
    n = len(array)
    for i in xrange(n):
        min = i
        for j in xrange(i + 1, n):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array


a = [23, 4, 5, 1, 345, 89, 7]
print selection_sort(a)
