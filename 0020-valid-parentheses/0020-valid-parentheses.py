class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for i in range(len(s)):
          if  s[i]=='(' or s[i]=='[' or s[i]=='{':
              stack.append(s[i]);
          else:
              if len(stack) < 1 :
                  return False;
              c= stack[len(stack)-1]
              stack.pop()
              if c=='(' and s[i]==')' or c=='{' and s[i]=='}' or c=='[' and s[i]==']':
                  continue;
              else:
                  return  False
      if len(stack)==0:
          return True
      else:
          return False
        