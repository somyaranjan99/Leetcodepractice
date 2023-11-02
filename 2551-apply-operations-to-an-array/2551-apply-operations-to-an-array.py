class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
      for i in range(1,len(nums)):
        if nums[i-1]==nums[i]:
            nums[i-1]=nums[i-1]*2
            nums[i]=0

      j=0
      for i in range(len(nums)):
          if nums[i] !=0:
              nums[i],nums[j]=nums[j],nums[i]
              j +=1
      return nums
        