class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        minNum=999999999
        i=0
        j=0
        while j < len(nums):
            if j-i+1 < k:
                j +=1
            elif j-i+1 == k:
                mindiff= min(nums[i:j+1])
                maxdiff=max(nums[i:j+1])
                diff=  maxdiff-mindiff
                minNum =min(minNum,diff)
                i +=1
                j+=1
        return minNum