class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        mpp = collections.defaultdict(int)
        preSum = 0
        cnt = 0
        mpp[0] = 1 # Setting 0 in the map.
        for i in range(n):
            preSum += nums[i]
            remove = preSum - k
            cnt += mpp[remove]
            mpp[preSum] += 1
        return cnt
        