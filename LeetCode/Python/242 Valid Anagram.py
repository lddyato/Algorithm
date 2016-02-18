# -*- coding: utf-8 -*-

'''
Valid Anagram
=============

Given two strings s and t, write a function to determine if t is an anagram
of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your
solution to such case?
'''


class Solution(object):
    '''算法思路：

    利用 couting sort 的思想生成 key (或者素数相乘)，然后比较key，
    但是这种算法不适合 unicode

    Time: O(n)
    Space: O(n)
    '''
    def genKey(self, s):
        bits = [0] * 26
        for char in s:
            bits[ord(char) - 97] += 1
        return bits

    def isAnagram(self, s, t):
        return self.genKey(s) == self.genKey(t)


class Solution(object):
    '''算法思路：

    因为是两个，所以记录 s 的各个字符出现的次数，然后再在其基础之上减去 t 各个字符
    出现的个数，如果最后个数全部为 0，则说明 True

    这种算法适用于 unicode，但是不适用于 3个 及以上个数的比较

    Time: O(n)
    Space: O(n)
    '''
    def isAnagram(self, s, t):
        record = {}

        for char in s:
            record[char] = record.get(char, 0) + 1

        for char in t:
            record[char] = record.get(char, 0) - 1

        return not any(record.values())


class Solution(object):
    '''算法思路：

    排序然后比较，这种算法适合 unicode

    Time: O(n*log(n))
    Space: O(1)
    '''
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
