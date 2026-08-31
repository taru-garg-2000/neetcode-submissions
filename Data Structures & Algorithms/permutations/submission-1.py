import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()

        def rec(curr):
            if len(curr) == len(nums):
                ans.append(copy.deepcopy(curr))

            for num in nums:
                if num not in visited:
                    curr.append(num)
                    visited.add(num)
                    rec(curr)
                    visited.remove(num)
                    curr.pop()

        temp = []
        rec(temp)
        return ans