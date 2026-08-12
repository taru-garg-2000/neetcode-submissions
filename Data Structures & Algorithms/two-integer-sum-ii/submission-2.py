import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            idx = bisect.bisect_left(numbers, new_target, i+1, len(numbers)-1)
            if numbers[idx] == new_target:
                return [i+1, idx+1]

        return [-1, -1]

