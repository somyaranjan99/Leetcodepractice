class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
      col= len(grid)
      rows= len(grid[0])
      res=[]
      maxLen=-99;
      for i in range(rows):
          calLen=[]
          newMax=0
          for j in range(col):
              calLen.append(len(str(grid[j][i])))
          newMax =max(calLen)
          res.append(newMax)
      return res
        