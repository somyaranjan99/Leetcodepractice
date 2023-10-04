class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxSum=0
        for num in nums:
            if num==1:
                count +=1
                maxSum=max(maxSum,count)
            else:
                count =0
        return maxSum
        