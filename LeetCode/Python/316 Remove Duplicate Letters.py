# -*- coding: utf-8 -*-

'''
Remove Duplicate Letters
========================

Given a string which contains only lowercase letters, remove duplicate letters
so that every letter appear once and only once. You must make sure your result
is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''


class Solution(object):
    '''算法思路：

    用栈来表示当前最小的组合
    - 当下一个字符已经在栈中，则舍弃该字符，因为该字符对改变最小组合于事无补
    - 当下一个字符不在栈中，则从栈顶一直 pop 直到栈顶的字符小于当前字符或者栈顶字符
      是最后一个
    '''
    def removeDuplicateLetters(self, s):
        maps, records = {chr(i): i - 97 for i in xrange(97, 123)}, [0] * 26
        for c in s:
            records[maps[c]] += 1

        stack, inStack = [], [False] * 26
        for c in s:
            if inStack[maps[c]]:
                records[maps[c]] -= 1
                continue

            while stack and c <= stack[-1] and records[maps[stack[-1]]] > 0:
                inStack[maps[stack[-1]]] = False
                stack.pop()

            inStack[maps[c]] = True
            stack.append(c)
            records[maps[c]] -= 1

        return ''.join(stack)


ss = Solution()
print ss.removeDuplicateLetters("ccacbaba")
