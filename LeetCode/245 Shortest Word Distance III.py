# -*- coding: utf-8 -*-

'''
Shortest Word Distance III
==========================

This is a follow up of Shortest Word Distance. The only difference is now
word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in
the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
'''


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        distance = len(words)

        if word1 != word2:
            last_word1, last_word2 = None, None
            for i, w in enumerate(words):
                if w == word1:
                    if last_word2 is not None and i - last_word2 < distance:
                        distance = i - last_word2
                    last_word1 = i

                if w == word2:
                    if last_word1 is not None and i - last_word1 < distance:
                        distance = i - last_word1
                    last_word2 = i
        else:
            last = None
            for i, w in enumerate(words):
                if w == word1:
                    if last is not None and i - last < distance:
                        distance = i - last
                    last = i

        return distance