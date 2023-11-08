class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
      arr3= nums1+nums2
      nums={}
      for num in arr3:
        if num in nums and num in nums2 and num in nums1:
          nums[num] +=1
        else:
          nums[num]=1
      smallet=99999999999999
      for key,val in nums.items():
        if val > 1 and key < smallet:
          smallet=key
      return smallet if smallet !=99999999999999 else -1

        