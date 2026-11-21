class Solution:
    def findMin(self, nums: List[int]) -> int:
        len_ = len(nums)
        print(len_)
        if len_ == 1:
            return nums[0]
        return min(self.findMin(nums[:int(len_/2)]), self.findMin(nums[int(len_/2):]))
        