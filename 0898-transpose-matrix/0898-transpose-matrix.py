class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix[0])
        col=len(matrix)
        ans=[]
        for i in range(row):
            trspose=[]
            for j in range(col):
               trspose.append( matrix[j][i])
            ans.append(trspose)
        return ans
        