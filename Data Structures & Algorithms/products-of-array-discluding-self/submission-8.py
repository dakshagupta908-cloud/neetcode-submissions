class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        o = [1] * n

        left = 1
        for i in range(n):
            o[i]  = left
            left *= nums[i]

        r = 1
        for j in range(n - 1,-1,-1):
            o[j] *= r
            r *= nums[j]

        return o