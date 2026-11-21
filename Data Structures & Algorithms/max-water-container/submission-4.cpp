class Solution {
public:
    int maxArea(vector<int>& heights) {
        vector<int>::iterator l = heights.begin();
        vector<int>::iterator r = heights.end() - 1;
        int res = 0;
        while (l < r) {
            res = std::max(res, static_cast<int>(r - l) * std::min(*l, *r));

            if (*r <= *l) {
                r--;
            } else if (*l < *r) {
                l++;
            }
        }

        return res;
    }
};
