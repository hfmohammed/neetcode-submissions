class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                c = maxLeft - height[left]
                res += max(c, 0)

            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                c = maxRight - height[right]
                res += max(c, 0)
        
        return res


