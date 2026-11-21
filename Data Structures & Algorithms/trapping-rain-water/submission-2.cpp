class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left_maxes;
        vector<int> right_maxes;
        vector<int> areas;
        int res = 0;
        
        left_maxes.push_back(height.front());
        for (auto it = height.begin() + 1; it < height.end(); it++) {
            left_maxes.push_back(std::max({left_maxes.back(), *it}));
        }

        right_maxes.push_back(height.back());
        for (auto it = height.end() - 2; it >= height.begin(); it--) {
            right_maxes.push_back(std::max({right_maxes.back(), *it}));
        }

        areas.push_back(0);
        int last_push = 0;
        for (auto it = height.begin() + 1; it < height.end(); it++) {
            std::cout << left_maxes[it - height.begin()] << "==?" << right_maxes[right_maxes.size() - 1 - (it - height.begin())] << std::endl;
            int min_amount = std::min(
                    left_maxes[it - height.begin()],
                    right_maxes[right_maxes.size() - 1 - (it - height.begin())]
                ) - *it;
            
            if (min_amount == 0) {
                areas.push_back(0);
                continue;
            }
            
            last_push += min_amount;
            areas.push_back(last_push);
        }

        for (auto it = areas.begin(); it < areas.end(); it++) {
            std::cout << *it << ", ";
        }
        std::cout << std::endl;

        return last_push;
    }
};
