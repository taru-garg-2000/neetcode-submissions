class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        
        for i, num in enumerate(nums):
            if i > 0:
                ans ^= num

        return ans