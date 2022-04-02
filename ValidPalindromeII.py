class Solution:

	def valid_data(self, payload) -> bool:
		if type(payload) == str and len(payload) > 1:
			return True
		return False

	def validPalindrome(self, s) -> bool:
		'''
		 Checks if a string is palindrome or can be made palindrome by removing atmost one character
		'''

		if not self.valid_data(s):
			return False

		start, end = 0, len(s)-1
		while start<end:
			if s[start] != s[end]:
				left_substring, right_substring = s[start+1:end+1], s[start:end]
				return left_substring == left_substring[::-1] or right_substring == right_substring[::-1]
			start += 1
			end -= 1

		return True


s = Solution()
print(s.validPalindrome('aaba')) #True
print(s.validPalindrome('aabx')) #False
print(s.validPalindrome('aaa')) #True
print(s.validPalindrome('abc')) #False