class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numset=set()
        for i in range(len(nums)):
            hashset=set()
            for j in range(i+1,len(nums)):
                k= -(nums[i]+nums[j])
                if k  in hashset:
                    temp =[nums[i],nums[j],k]
                    temp.sort()
                    numset.add(tuple(temp))
                hashset.add(nums[j])
        return list(numset)

                

        