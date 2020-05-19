"""
https://leetcode.com/problems/online-stock-span/

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
"""

class StockSpanner:

    def __init__(self):
        self.arr = []
        self.index = 0

    def next(self, price: int) -> int:
        count = 1
        
        while(self.arr and self.arr[-1][0] <= price):
            count += self.arr.pop()[1]
            
        self.arr.append([price, count])            
        self.index += 1
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)