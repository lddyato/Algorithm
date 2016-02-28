/*
Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
*/

#include "header.h"


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        auto r = 0, k = 3;
        for (auto i = 0; i < 32; ++i) {
            auto mask = 1 << i, cnt = 0;

            for (auto num : nums)
                cnt += bool(num & mask);

            if (cnt % k)
                r |= mask;
        }
        return r;
    }
};


int main() {
    Solution s;
    vector<int> v = {-3, -3, -3, -100};
    cout << s.singleNumber(v) << endl;
}