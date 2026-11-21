class Solution {
public:
    int maxArea(vector<int>& heights) {
        vector<int>::iterator l = heights.begin();
        vector<int>::iterator r = heights.end() - 1;
        int res = 0;
        while (l < r) {
            int temp = (r - l) * std::min(*l, *r);
            res = std::max(res, temp);

            if (*r <= *l) {
                r--;
            } else if (*l < *r) {
                l++;
            }
        }

        return res;
    }
};
