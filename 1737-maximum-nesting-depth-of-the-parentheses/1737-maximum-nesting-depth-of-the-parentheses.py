class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxLen=-999
        for ch in s:
            if ch ==")":
                stack.append(ch)
            elif ch=="(":
                if(stack):
                    stack.pop()
            maxLen=max(maxLen,len(stack))
        return maxLen
        