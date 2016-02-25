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


a = [23, 4, 5, 1, 345, 89, 7]
print merge_sort(a)
