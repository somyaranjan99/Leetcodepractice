class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numsMap={}
        for num in nums:
            print(num)
            if num in numsMap:
                numsMap[num] +=1
            else:
                numsMap[num]=1
        for key,val in numsMap.items():
            if val==1:
                return key
        return -1
        