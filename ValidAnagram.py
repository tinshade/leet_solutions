class Solution:
	def isAnagram(self, s, t):
		s = sorted(s)
		t = sorted(t)
		return True if s == t else False
	def alternative(self,s,t):
		from collections import Counter
		s = Counter(s)
		t = Counter(t)
		return True if s == t else False
s=Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))
print(s.alternative(s = "anagram", t = "nagaram"))