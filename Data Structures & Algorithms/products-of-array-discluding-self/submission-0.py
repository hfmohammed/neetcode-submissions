class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        len_nums = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[idx - 1] * nums[idx - 1])
            len_nums += 1
        
        postfix = []
        for idx in range(len_nums - 1, -1, -1):
            if idx == len_nums - 1:
                postfix.append(1)
            else:
                postfix.append(postfix[len_nums - idx - 2] * nums[idx + 1])

        res = []
        for idx in range(len_nums):
            res.append(prefix[idx] * postfix[len_nums - idx - 1])

        [print(i) for i in prefix]
        [print(i) for i in postfix]
        [print(i) for i in res]

        return res