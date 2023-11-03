class Solution:
    def removeStars(self, s: str) -> str:
      stk=[]
      for chrs in s:
        if chrs=='*':
          stk.pop()
        else:
          stk.append(chrs)
      return "".join(stk)
        