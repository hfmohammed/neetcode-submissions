class Solution:
    def isHappy(self, n: int) -> bool:
        _seen = set()

        while n not in _seen:
            if n == 1:
                return True

            _seen.add(n)
            _sum = 0
            while n:
                rem = n % 10
                n = n // 10

                _sum += rem ** 2

            n = _sum            
        
        return False