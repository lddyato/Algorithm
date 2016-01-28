# -*- coding: utf-8 -*-

'''
String to Integer (atoi)
========================

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given
input specs). You are responsible to gather all the input requirements up
front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your
function signature accepts a const char * argument, please click the reload
button  to reset your code definition.
'''


class Solution(object):
    '''算法思路：

    注意 int 的范围 -2^31 ~ 2^31-1
    '''
    def myAtoi(self, str):
        first, max, min = None, pow(2, 31) - 1, -pow(2, 31)
        for i, c in enumerate(str):
            if not c.isspace():
                first = i
                break

        if first is None or (
                str[first] not in ['-', '+'] and not str[first].isdigit()):
            return 0

        negative = False
        if str[first] == '-':
            negative = True
            first += 1
        elif str[first] == '+':
            first += 1

        end = first
        while end < len(str):
            if not str[end].isdigit():
                break
            end += 1

        if end == first:
            return 0

        end -= 1

        while first <= end and str[first] == '0':
            first += 1

        if first > end:
            return 0

        sum, i = 0, 1
        while end >= first:
            plus = (ord(str[end]) - ord('0')) * i
            if negative and -min - plus < sum:
                return min

            if not negative and max - plus < sum:
                return max

            sum += plus
            i *= 10
            end -= 1

        if negative:
            sum = -sum

        return sum


s = Solution()
print s.myAtoi('-2147483648')
