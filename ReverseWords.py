class Solution:
    def reverseWords(self, s):
        def reverseString(st):
            start, end=0,len(st)-1
            while start<end:
              st[start],st[end] = st[end],st[start]
              start+=1
              end-=1
            return ''.join(st)
        s = s.split(' ')
        print(s)
        for i in range(len(s)):
            print(s[i])
            s[i] = reverseString(list(s[i]))
        print(s)
        return ' '.join(s)
    def pythonic(self, s):
        s = s.split(' ')
        for i in range(len(s)):
          s[i] = s[i][::-1]
        return (' '.join(s))

s = Solution()
print(s.reverseWords('God Ding'))
print(s.pythonic('God Ding'))


        