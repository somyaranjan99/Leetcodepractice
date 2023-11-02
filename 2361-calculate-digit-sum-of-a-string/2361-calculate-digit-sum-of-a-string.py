class Solution:
    def digitSum(self, s: str, k: int) -> str:
      while len(s) > k:
          new_set=[]
          for i in range(0,len(s),k):
              new_set.append(s[i:i+k])
          s=''
          for n in new_set:
              val = 0
              for j in n:
                  val +=int(j)
              s +=str(val)
      return s
        