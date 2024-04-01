class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            key_=''.join(sorted(s))
            res[key_].append(s)
            
        return res.values()
        
            
            
        