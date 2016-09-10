# -*- coding: utf-8 -*-


class Solution(object):
    """算法思路：

    DFS搜索
    """
    def dfs(self, s, start1, end1, t, start2, end2):
        if start1 > end1:
            return True

        if (end1 - start1) > (end2 - start2):
            return False

        for i in xrange(start2, end2 + 1):
            if s[start1] == t[i] and self.dfs(
                    s, start1 + 1, end1, t, i + 1, end2):
                return True

        return False

    def isSubsequence(self, s, t):
        return self.dfs(s, 0, len(s) - 1, t, 0, len(t) - 1)


class Solution(object):
    """算法思路：

    贪心
    """
    def isSubsequence(self, s, t):
        if not s:
            return True

        i = 0
        for char in t:
            if s[i] == char:
                i += 1

            if i == len(s):
                return True

        return False


import bisect


class Solution(object):
    """算法思路：

    利用二分解决Follow Up的问题
    """
    def build(self, t):
        self.queue = [[] for _ in xrange(26)]
        for i, char in enumerate(t):
            self.queue[ord(char) - 97].append(i)

    def isSubsequence(self, s, t):
        self.build(t)

        index = -1
        for char in s:
            queue = self.queue[ord(char) - 97]
            i = bisect.bisect_left(queue, index + 1)

            if i == len(queue):
                return False

            index = queue[i]
        return True


s = Solution()
print s.isSubsequence("", "acbd")
