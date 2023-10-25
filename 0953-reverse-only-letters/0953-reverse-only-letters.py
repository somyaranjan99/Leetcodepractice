class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i < j:
            if s[i].isalpha() == False:
                i +=1
            elif s[j].isalpha() ==False:
                j -=1
            else:
                s[i],s[j]=s[j],s[i]
                i +=1
                j-=1
        return "".join(s)
        