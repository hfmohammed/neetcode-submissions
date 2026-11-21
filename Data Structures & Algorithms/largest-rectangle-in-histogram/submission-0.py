class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        
        for idx in range(len(heights)):
            width = 1
            left = idx - 1
            while left >= 0 and heights[left] >= heights[idx]:
                left -= 1
                width += 1
            
            right = idx + 1
            while right < len(heights) and heights[right] >= heights[idx]:
                right += 1
                width += 1
            
            max_area = max(max_area, heights[idx] * width)

        return max_area