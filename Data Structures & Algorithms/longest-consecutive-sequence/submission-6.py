class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        numSet = set(nums)
        read = set()

        for i in nums:
            temp_len = 0
            if i - 1 not in numSet:
                while i in numSet and i not in read:
                    read.add(i)
                    temp_len += 1
                    i += 1
                max_len = max(max_len, temp_len)


        return max_len
