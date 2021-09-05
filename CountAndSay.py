class Solution:
	def countAndSay(self, n):
		output = '1'
		def recur(string):
			result, i = '',0
			while i < len(string):
				count = 1
				while i+1<len(string) and string[i] == string[i+1]:
					i+=1
					count +=1
				result += str(count)+string[i]
				i+=1
			return result
		while n != 1:
			output = recur(output)
			n-=1
		return output


s=Solution()
print(s.countAndSay(4)) #1211