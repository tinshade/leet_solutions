from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = []
        for each in Counter(arr).values():
          if each not in seen:
            seen.append(each)
          else:
            return False
        return True


s = Solution()
s.uniqueOccurrences([1,2,2,1,1,3])