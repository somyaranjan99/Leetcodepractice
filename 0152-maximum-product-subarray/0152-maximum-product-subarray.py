class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      maxSubproduct=-9999
      maxPrefix=0
      maxSubfix=0
      for i in range(len(nums)):
        if maxPrefix==0:
          maxPrefix=1
        if maxSubfix==0:
          maxSubfix=1
        maxPrefix *=nums[i]
        maxSubfix *=nums[len(nums)-i-1]
        maxSubproduct= max(maxSubproduct,max(maxPrefix,maxSubfix))
      return maxSubproduct


        

        
        