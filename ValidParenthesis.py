class Solution:
    def isValid(self, s: str) -> bool:
      pairs = {"{":"}", "(":")", "[":"]"}
      stack = []
      if len(s) <= 1:
          return False
      for i in range(len(s)):
          if s[i] in pairs.keys():
              stack.append(s[i])
          else:
              if len(stack) == 0:
                  return False
              else:
                  if pairs[stack.pop()] != s[i]:
                      return False
      if len(stack) == 0:
          return True
      else:
          return False


s = Solution()
print(s.isValid('[(])'))