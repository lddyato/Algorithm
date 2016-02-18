/*
Two Sum II - Input array is sorted My Submissions Question
==========================================================

Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2. Please note that
your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/

#include "header.h"


class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        int low = 0, high = numbers.size() - 1;
        while (low < high) {
            int s = numbers[low] + numbers[high];
            if (s < target) {
                ++low;
            }
            else if (s > target) {
                --high;
            }
            else {
                return {low + 1, high + 1};
            }
        }
    }
};


int main() {
    Solution s;
    vector<int> v = {1, 2, 4, 8};
    for (auto i : s.twoSum(v, 6)) {
        cout << i << endl;
    }
}
