class Solution:
    def makeGood(self, s: str) -> str:
      stack=[]
      for st in s:
          if len(stack) >0 and abs(ord(stack[len(stack)-1])-ord(st))==32:
              stack.pop()
          else:
              stack.append(st)
      return "".join(stack)
        