class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        cur,maxcount=0,0
        for n in nums:
            count[n]=1+count.get(n,0)
            cur=n if count[n]>maxcount else cur
            maxcount=max(count[n], maxcount)
        return cur        