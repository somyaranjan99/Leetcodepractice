class Solution:
    def reverseVowels(self, s: str) -> str:
      s=list(s)
      voewl="aeiouAEIOU"
      i=0
      j=len(s)-1
      while i<= j:
          if s[i] in voewl and s[j] in voewl:
              s[i],s[j]=s[j],s[i]
              i +=1
              j -=1
          elif s[i] in voewl and s[j] not in voewl:
              j -=1
          elif s[i] not in voewl and s[j]  in voewl:
              i+=1
          else:
              i += 1
              j -= 1
      return "".join(s)
        