# include "header.h"


class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> r;
        sort(nums.begin(), nums.end());
        auto n = int(pow(2, nums.size()));

        for (auto i = 0; i < n; ++i) {
            vector<int> subset;
            auto x = i, j = 0;

            while (x) {
                if (x & 1) subset.push_back(nums[j]);
                ++j;
                x >>= 1;
            }
            r.push_back(subset);
        }
        return r;
    }
};


int main() {
    Solution s;
    vector<int> v = {1, 2, 3};
    auto r = s.subsets(v);

    for (auto i = r.begin(); i != r.end(); ++i) {
        auto array = *i;
        for (auto j = array.begin(); j != array.end(); ++j) {
            cout << *j << endl;
        }
        cout << "------------------" << endl;
    }
}
