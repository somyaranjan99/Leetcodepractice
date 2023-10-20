class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total=''
        for i in range(len(digits)):
            total +=str(digits[i])
        total =int(total)+1
        total =str(total)
        ans=[]
        for num in total:
            ans.append(int(num))
        return ans
        