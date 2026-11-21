class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::vector<int>::iterator forward = numbers.begin();
        std::vector<int>::iterator backward = numbers.end() - 1;

        vector<int> result(2);
        while (forward < backward) {
            if (*backward + *forward > target) {
                backward--;
            }
            if (*backward + *forward < target) {
                forward++;
            }

            if (*backward + *forward == target) {
                return vector<int>{forward - numbers.begin() + 1, backward - numbers.begin() + 1};
            }
        }
    }
};
