class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> counts;
        for (int item : nums) {
            if (counts.find(item) == counts.end()) {
                counts[item] = 0;
            } else {
                return true;
            }
            cout << item << endl;
        } return false;
    }
};