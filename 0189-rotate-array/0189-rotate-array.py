class Solution:
    def rotateList(self,start,end,arr):
        while start <= end:
            arr[start],arr[end]=arr[end],arr[start]
            start +=1
            end -=1
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        # if len(nums) <=1:
        #     return
        # if k==0:
        #     return
        # firstK=0
        # if len(nums)%2==0:
        #     firstK=k-1
        # else:
        #     firstK=k
        # self.rotateList(0,firstK,nums);
        # secondK=0
        # if len(nums)%2==0:
        #     secondK=k
        # else:
        #     secondK=k+1
            
        # self.rotateList(secondK,len(nums)-1,nums)
        # self.rotateList(0,len(nums)-1,nums)
        if k==0:return 1
        a=nums[:len(nums)-k];b=nums[len(nums)-k:];c=b+a
        for num in range(0,len(nums)):nums[num]=c[num]

        """
        Do not return anything, modify nums in-place instead.
        """
        