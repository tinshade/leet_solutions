class Solution:
    def countNegatives(self, grid) -> int:
        def helper(arr):
            temp = 0
            for i in range(len(arr)):
                if arr[i] < 0:
                    temp += 1
            
            return temp
        answer = 0
        for i in range(len(grid)):
            answer += helper(grid[i])
        
        return answer
    
    def flatten(self, grid) -> int:
        flat = [num for sublist in grid for num in sublist]
        res = 0
        for i in range(len(flat)):
            if flat[i] < 0:
                res += 1
        
        return res


if __name__ == "__main__":
    s = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(s.countNegatives(grid)) # 8
    print(s.flatten(grid))
    grid = [[3,2],[1,0]]
    print(s.countNegatives(grid)) # 0

    