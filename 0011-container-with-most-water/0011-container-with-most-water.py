class Solution:
    def maxArea(self, height: List[int]) -> int:
        first=0
        last=len(height)-1
        sol=0
        while(first<last):
            area=(last-first)*min(height[first], height[last])
            sol=max(area,sol)
            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        return sol

        

        