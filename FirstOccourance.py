class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:(i+len(needle))] == needle:
                return i
        
        return -1




if __name__ == "__main__":
    s = Solution()
    print(s.strStr('sadbousadverysad', 'sad')) # 0
    print(s.strStr('sadbousadverysad', 'asdad')) # -1

