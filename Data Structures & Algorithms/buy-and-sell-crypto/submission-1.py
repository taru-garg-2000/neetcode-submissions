class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        _min_price = float('inf')

        for price in prices:
            max_profit = max(price - _min_price, max_profit)
            _min_price = min(_min_price, price)

        return max_profit