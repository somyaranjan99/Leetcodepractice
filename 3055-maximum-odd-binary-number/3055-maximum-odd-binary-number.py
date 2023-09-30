class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res=[0]*len(s)
        count= s.count('1')
        if count==1:
            res[len(s)-1]=1
        else:
            if count > 1:
                for i in range(count-1):
                    res[i]=1
                res[len(s)-1]=1
        ans=''
        for i in res:
            ans +=str(i)
        return  ans
        