class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # map={}
        # for num in nums:
        #     if num in map:
        #         map[num]+=1
        #     else:
        #         map[num]=1
        # for key,value in map.items():
        #     if value==1:
        #         return key
        # return -1
        xor=0
        for i in range(len(nums)):
            xor =xor^nums[i]
        return xor