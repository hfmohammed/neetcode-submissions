class Solution {
public:
    std::vector<std::vector<int>> twoSum(std::vector<int>& nums, int target, int skip_idx) {
        std::vector<int>::iterator forward = nums.begin() + skip_idx + 1;
        std::vector<int>::iterator backward = nums.end() - 1;
        std::vector<std::vector<int>> res;

        while (forward < backward) {
            if (*forward + *backward < target) {
                forward++;
            } else if (*forward + *backward > target) {
                backward--;
            } else {
                std::cout << "pushing {" << *forward << ", " << *backward << "}" << std::endl;
                res.push_back({ *forward, *backward });
                forward++;
            }
        }

        return res;
    }

    std::vector<std::vector<int>> threeSum(vector<int>& v) {
        std::sort(v.begin(), v.end());
        for (int i : v) std::cout << i << ", ";
        std::cout << std::endl;

        std::vector<std::vector<int>> answer;
        
        std::vector<int>::iterator it = v.begin(); 
        while (it < v.end()) {
            std::cout << (it - v.begin()) << ", target == " << -(*it) << std::endl;
            std::vector<std::vector<int>> result = twoSum(v, -(*it), it - v.begin());
            
            try {
                std::cout << result.size() << std::endl;
                if (result.size() != 0) {
                    for (vector<int> r : result) {
                        r.insert(r.begin(), *it);
                        
                        if (std::find(answer.begin(), answer.end(), r) == answer.end()) {
                            answer.push_back(r);
                        }
                    }
                }
            } catch (...) {
                std::cout << "Error" << std::endl;
            }

            it++;
        }
        
        return answer;
    }   
};
