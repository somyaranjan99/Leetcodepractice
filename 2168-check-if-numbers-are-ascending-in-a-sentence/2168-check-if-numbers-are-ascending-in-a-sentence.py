class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        splArr= s.split(' ')
        res=[]
        for i in range(len(splArr)):
            if splArr[i].isdigit():
                res.append(int(splArr[i]))
        for i in range(1,len(res)):
            if res[i-1] < res[i]:
                continue
            else:
                return False
        return True
        