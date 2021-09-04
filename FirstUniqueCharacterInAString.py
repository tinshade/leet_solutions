from collections import Counter as c
class Solution:
	def firstUniqChar(self,s):
        for key,value in c(s).items():
            if value == 1:
                return s.index(key)
        return -1


s = Solution()
print(s.firstUniqChar('leetcode')) #0
print(s.firstUniqChar('loveleetcode')) #2
print(s.firstUniqChar('aabb')) #-1