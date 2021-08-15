class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i],s[-1 - i] = s[-i-1], s[i]

        print(s)

        






s = Solution()
arr = ["h","e","l","l","o"]
s.reverseString(arr)

arr = ["H","a","n","n","a","h"]
s.reverseString(arr)