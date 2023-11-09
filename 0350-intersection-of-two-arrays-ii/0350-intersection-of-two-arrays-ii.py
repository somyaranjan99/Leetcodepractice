class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      res=[]
      if(len(nums1) < len(nums2)):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])

      else:
          for i in range(len(nums2)):
              if nums2[i] in nums1:
                  res.append(nums2[i])
                  nums1.remove(nums2[i])
      return res
        