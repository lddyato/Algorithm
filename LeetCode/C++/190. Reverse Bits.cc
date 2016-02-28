/*
Reverse Bits
============

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as
00000010100101000001111010011100), return 964176192 (represented in binary as
00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
*/


#include "header.h"


class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        auto r = 0;
        for (auto i = 0; i < 32; ++i) {
            r <<= 1;
            r |= n & 1;
            n >>= 1;
        }
        return r;
    }
};


int main() {
    Solution s;
    cout << s.reverseBits(1) << endl;
}
