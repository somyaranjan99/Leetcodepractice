class Solution:
    def minSwaps(self, s: str) -> int:
      maxSwap=-111
      close=0
      for st in s:
        if st=="]":
          close +=1
        else:
          close -=1
        maxSwap=max(maxSwap,close)
      return (maxSwap+1)//2
      


        