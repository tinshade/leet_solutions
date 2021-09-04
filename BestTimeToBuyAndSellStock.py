class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 999999999999
        res = 0
        for index, value in enumerate(prices):
            if value < max_profit:
                max_profit = value
            elif value > max_profit:
                res = max(res,value-max_profit)
        return res


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
