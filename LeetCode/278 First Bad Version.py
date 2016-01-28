# -*- coding: utf-8 -*-

'''
You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version. You should
minimize the number of calls to the API.
'''


class Solution(object):
    def judgeBadVersion(self, n):
        if n not in self.record:
            self.record[n] = isBadVersion(n)
        return self.record[n]

    def firstBadVersion(self, n):
        self.record = {}

        low, high = 1, n
        while low <= high:
            mid = (low + high) / 2
            if not self.judgeBadVersion(mid):
                low = mid + 1
                continue

            if mid > 1 and not self.judgeBadVersion(mid - 1) or mid == 1:
                return mid

            high = mid - 1
        return low


def isBadVersion(i):
    return [100, 0, 0, 0, 0, 0, 0, 0][i]


s = Solution()
print s.firstBadVersion(7)
