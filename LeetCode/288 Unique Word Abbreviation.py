# -*- coding: utf-8 -*-

'''
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation
is unique in the dictionary. A word's abbreviation is unique if no other word
from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
'''


class ValidWordAbbr(object):
    '''算法思路：

    此题容易很容易误解，需要注意的是

    - 长度 < 3 的 word 是没有 abbreviation 的
    - 查询的 word1 `在` 给的 dictionary 中，且 dictionary 还有其他 word2 与 word1
      的 abbreviation 相同，则不是 unique
    - 查询的 word1 `不在` 给的 dictionary 中，但是 dictionary 有其他 word2 与
      word1 的 abbreviation 相同，则不是 unique
    '''
    def __init__(self, dictionary):
        self.record = {}

        for word in dictionary:
            abb = self.getAbb(word)
            if word == abb:
                continue

            [self.record.update({w: self.record.get(w, 0) + 1})
             for w in (word, abb)]

    def getAbb(self, word):
        return word if len(word) < 3 else '{}{}{}'.format(
            word[0], len(word) - 2, word[-1])

    def isUnique(self, word):
        abb = self.getAbb(word)
        return not (
            word in self.record and self.record[abb] > 1 or
            word not in self.record and abb in self.record)


vwa = ValidWordAbbr(['hello'])
print vwa.isUnique('hello')
