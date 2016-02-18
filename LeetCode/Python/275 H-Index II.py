# -*- coding: utf-8 -*-

'''
H-Index II
==========

Follow up for H-Index: What if the citations array is sorted in ascending
order? Could you optimize your algorithm?
'''


class Solution(object):
    '''算法思路：

    二分查找
    '''
    def hIndex(self, citations):
        low, high, n = 0, len(citations) - 1, len(citations)
        while low <= high:
            mid = low + high >> 1
            if n - mid <= citations[mid]:
                high = mid - 1
            else:
                if (mid + 1 < n and n - 1 - mid <= citations[mid + 1] or
                        mid + 1 == n):
                    return n - 1 - mid
                low = mid + 1
        return n


s = Solution()
print s.hIndex([0, 0, 0])
