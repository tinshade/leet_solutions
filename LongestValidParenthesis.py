class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not len(s):
            return 0
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack and stack[-1]!=-1 and s[stack[-1]] == "(":
                    stack.pop()
                    ans = max(ans,i - stack[-1])
                else:
                    stack.append(i)
        return ans







if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()")) # 2
    print(s.longestValidParentheses(")()())")) # 4
    print(s.longestValidParentheses("")) # 0 
    print(s.longestValidParentheses('(){}[]')) # 2