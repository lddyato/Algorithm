# -*- coding: utf-8 -*-

'''
Minimum Window Substring
========================

Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the
empty string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.
'''

import collections
import operator


class Solution(object):
    '''算法思路：

    sliding window，关键一点是如何花费 O(1) 的时间去比较 window 里边的字符集合是否
    包含 t，这里用了 位压缩 这个技巧
    '''
    def minWindow(self, s, t):
        rs, rt = collections.defaultdict(int), collections.Counter(t)
        destS, destT = 0, reduce(operator.or_, (1 << ord(c) - 65 for c in t))

        head, tail, start, end = 0, 0, float('-inf'), float('inf')
        while 1:
            while head < len(s) and destS != destT:
                char = s[head]
                rs[char] += 1

                if char in rt and rs[char] >= rt[char]:
                    destS |= 1 << ord(char) - 65

                head += 1

            if head >= len(s) and destS != destT:
                break

            while tail < head and destS == destT:
                char = s[tail]
                rs[char] -= 1

                if head - tail < end - start:
                    start, end = tail, head

                if char in rt and rs[char] < rt[char]:
                    destS &= ~(1 << ord(char) - 65)

                tail += 1

        return s[start:end] if end != float('inf') else ''



class Solution(object):
    '''算法思路：

    同上，不过没用 bit 操作
    '''
    def minWindow(self, s, t):
        counter, times, local = (
            collections.Counter(t), collections.defaultdict(int), set())

        n, m, slow, fast, l, r = len(s), len(counter), 0, 0, float('inf'), ''
        while 1:
            while fast < n and len(local) < m:
                char = s[fast]
                if char in counter:
                    times[char] += 1
                    if times[char] >= counter[char]:
                        local.add(char)
                fast += 1

            if fast >= n and len(local) < m:
                break

            while slow < fast and len(local) >= m:
                if fast - slow < l:
                    l = fast - slow
                    r = s[slow:fast]

                char = s[slow]
                if char in counter:
                    times[char] -= 1
                    if times[char] < counter[char]:
                        local.discard(char)
                slow += 1
        return r


s = Solution()
print s.minWindow('a', 'a')
