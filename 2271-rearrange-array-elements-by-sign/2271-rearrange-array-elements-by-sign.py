class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_arr=[]
        neg_arr=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                pos_arr.append(nums[i])
            else:
                neg_arr.append(nums[i])
        i=0
        j=0
        while i < len(pos_arr) and j < len(neg_arr):
            nums[i*2]=pos_arr[i]
            nums[i*2+1]=neg_arr[j]
            i+=1
            j+=1
        return nums
        