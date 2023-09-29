class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            st=''
            if i %3==0:
                st +='Fizz'
            if i%5==0:
                st +='Buzz'
            if st=='':
                st=str(i)
            res.append(st)
        return res
        