class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for i in nums:
            if i not in num_count:
                num_count[i] = 0
            num_count[i] += 1
        
        sorted_items = sorted(num_count.items(), key=lambda item: item[1], reverse=True)

        return [i[0] for i in sorted_items[:k]]