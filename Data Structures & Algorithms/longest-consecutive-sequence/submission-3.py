class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        data = {k : 1 for k in nums}

        for i in nums: 
            print(data)
            k = i - 1
            print(i)
            while (k in nums):
                data[k] = data[k + 1] + 1
                k -= 1
            print(data)
        
        res = 0
        for i in data:
            res = max(res, data[i])
        
        return res
        
