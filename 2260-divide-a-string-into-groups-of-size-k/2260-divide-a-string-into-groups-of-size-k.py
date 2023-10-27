class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
      slen=len(s)
      ans=[]
      res=[]
      rem= slen%k
      needel=0
      if rem > 0 :
        needel= k-rem
      for st in s:
          res.append(st)
      res=['']+res +[fill]*needel
      temp =''
      for i in range(len(res)):
          temp +=res[i]
          if i > 0 and i%k==0:
              ans.append(temp)
              temp =''
      return ans
      