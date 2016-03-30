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
        MAX_INT, MIN_INT = 2**31 - 1, -2**31

        str = str.strip()
        negative = -1 if (str and str[0] == '-') else 1

        i = 0
        if str and str[0] in ['-', '+']:
            i += 1

        r = []
        while i < len(str):
            if str[i].isdigit():
                r.append(int(str[i]))
            else:
                break
            i += 1

        num, base = 0, 1
        for i in range(len(r) - 1, -1, -1):
            if negative == 1 and MAX_INT - base * r[i] <= num:
                return MAX_INT

            if negative == -1 and MAX_INT + 1 - base * r[i] <= num:
                return MIN_INT

            num += base * r[i]
            base *= 10

        return num * negative


s = Solution()
print s.myAtoi('-2147483648')
