class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        sol=set()
        for i in range(0, len(nums)):

            target=-nums[i]
            first=i+1
            last=len(nums)-1
            while(first<last):
                if nums[first]+nums[last]==target:
                    sol.add((nums[i],nums[first],nums[last]))
                    first+=1
                    last-=1
                if nums[first]+nums[last]>target:
                    last-=1
                if nums[first]+nums[last]<target:
                    first+=1
    
        return list(sol)
            
        