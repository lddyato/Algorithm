# -*- coding: utf-8 -*-

'''
Flip Game II
============

You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip two consecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee
a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
'''


class Solution(object):
    '''算法思路：

    容易让人误解的一个地方是，`guarantee a win` 指的是所有情况中有一个 win 则 return
    True，而不是 `guarantee win`(不管对方怎么走，对方都是输)
    '''
    def canWin(self, s):
        return any(
            s[i:i+2] == '++' and
            not self.canWin('{}--{}'.format(s[:i], s[i+2:]))
            for i in xrange(len(s) - 1))


s = Solution()
print s.canWin('++++++--++')
