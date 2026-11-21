class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1, mid = 0;
        int index_0 = nums[0];

        while (left <= right) {
            mid = left + (right - left) / 2;
            cout << "left: " << left << " mid: " << mid << " right: " << right << endl;

            if (nums[mid] >= nums[left]) {
                if (target == nums[mid]) {
                    return mid;
                }

                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else if (nums[left] > target || target > nums[mid]) {
                    left = mid + 1;
                } else {
                    return -1;
                }

            } else {
                if (target == nums[mid]) {
                    return mid;
                }

                if (nums[left] <= target || target < nums[mid]) {
                    right = mid - 1;
                } else if (nums[mid] < target || target <= nums[right]) {
                    left = mid + 1;
                } else {
                    return -1;
                }
            }

        }

        return -1;
    }
};
