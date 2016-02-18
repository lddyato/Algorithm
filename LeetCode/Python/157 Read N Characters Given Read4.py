# -*- coding: utf-8 -*-

'''
Read N Characters Given Read4
=============================

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that
reads n characters from the file.

Note:
The read function will only be called once for each test case.
'''


class Solution(object):
    '''算法思路：

    这一题问题有点不明确，read4 和 read 里边的参数是读取的结果
    '''
    def read(self, buf, n):
        count, readed = 0, [''] * 4
        while count < n:
            size = read4(readed)
            if not size:
                break

            size = min(size, n - count)
            for i in xrange(size):
                buf[count] = readed[i]
                count += 1

        return count
