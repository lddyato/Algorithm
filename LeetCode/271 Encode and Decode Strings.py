# -*- coding: utf-8 -*-

'''
Encode and Decode Strings
=========================

Design an algorithm to encode a list of strings to a string. The encoded string
is then sent over the network and is decoded back to the original list of
strings.

Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }

Machine 2 (receiver) has the function:

    vector<string> decode(string s) {
      //... your code
      return strs;
    }

So Machine 1 does:

    string encoded_string = encode(strs);

and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
- The string may contain any possible characters out of 256 valid ascii
  characters. Your algorithm should be generalized enough to work on any
  possible characters.
- Do not use class member/global/static variables to store states. Your encode
  and decode algorithms should be stateless.
- Do not rely on any library method such as eval or serialize methods. You
  should implement your own encode/decode algorithm.
'''


class Codec(object):
    '''算法思路：

    长度充当前缀
    '''
    def encode(self, strs):
        return ''.join('{}:{}'.format(len(s), s) for s in strs)

    def decode(self, s):
        r, i = [], 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            r.append(s[j + 1:i])
        return r


codec = Codec()
print codec.decode(codec.encode(['"hello']))
