class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                for k in range(j - 1, -1, -1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res_temp = [nums[k], nums[j], nums[i]]
                        print(res_temp)
                        if res_temp not in res:
                            res.append(res_temp)

        return list(res)