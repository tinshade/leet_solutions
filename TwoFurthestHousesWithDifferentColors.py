class Solution:
    def maxDistance(self, colors: [int]) -> int:
        n = len(colors)
        if n == 2 and colors[0] == colors[1]:
            return 1
        
        def helper(n, colors)->int:
            color1 = colors[0]
            index = 0
            curr_max = 0
            for i in range(1, n):
                if colors[i] != color1:
                    difference = i - index 
                    curr_max = max(curr_max, difference)
            
            return curr_max
        return max(helper(n, colors),helper(n, colors[::-1]))


if __name__ == "__main__":
    s = Solution()
    print(s.maxDistance([4,4,4,11,4,4,11,4,4,4,4,4])) # 8
    print(s.maxDistance([1,1,1,6,1,1,1])) # 3