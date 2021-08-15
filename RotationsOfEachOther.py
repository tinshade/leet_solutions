class Solution:
	def areRotations(self, str1, str2):
		if len(str1) != len(str2):
			return False
		temp = str1*2
		if str2 in temp:
			return True
		return False



s = Solution()

s1 = "ABCD"
s2 = "CDAB"
print(s.areRotations(s1,s2)) #True

s1 = "ABCD"
s2 = "ACBD"
print(s.areRotations(s1,s2)) #False