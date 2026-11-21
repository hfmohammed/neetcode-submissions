class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            val = x
            k = n
            if n < 0:
                k = abs(n)

            while k > 1:
                val = val * x
                k -= 1

            if n < 0:
                val = 1/val

        return val