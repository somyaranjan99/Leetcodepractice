class Solution:
    def reformatNumber(self, number: str) -> str:

      number = number.replace(' ','').replace('-','')
      ans=[]
      while len(number) > 0:
          if len(number)==3:
              ans.append(number[0:3])
              number=number[3:]
          elif len(number) ==2:
              ans.append(number[0:2])
              number = number[2:]
          elif len(number) ==4:
              ans.append(number[0:2])
              number=number[2:]
          elif len(number) > 4:
              ans.append(number[0:3])
              number=number[3:]
      return "-".join(ans)
        