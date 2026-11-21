class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        digits[n] += 1
        carry = 0
        while n >= 0:
            total = digits[n] + carry
            carry = total // 10
            digits[n] = total % 10
            n -= 1
        
        if carry:
            digits.insert(0, carry)

        return digits