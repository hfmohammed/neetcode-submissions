class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::vector<int>::iterator forward = numbers.begin();
        std::vector<int>::iterator backward = numbers.end() - 1;

        while (forward < backward) {
            if (*backward + *forward > target) backward--;
            else if (*backward + *forward < target) forward++;
            else return vector<int>{forward - numbers.begin() + 1, backward - numbers.begin() + 1};
        }
    }
};
