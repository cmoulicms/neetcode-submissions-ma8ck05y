class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # should be 1-indexed
        # space complexity should be O(1)
        # not use the same element twice
        left, right = 0, len(numbers) -1 

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]
        return []