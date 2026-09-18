class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = sorted(s)
        g = sorted(t)

        if(r == g):
            return True
           

        else:
            return False

obj = Solution()

print(obj.isAnagram("race", "care"))  # True
print(obj.isAnagram("rat", "car"))    # False
            