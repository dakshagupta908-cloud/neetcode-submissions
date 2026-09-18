class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = sorted(nums)
        count = {}

        # Count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort numbers by frequency
        arr = list(count.keys())
        arr.sort(key=lambda x: count[x], reverse=True)

        return arr[:k]
            