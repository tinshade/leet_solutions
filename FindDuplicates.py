class Solution:
	def findDuplicates(self, s):
		occourances = {}
		for i in range(len(s)):
			if s[i] in occourances.keys():
				occourances[s[i]] += 1
			else:
				occourances[s[i]] = 1
		for key,val in occourances.items():
			if val > 1:
				print(f"{key}: count={val}")



s = Solution()
st = "geek"
s.findDuplicates(st)
st = "test string"
s.findDuplicates(st)