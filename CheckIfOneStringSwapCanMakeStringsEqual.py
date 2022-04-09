import collections
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if collections.Counter(s1) != collections.Counter(s2):
            return False
        
        swaps = 0
        for ss1, ss2 in zip(s1,s2):
            if ss1 != ss2:
                swaps += 1
        return swaps == 2 


s = Solution()
print(s.areAlmostEqual('kepl', 'kepl')) # True
print(s.areAlmostEqual('bank', 'bakn')) # True
print(s.areAlmostEqual('bkna', 'bakn')) # False
print(s.areAlmostEqual('attack', 'defend')) # False