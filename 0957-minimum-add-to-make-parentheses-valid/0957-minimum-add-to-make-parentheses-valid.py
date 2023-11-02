class Solution:
    def minAddToMakeValid(self, s: str) -> int:
      stk=[]
      count=0
      for st in s:
          if st=='(' :
              stk.append(st)
          elif len(stk) > 0 and st==')':
              stk.pop()
          else:
              count +=1
      return count + len(stk)
        