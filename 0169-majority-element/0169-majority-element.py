class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =0
        el=0
        for i in range(len(nums)):
                if count==0:
                    count +=1
                    el=nums[i]
                elif nums[i]==el:
                    count +=1
                else:
                    count -=1
        for i in range(len(nums)):
            if nums[i]==el:
                count +=1
        if count >= len(nums)//2:
            return el
        return -1
        