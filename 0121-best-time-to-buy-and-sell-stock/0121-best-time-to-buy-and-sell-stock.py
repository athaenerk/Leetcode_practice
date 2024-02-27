class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,maxp=0,1,0
        while(l<r and r<len(prices)):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp