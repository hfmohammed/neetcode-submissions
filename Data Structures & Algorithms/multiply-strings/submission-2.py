class Solution:
    def add(self, nums) -> int:
        res = [0]
        k = 0
        carry = 0
        while nums:
            l = 0
            while l < len(nums):
                if len(nums[l]) < k + 1:
                    nums.pop(l)
                    l -= 1
                else:
                    res[k] += nums[l][k]
                l += 1
            
            total = res[k] + carry
            res[k] = total % 10
            carry = total // 10

            k += 1
            res.append(0)

        total = res[k] + carry
        res[k] = total % 10
        carry = total // 10

        print(res)
        o = 0
        for i in res[::-1]:
            o = o * 10 + i
        return o

    def multiply(self, num1: str, num2: str) -> str:
        res = []
        num1, num2 = num1[::-1], num2[::-1]
        
        n = 0
        for i in num2:
            temp = []
            for j in range(n):
                temp.append(0)

            for j in num1:
                temp.append(int(i)*int(j))

            n += 1
            res.append(temp)
        
        print(res)
        return str(self.add(res))