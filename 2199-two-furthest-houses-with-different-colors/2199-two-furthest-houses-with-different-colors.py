class Solution:
    def maxDistance(self, colors: List[int]) -> int:
      i=0
      j=len(colors)-1
      maxDis=-9999
      n=len(colors)
      while colors[0] ==colors[j]:
        j -=1
      while colors[n-1] ==colors[i]:
        i+=1
      return max(j,n-i-1)
      
        