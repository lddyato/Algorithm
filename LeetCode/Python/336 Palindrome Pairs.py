# -*- coding: utf-8 -*-

"""
Palindrome Pairs
================

Given a list of unique words. Find all pairs of distinct indices (i, j) in the
given list, so that the concatenation of the two words, i.e.
words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""


class Solution(object):
    '''算法思路：

    brute force

    Time: O(n^2*k), k is the average length of words

    结果：TLE
    '''
    def isPalindrome(self, word):
        i, j = 0, len(word) - 1
        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True

    def palindromePairs(self, words):
        n, r = len(words), []
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPalindrome(words[i] + words[j]):
                    r.append([i, j])

                if self.isPalindrome(words[j] + words[i]):
                    r.append([j, i])
        return r


class Solution(object):
    '''算法思路：

    因为结果已知，由结果推导未知数，然后寻找未知数是否在表里边，是 hashtable 常见的一种应用，
    比如像 Two Sum，Three Sum 等等
    '''
    def palindromePairs(self, words):
        table, r = dict(map(reversed, enumerate(words))), set()
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                a, b = word[:k], word[k:]

                if a == a[::-1] and table.get(b[::-1], -1) not in [-1, i]:
                    r.add((table[b[::-1]], i))

                if b == b[::-1] and table.get(a[::-1], -1) not in [-1, i]:
                    r.add((i, table[a[::-1]]))

        return list(r)


# ['', 'a'] => [[0, 1], [1, 0]]
# ['', 'aa'] => [[0, 1], [1, 0]]
# ['aa', 'abc'] => []
# ['aa', 'baa'] => [[0, 1]]
# ['abc'] => []


s = Solution()
print s.palindromePairs(['', 'a'])
