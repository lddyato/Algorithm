/*
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of
all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
*/

#include "header.h"


class Solution {
public:
    unsigned countZero(int num, int k) {
        auto cycles = num >> k + 1, mask = 1 << k;
        num &= (1 << k + 1) - 1;
        return cycles * mask + ((num & mask) ? mask : (num + 1));
    }

    int rangeBitwiseAnd(int m, int n) {
        auto r = 0, mask = 1;
        for (auto i = 0; i < 31; ++i) {
            if (countZero(n, i) - countZero(m - 1, i) == 0) {
                r |= mask;
            }
            mask <<= 1;
        }
        return r;
    }
};


int main() {
    Solution s;
    cout << s.rangeBitwiseAnd(0, 1) << endl;
}
