class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1, -1, -1):
            # if numbers[i] < target or numbers[i] == 0:
            for j in range(i - 1, -1, -1):
                if numbers[j] < target - numbers[i]:
                    break

                if target - numbers[i] == numbers[j]:
                    return [j + 1, i + 1]