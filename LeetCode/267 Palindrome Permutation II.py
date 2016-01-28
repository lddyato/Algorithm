# -*- coding: utf-8 -*-

'''
Palindrome Permutation II
=========================

Given a string s, return all the palindromic permutations (without duplicates)
of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].
'''


class Solution(object):
    '''算法思路：

    结合 判断是否能够生成回文数 + 生成不重复的字典序列
    '''
    def _gen_permutation(self, chars):
        existed = {}

        if not chars:
            return []

        if len(chars) == 1:
            return chars

        result = []
        for i, c in enumerate(chars):
            if c not in existed:
                result.append([
                    c + p
                    for p in self._gen_permutation(chars[:i] + chars[i+1:])])
                existed[c] = 1

        return sum(result, [])

    def generatePalindromes(self, s):
        if len(s) == 1:
            return [s]

        maps = {}
        for c in s:
            maps[c] = maps.setdefault(c, 0) + 1

        count, chars, pivot = 0, [], ''
        for c, v in maps.items():
            div, mod = divmod(v, 2)

            if mod:
                count += 1
                if count > 1:
                    return []
                pivot = c

            chars += [c] * div

        return map(
            lambda p: ''.join([p, pivot, p[::-1]]),
            self._gen_permutation(chars))


s = Solution()
print s.generatePalindromes('a')
