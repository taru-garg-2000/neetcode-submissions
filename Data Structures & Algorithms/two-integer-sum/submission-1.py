class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()

        for i, num in enumerate(nums):
            if m.get(target - num, None) is not None:
                return [m[target - num], i]
            m[num] = i

        return [-1, -1]