class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            curr = 0
            if num - 1 not in nums:
                curr = 1
                l = 1
                while num + l in nums:
                    curr += 1
                    l += 1
            longest = max(curr, longest)

        return longest