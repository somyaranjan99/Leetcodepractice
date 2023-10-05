class Solution:
    def removeDuplicates(self, s: str) -> str:
        sleen=len(s)
        stack=[0]
        stack.append(s[0])
        i=1
        while i < len(s):
            if stack[-1] ==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        if len(stack) >=1:
            stack.pop(0)
        return (''.join(stack))
        