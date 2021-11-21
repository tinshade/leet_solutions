# Solve using backtracking

class Solution:
	#Exponential solution
	def letterCombinations(self, digits):
		if digits == "":
			return []
		phone_map = {
		"2":'abc',
		"3":'def',
		"4":'hij',
		"5":"klm",
		'6':"nop",
		'7':"qrs",
		'8':"tuv",
		'9':"wxyz",
		}
		res = []
		
		def backtrack(index, substring):
			if len(substring) == len(digits):
				res.append(substring)
				return

			for each in phone_map[digits[index]]:
				backtrack(index+1,substring+each)
		backtrack(0,"")
		return res

s = Solution()
print(s.letterCombinations("23"))