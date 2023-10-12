class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumNum=0
        maxEle=-9999999
        for i in range(len(nums)):
            sumNum +=nums[i]
            if sumNum > maxEle:
                maxEle=sumNum
            if sumNum < 0:
                sumNum =0
        return maxEle
        