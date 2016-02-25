/*
Two Sum
=======

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above
updated description carefully.
*/

#include "header.h"


// 利用哈希
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> record;

        for (auto i = 0; i < nums.size(); ++i) {
            auto item = record.find(target - nums[i]);
            if (item != record.end()) {
                return {item->second, i};
            }

            record[nums[i]] = i;
        }
    }
};


int main() {
    Solution s;
    vector<int> v = {5, 1, 2, 3, 5};

    for (auto i : s.twoSum(v, 10)) {
        cout << i << endl;
    }
}
