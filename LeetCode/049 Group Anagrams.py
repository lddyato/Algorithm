# -*- coding: utf-8 -*-

'''
Group Anagrams
==============

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
- For the return value, each inner list's elements must follow the
  lexicographic order.
- All inputs will be in lower-case.
'''

'''
利用 hash，每个字符串可以生成一个 key，然后把相同 key 的字符串放在一起

有多种生成 key 的方法
  - 用数组，里边每项代表对应字符出现的次数，比如 '00000000000000000012030000001'
  - sorted(word)
  - countingSort(word)
  - 26个字母对应26个素数，相乘（容易 overflow）

综上，第 4 种方法最快，但是容易overflow，次之是自带的 sorted，最差的是剩下的两种方法
'''

class Solution(object):
    def groupAnagrams(self, strs):
        record = {}

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1

            key = ''.join(map(str, key))
            record.setdefault(key, []).append(word)

        return map(sorted, record.values())


class Solution(object):
    def groupAnagrams(self, strs):
        record = {}

        for word in strs:
            key = ''.join(sorted(word))
            record.setdefault(key, []).append(word)

        return map(sorted, record.values())


class Solution(object):
    def groupAnagrams(self, strs):
        record = {}

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1
            key = ''.join([chr(97 + i) * v for i, v in enumerate(key)])
            record.setdefault(key, []).append(word)

        return map(sorted, record.values())


class Solution(object):
    def groupAnagrams(self, strs):
        record = {}
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101
        ]

        for word in strs:
            key = reduce(
                lambda x, y: x * y, [primes[ord(c) - 97] for c in word], 1)
            record.setdefault(key, []).append(word)

        return map(sorted, record.values())


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
