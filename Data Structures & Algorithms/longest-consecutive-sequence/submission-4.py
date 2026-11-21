class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_val = 0

        for i in nums.copy():
            if i - 1 not in nums:
                max_temp = 0
                while i + max_temp in nums:
                    nums.remove(i + max_temp)
                    max_temp += 1
                
                max_val = max(max_val, max_temp)
        
        return max_val
        
