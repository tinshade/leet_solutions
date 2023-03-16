class Solution:
    def maximumValue(self, strs) -> int:
        curr_max = 0
        for i in range(len(strs)):
            if strs[i].isdigit():
                curr_max = max(curr_max, int(strs[i]))
            else:
                curr_max = max(curr_max, len(strs[i]))
        
        return curr_max


if __name__ == "__main__":
    s = Solution()
    print(s.maximumValue(["alic3","bob","3","4","00000"])) # 5
    print(s.maximumValue(["1","01","001","0001"])) # 1