class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      stk1=[]
      stk2=[]
      for st in s:
          if len(stk1) > 0 and st=='#':
              stk1.pop()
          elif st !='#':
              stk1.append(st)
      for st in t:
          if len(stk2) > 0 and st=='#':
              stk2.pop()
          elif st !='#':
              stk2.append(st)
      if stk1==stk2:
        return True
      else:
        return False    