class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(list)
        
        keys=set(nums)
        for o in keys:
            key=o
            res[key]=0
        for num in nums:
            res[num]+=1
        
        sorted_res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_res.keys())[:k]

     