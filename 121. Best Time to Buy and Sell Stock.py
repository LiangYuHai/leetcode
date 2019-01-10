class Solution(object):# Brutal Solution
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max=0
        for i in range(len(prices)-1):
            highest=0
            for j in prices[i+1:]:
                if j>highest:
                    highest=j
            if highest-prices[i]>max:
                max=highest-prices[i]
        return max

# One Pass: O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        max_profit=0
        for day_price in prices:
            if day_price <= min_price:
                min_price=day_price
            else:
                if day_price-min_price>max_profit:
                    max_profit=day_price-min_price
        return max_profit