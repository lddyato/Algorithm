# -*- coding: utf-8 -*-

'''
Read N Characters Given Read4 II - Call multiple times
======================================================

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

Note:
The read function may be called multiple times.
'''


class Solution(object):
    '''算法思路：

    要将上次 read4 读取后剩余的保存起来
    '''
    def __init__(self):
        self.left = []

    def read(self, buf, n):
        count, reads = 0, [''] * 4

        if self.left:
            while count < min(n, len(self.left)):
                buf[count] = self.left[count]
                count += 1

            self.left = self.left[count:]

        while count < n:
            size = read4(reads)
            if not size:
                break

            length = min(n - count, size)
            self.left = reads[length : size]

            for i in xrange(length):
                buf[count] = reads[i]
                count += 1

        return count


index = 0
string = 'abcdefg'

def read4(reads):
    global index

    count = 0
    while count < 4 and index < len(string):
        reads[count] = string[index]
        count += 1
        index += 1
    return count


s = Solution()
buf = [0] * 100
print s.read(buf, 3)
print s.read(buf, 4)
print s.read(buf, 3)
