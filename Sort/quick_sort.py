# -*- coding: utf-8 -*-

'''
快排
===

时间复杂度：O(n * log(n))
空间复杂度：O(1)

是否稳定：否
'''


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot, i, j = array[start], start + 1, end
    while 1:
        while i <= end and array[i] <= pivot:
            i += 1
        while j > start and array[j] > pivot:
            j -= 1

        if i > j:
            break

        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    array[start], array[j] = array[j], array[start]

    quick_sort(array, start, j - 1)
    quick_sort(array, j + 1, end)

    return array


a = [23, 4, 5, 1, 345, 89, 7]
print quick_sort(a, 0, len(a) - 1)
