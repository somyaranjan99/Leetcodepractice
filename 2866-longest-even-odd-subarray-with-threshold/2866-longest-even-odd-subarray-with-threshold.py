class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res,i,n=0,0,len(nums)
        while i < n:
            if nums[i] % 2  or nums[i] >  threshold:
                i +=1
                continue
            start =i
            while i < n-1 and nums[i]%2 != nums[i+1]%2 and nums[i+1] <= threshold:
                i +=1
            res = max(res,i-start+1)
            i +=1
        return res
            


        