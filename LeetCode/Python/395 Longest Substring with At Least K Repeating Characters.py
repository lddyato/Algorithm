# -*- coding: utf-8 -*-

"""
Longest Substring with At Least K Repeating Characters
======================================================

Find the length of the longest substring T of a given string (consists of
lowercase letters only) such that every character in T appears no less than k
times.

Example 1:

    Input:
    s = "aaabb", k = 3

    Output:
    3

    The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

    Input:
    s = "ababbc", k = 2

    Output:
    5

    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
    repeated 3 times.
"""

import collections


class Solution(object):
    """算法思路：

    快慢指针-Sliding Window

    首先slow指针一直右移直到当前char的数量不小于k，然后fast指针从slow指针开始
    往后遍历，一直到char的数量小于k，中间我们记录slow到fast之间是否所有的char
    的数量都不小于k，并且记录满足上句条件时fast的位置index，然后把slow挪到index
    上，如此循环，一直到slow指针等于s的长度。

    什么时候用sliding window? 一般使用sliding window的情景都会满足以下条件：

      - 当window满足条件时，fast再往前探不会有更优的结果
    """
    def longestSubstring(self, s, k):
        low, r, n, total = 0, 0, len(s), collections.Counter(s)

        while low < n:
            while low < n and total[s[low]] < k:
                total[s[low]] -= 1
                low += 1

            if low >= n:
                break

            high, counter, mask, index = low, collections.defaultdict(
                int), 0, low

            while high < n and total[s[high]] >= k:
                counter[s[high]] += 1

                bit = 1 << ord(s[high]) - 97
                if counter[s[high]] < k:
                    mask |= bit
                else:
                    mask &= ~bit

                if not mask:
                    index = high
                    r = max(r, high - low + 1)

                high += 1

            while low <= index:
                total[low] -= 1
                low += 1

        return r


s = Solution()
print s.longestSubstring("ababbc", 2)
