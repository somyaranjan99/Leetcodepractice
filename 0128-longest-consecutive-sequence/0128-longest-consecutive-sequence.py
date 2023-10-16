class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st=set()
        for num in nums:
            st.add(num)
        longest=1
        for ele in st:
            if ele-1 not in st:
                x=ele
                cnt=1
                while x+1 in st:
                    x +=1
                    cnt +=1
                longest=max(longest,cnt)
        return longest
                
        