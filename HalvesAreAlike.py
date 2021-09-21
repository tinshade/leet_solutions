class Solution:
	def halvesAreAlive(self,s):
		vowels = {'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
		l=len(s)//2
		h1, h2 = s[:l],s[l:]
		vh1,vh2 = 0,0
		for i in range(len(h1)):
			if h1[i] in vowels:
				vh1+=1
			if h2[i] in vowels:
				vh2 += 1
		if vh1 == vh2:
			return True
		return False
		

sol = Solution()
print(sol.halvesAreAlive('textbook')) #False
print(sol.halvesAreAlive('book')) #True
print(sol.halvesAreAlive('MerryChristmas')) #False
print(sol.halvesAreAlive('AbCdEfGh')) #True