class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sset=set()
        prev=''
        next=''
        for st in s:
            sset.add(st)
        for i in range(len(s)):
            if s[i].lower() not in sset or s[i].upper() not in sset:
                prev = self.longestNiceSubstring(s[0:i])
                next= self.longestNiceSubstring(s[i+1:])
                return max(prev, next, key=len) 
        return s
        