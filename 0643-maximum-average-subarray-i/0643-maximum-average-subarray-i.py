class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        ans=-99999999
        avgSum=0
        if len(nums) <=1:
            return nums[0]
        while j < len(nums):
            avgSum +=nums[j]
            avg=-999999
            if j-i+1 < k:
                j +=1
            elif j-i+1==k:
                if i > 0:
                    avgSum -=nums[i-1]
                avg = avgSum/k
                i+=1
                j+=1
            ans= max(ans,avg)
        return ans

        