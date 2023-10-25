class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        mapNum={}
        for num in nums:
            if num not in mapNum:
                mapNum[num]=1
            else:
                mapNum[num]+=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > 0 and 0-nums[i] in mapNum:
                return nums[i]
            else:
                continue
        return -1
        