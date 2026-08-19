class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        mn = [prices[0]]
        for i in range(1, len(prices)):
            if prices[i]>mn[-1]:
                if prices[i]-mn[-1]> profits[-1]:
                    profits.append(prices[i]-mn[-1])
                else:
                    profits.append(profits[-1])
            else:
                profits.append(profits[i-1])
                if mn[-1]>prices[i]:
                    mn.append(prices[i])
                else:
                    mn.append(mn[-1])
        return profits[-1]