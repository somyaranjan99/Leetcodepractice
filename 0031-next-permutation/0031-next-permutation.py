class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        ind=-1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                ind=i
                break
        if ind==-1:
            nums[:]=nums[::-1]
            return nums
        for i in range(n-1,ind-1,-1):
            if nums[ind] < nums[i]:
                nums[ind],nums[i]=nums[i],nums[ind]
                break
        nums[ind+1:] = reversed(nums[ind+1:])
        return nums

        