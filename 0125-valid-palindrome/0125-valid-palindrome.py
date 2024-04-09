class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.translate(str.maketrans('','',string.punctuation))
        s=((s.lower()).strip()).replace(' ','')
        first, last=0, len(s)-1
        while(first<last):
            if s[first]!=s[last]:
                return False
            else:
                first+=1
                last-=1
            
        return True