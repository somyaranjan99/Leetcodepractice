class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
      nums.sort()
      set_nums=set()
      while len(nums) > 0:
          i=0
          j=len(nums)-1
          avgNum = (nums[i] + nums[j])/2
          print(avgNum)
          set_nums.add(avgNum)
          nums.pop()
          nums.pop(i)
      return len(set_nums)
        