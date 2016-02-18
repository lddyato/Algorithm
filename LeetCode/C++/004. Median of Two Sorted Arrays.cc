/*
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find
the median of the two sorted arrays. The overall run time complexity should be
O(log (m+n)).
*/

#include "header.h"


// 先 merge，再找中位数，O(n)
class Solution {
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        vector<int> nums;
        auto i = 0, j = 0;

        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                nums.push_back(nums1[i]);
                ++i;
            } else {
                nums.push_back(nums2[j]);
                ++j;
            }
        }

        for (; i < nums1.size(); ++i) {
            nums.push_back(nums1[i]);
        }

        for (; j < nums2.size(); ++j) {
            nums.push_back(nums2[j]);
        }

        auto n = nums.size(), mid = n >> 1;
        return n & 1 ? nums[mid] : (nums[mid] + nums[mid - 1]) / 2.0;
    }
};


int main() {
    Solution s;
    vector<int> nums1 = {1, 2, 3}, nums2 = {4, 5, 9};

    cout << s.findMedianSortedArrays(nums1, nums2) << endl;
}