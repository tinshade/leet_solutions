from collections import Counter as c
class Solution:
	def findTheDifference(self, s, t):
		ascii_t=0
		for i in range(len(t)):
			ascii_t += ord(t[i])
		for i in range(len(s)):
			ascii_t -= ord(s[i])
		return chr(ascii_t)






sol = Solution()
print(sol.findTheDifference('baa', 'baeaa'))#e
print(sol.findTheDifference('', 'y')) #y
print(sol.findTheDifference('abcd', 'abcde')) #e
print(sol.findTheDifference('a', 'aa')) #a
print(sol.findTheDifference('ae', 'aea')) #a