from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i<len(s):
            if j < len(t):

                if s[i] == t[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                return False
        
        return True
        


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence('abc', 'aasdvbasasc')) # True
    print(s.isSubsequence('abc', 'xyc')) # False
    print(s.isSubsequence('acb', 'abc')) # False