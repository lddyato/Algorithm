# -*- coding: utf-8 -*-

'''
Generalized Abbreviation
========================

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
"w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''


class Solution(object):
    '''算法思路：

    递归
    '''
    def generate(self, word, preIsDigit):
        if not word:
            return [[]]

        r = [[word[0]] + p for p in self.generate(word[1:], False)]
        if not preIsDigit:
            r += sum([
                [[str(i)] + p for p in self.generate(word[i:], True)]
                for i in xrange(1, len(word) + 1)
            ], [])
        return r

    def generateAbbreviations(self, word):
        return map(''.join, self.generate(word, False))


class Solution(object):
    '''算法思路：

    同上，不过加了缓存
    '''
    def cache(f):
        def method(obj, *args):
            key = '{}:{}'.format(*args)

            if not hasattr(obj, 'r'):
                setattr(obj, 'r', {})

            if key not in obj.r:
                obj.r[key] = f(obj, *args)

            return obj.r[key]
        return method

    @cache
    def generate(self, word, preIsDigit):
        if not word:
            return [[]]

        r = [[word[0]] + p for p in self.generate(word[1:], False)]
        if not preIsDigit:
            r += sum([
                [[str(i)] + p for p in self.generate(word[i:], True)]
                for i in xrange(1, len(word) + 1)
            ], [])
        return r

    def generateAbbreviations(self, word):
        return map(''.join, self.generate(word, False))


class Solution(object):
    '''算法思路：

    迭代
    '''
    def generateAbbreviations(self, word):
        import collections

        if not word:
            return ['']

        word = collections.deque(word)
        queue = collections.deque([[word.popleft()], [1]])

        while word:
            char = word.popleft()

            for _ in xrange(len(queue)):
                node = queue.popleft()
                queue += [node + [char]] + (
                    [node[:-1] + [node[-1] + 1]]
                    if isinstance(node[-1], int) else [node + [1]]
                )

        return map(lambda r: ''.join(map(str, r)), queue)


s = Solution()
print s.generateAbbreviations("a")
