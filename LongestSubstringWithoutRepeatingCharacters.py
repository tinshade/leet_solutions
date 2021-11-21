# Optimal solution is to use the Sliding Window technique
# Use sliding window techniques for problems like finding the max sum of any contiguous subarray of size "k"
class Solution:
	def lengthOfLongestSubstring(self,s):
		uniques = set()
		start=end=result = 0
		while end < len(s):
			while s[end] in uniques:
				uniques.remove(s[start])
				start+=1
			uniques.add(s[end])
			result = max(result, end - start+1)
			end += 1
		return result


s = Solution()
print(s.lengthOfLongestSubstring("pwwkekkew")) #3 -> wke | kew