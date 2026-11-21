class Solution:
    def rob(self, nums: List[int]) -> int:
        def r(nums):
            dp = {}
            def best(nm):
                if nm < 0:
                    return 0
                
                if nm not in dp:
                    dp[nm] = max(nums[nm] + best(nm - 2), best(nm - 1))

                return dp[nm]

            return best(len(nums) - 1)

        if len(nums) == 1:
            return nums[0]
        return max(r(nums[1:]), r(nums[:-1]))