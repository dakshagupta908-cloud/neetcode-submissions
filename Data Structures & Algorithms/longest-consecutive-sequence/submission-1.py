class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = sorted(nums)

        if not r:
            return 0

        c = 1
        longest = 1

        for i in range(1, len(r)):
            if r[i] == r[i - 1] + 1:
                c += 1
                longest = max(longest, c)

            elif r[i] == r[i - 1]:
                continue

            else:
                c = 1

        return longest