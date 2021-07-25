class Solution:	
	def isPalindrome(self, s:str) -> bool:
		n = len(s)
		if n<=1:
			return True
		start, end = 0, len(s)-1
		while start <= end:
			if s[start].isalpha() or s[start].isdigit():
				if s[end].isalpha() or s[end].isdigit():
					if s[start].lower() != s[end].lower():
						return False
					else:
						start+=1
						end-=1
				else:
					end-=1
			else:
				start+=1
		return True






s = Solution()
s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
s3 = 'racecar'
s4 = "ab_a"
print(s.isPalindrome(s2))