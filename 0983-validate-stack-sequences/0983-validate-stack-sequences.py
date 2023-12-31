class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
      i=0
      stack=[]
      for num in pushed:
        stack.append(num)
        while i<len(popped) and stack and stack[-1]==popped[i]:
          stack.pop()
          i+=1
      return not stack


        