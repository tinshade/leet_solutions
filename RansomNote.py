from collections import Counter
class Solution:
	def canConstruct(self, ransomNote, magazine):
		_ran,_mag={},{}
		for each in ransomNote:
			if each not in _ran:
				_ran[each] = 1
			else:
				_ran[each] += 1
		for each in magazine:
			if each not in _mag:
				_mag[each] = 1
			else:
				_mag[each] += 1
		for each in ransomNote:
			try:
				if _ran[each] > _mag[each]:
					return False
			except:
				return False
		return True

	def pythonicSolution(self, ransomNote, magazine):
		_ran, _mag = Counter(ransomNote), Counter(magazine)
		for each in ransomNote:
			try:
				if _ran[each] > _mag[each]:
					return False
			except:
				return False
		return True
s = Solution()

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(s.canConstruct(ransomNote, magazine)) #118ms
print(s.pythonicSolution(ransomNote, magazine)) #40ms
		