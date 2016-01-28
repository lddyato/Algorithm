# -*- coding: utf-8 -*-

'''
Shortest Word Distance
======================

Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are
both in the list.
'''


class Solution(object):
    '''算法思路:

    分别记录上次 word1, word2 出现的地方
    '''
    def shortestDistance(self, words, word1, word2):
        last_word1, last_word2, distance = None, None, len(words)

        for i, w in enumerate(words):
            if w == word1:
                if last_word2 is not None and i - last_word2 < distance:
                    distance = i - last_word2
                last_word1 = i

            if w == word2:
                if last_word1 is not None and i - last_word1 < distance:
                    distance = i - last_word1
                last_word2 = i

        return distance


s = Solution()
print s.shortestDistance(["practice", "makes"], 'makes', 'practice')
