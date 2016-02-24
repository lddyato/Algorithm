# -*- coding: utf-8 -*-

'''
H-Index
=======

Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h
if h of his/her N papers have at least h citations each, and the other N − h
papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has
5 papers in total and each of them had received 3, 0, 6, 1, 5 citations
respectively. Since the researcher has 3 papers with at least 3 citations each
and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as
the h-index.
'''


class Solution(object):
    '''算法思路：

    将数组按照从大到小的顺序排序，然后从前往后遍历直到 index > 当前的 citation 值

    Time: O(n*log(n))
    '''
    def hIndex(self, citations):
        for i, num in enumerate(sorted(citations), 1):
            if num < i:
                return i - 1
        return len(citations)


class Solution(object):
    '''算法思路：

    由于 h-index <= 数组的长度, 因此可以利用 couting sort

    Time: O(n)
    '''
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)

        for num in citations:
            count[min(n, num)] += 1

        r = 0
        for i in xrange(n, 0, -1):
            r += count[i]
            if r >= i:
                return i
        return 0


s = Solution()
print s.hIndex([3, 0, 6, 1, 5])
