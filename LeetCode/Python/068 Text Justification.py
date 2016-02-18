# -*- coding: utf-8 -*-

'''
Text Justification
==================

Given an array of words and a length L, format the text such that each line has
exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.
'''

import itertools


class Solution(object):
    '''算法思路：

    按照题目描述做即可

    - 每一行尽可能多的 words，每一行必须 L 个字符
    - 非最后一行，每个 words 之间的空格应该尽可能平均，若只有一个 word，则左对齐
    - 最后一行，每个 words 之间只能有一个空格，并且左对齐
    '''
    def formLine(self, words, size, maxWidth):
        if size == 1:
            return words[0] + ' ' * (maxWidth - len(words[0]))

        base, mod = divmod(maxWidth - sum(map(len, words)), size - 1)
        return ''.join(words[:1] + map(''.join, itertools.izip(
            itertools.chain(
                itertools.repeat(' ' * (base + 1), mod),
                itertools.repeat(' ' * base, size - 1 - mod)),
            words[1:]
        )))

    def formLastLine(self, words, size, maxWidth):
        r = ' '.join(words)
        return r + ' ' * (maxWidth - len(r))

    def fullJustify(self, words, maxWidth):
        i, n, L, lines = 0, len(words), maxWidth, []
        while i < n:
            length, j = 0, i
            while i < n:
                add = len(words[i]) + (length != 0)
                if length + add > L:
                    break
                length += add
                i += 1
            lines.append([j, i])

        return [f(words[j:i], i - j, L) for f, (j, i) in itertools.izip(
            itertools.chain(
                itertools.repeat(self.formLine, len(lines) - 1),
                [self.formLastLine]
            ), lines)
        ]


s = Solution()
print s.fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16)
