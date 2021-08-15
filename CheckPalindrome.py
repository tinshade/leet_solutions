class Solution:
	def isPlaindrome(self, S):
		# code here
		n = len(S)//2
		for i in range(n):
			if S[i] != S[-i-1] or S[-1-i] != S[i]:
				return 0
				
		return 1



s = Solution()
st = "abba"
print(s.isPlaindrome(st))

st = "abbas"
print(s.isPlaindrome(st))