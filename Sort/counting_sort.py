# -*- coding: utf-8 -*-


'''
计数排序
=======

设取值范围为 [start, end]，长度为 k = end - start + 1, 数组长度为 n

时间复杂度：O(n + k)
空间复杂度：O(k)

是否稳定：是
'''


def counting_sort(array, start=0, end=100):
    count = [0] * (end - start + 1)
    for num in array:
        count[num - start] += 1

    i = 0
    for v, n in enumerate(count):
        array[i:i + n] = [v] * n
        i += n

    return array


print counting_sort([8, 3, 9, 2, 1, 8, 2, 3])
