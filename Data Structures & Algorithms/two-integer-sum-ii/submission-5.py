class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i, val in enumerate(numbers):
            diff = target - val
            if diff in map:
                return [map[diff]+1, i+1]
            map[val] = i
        return []