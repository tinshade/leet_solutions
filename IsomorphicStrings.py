class Solution:
	def isIsomorphic(self, s, t):
		hashmap = {}
		for i in range(len(s)):
			if s[i] not in hashmap:
				if t[i] in hashmap.values():
					return False
				hashmap[s[i]] = t[i]
			else:
				if hashmap[s[i]] != t[i]:
					return False
		return True

sol=Solution()


s="badc"
t="baba"
print(sol.isIsomorphic(s,t)) #False

s="egg"
t="add"
print(sol.isIsomorphic(s,t)) #True

s="foo"
t="bar"
print(sol.isIsomorphic(s,t)) #False


s="paper"
t="title"
print(sol.isIsomorphic(s,t)) #True