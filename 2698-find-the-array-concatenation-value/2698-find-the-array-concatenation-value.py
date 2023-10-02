class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        sum=0
        while i <= j:
            if i==j:
                num=str(nums[i])
            else:
                num =str(nums[i])+str(nums[j])
            i+=1
            j-=1
            sum +=int(num)
        return sum
        
        