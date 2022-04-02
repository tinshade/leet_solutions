class Solution:
    def reverseVowels(self, s) -> str:
        s = list(s)
        vowels = {'a':10, 'e' : 1, 'i':2, 'o':3, 'u':4}
        l,r=0,len(s)-1
        while l < r:
            if vowels.get(s[l].lower()):
                if vowels.get(s[r].lower()):
                    s[l], s[r] = s[r], s[l]
                    l+=1
                    r-=1
                else:
                    r-=1
            else:
                l+=1

        return ''.join(s)







s = Solution()

print(s.reverseVowels("hello")) #holle
print(s.reverseVowels("leetcode")) #leotcede
print(s.reverseVowels("ai")) #ia
print(s.reverseVowels("aA")) #Aa