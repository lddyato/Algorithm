# -*- coding: utf-8 -*-

'''
Longest Substring Without Repeating Characters
==============================================

Given a string, find the length of the longest substring without repeating
characters. For example, the longest substring without repeating letters for
"abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
'''


class Solution(object):
    '''算法思路：

    用 hash {char: index} 记录已经被访问的字符，当当前字符 char 已经在 hash 里边时，
    以 hash[char] 后一位为起点，继续找下一位
    '''
    def lengthOfLongestSubstring(self, s):
        record_tuple = [(v, i) for i, v in enumerate(s)]

        record, i, count, longest = {}, 0, 0, 0
        while i < len(s):
            current = s[i]

            if current not in record:
                count += 1
                record[current] = i
            else:
                longest = max(count, longest)
                count = i - record[current]
                record = dict(record_tuple[record[current] + 1 : i + 1])
            i += 1

        return max(count, longest)



class Solution(object):
    '''算法思路：

    设置一个 start 代表当前 substr 的起点，会发现当当前 char 是重复字母时，肯定有
    record[char] >= start

    根据上述规律就不用每次遇到重复数字时重新生成 record 了，而且也不会占用额外空间
    record_tuple 了
    '''
    def lengthOfLongestSubstring(self, s):
        i, start, count, longest, record = 0, 0, 0, 0, {}
        while i < len(s):
            current = s[i]
            if current not in record or record[current] < start:
                count += 1
            else:
                longest = max(count, longest)
                count = i - record[current]
                start = record[current] + 1

            record[current] = i
            i += 1

        return max(count, longest)


s = Solution()
print s.lengthOfLongestSubstring('baccabcdefg')
