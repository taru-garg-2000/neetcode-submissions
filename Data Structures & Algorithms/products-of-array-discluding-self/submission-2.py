class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for i in range(1,len(nums)):
            prefix[i] *= (prefix[i-1]*nums[i-1])
            suffix[len(nums)-i-1] *= (suffix[len(nums)-i]*nums[len(nums)-i])

        return [x*y for x, y in zip(prefix, suffix)]
