# -*- coding: utf-8 -*-

'''
Valid Number
============

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should
gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your
function signature accepts a const char * argument, please click the reload
button  to reset your code definition.
'''

import re


class Solution(object):
    '''算法思路：

    使用正则表达式，也可以自己一个一个字符地判断

    - 整数：r'^[+-]?\d+$'
    - 浮点数：r'^[+-]?((\d*\.\d+)|(\d+\.\d*))$'
    - 科学计数法：r'^[+-]?((\d*\.\d+)|(\d+(\.\d*)?))[eE][+-]?\d+$'

    把他们结合起来就是：r'^[+-]?((\d*\.\d+)|(\d+(\.\d*)?))([eE][+-]?\d+)?$'
    '''
    regex = re.compile(r'^[+-]?((\d*\.\d+)|(\d+(\.\d*)?))([eE][+-]?\d+)?$')

    def isNumber(self, s):
        return bool(self.regex.match(s.strip()))


s = Solution()
print s.isNumber('0000')
