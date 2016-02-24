# -*- coding: utf-8 -*-

'''
H-Index II
==========

Follow up for H-Index: What if the citations array is sorted in ascending
order? Could you optimize your algorithm?
'''


class Solution(object):
    '''算法思路：

    从右往左，找到最后一个使得 num[mid] >= n - mid，返回长度 n - mid
    '''
    def hIndex(self, citations):
        n = len(citations)

        low, high = 0, n - 1
        while low <= high:
            mid = low + high >> 1
            if citations[mid] < n - mid:
                low = mid + 1
            else:
                if mid == 0 or citations[mid - 1] < n - mid + 1:
                    return n - mid
                high = mid - 1
        return 0


s = Solution()
print s.hIndex([0, 0, 0])
