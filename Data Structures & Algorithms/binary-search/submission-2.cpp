class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = (right - left) / 2;
            std::cout << "left: " << left << ", mid: " << mid << ", right: " << right << std::endl;
            
            if (nums[left + mid] > target) {
                right = left + mid - 1;
            } else if (nums[left + mid] < target) {
                left += mid + 1;
            } else if (nums[left + mid] == target) {
                return left + mid;
            } else {
                return -1;
            }
        }
        return -1;
    }
};
