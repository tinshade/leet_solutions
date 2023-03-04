class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = ""
        
        for i in range(len(s)):
            #odd length palindromes
            l,r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    res = s[l:r+1]
                    length = r-l+1
                #Expanding outward
                l -= 1
                r += 1
            #even length palindromes
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    res = s[l:r+1]
                    length = r-l+1
                #Expanding outward
                l -= 1
                r += 1
        return res