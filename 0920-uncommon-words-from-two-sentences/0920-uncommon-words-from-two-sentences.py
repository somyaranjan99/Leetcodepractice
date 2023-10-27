class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      sentenceHas={}
      i=0
      j=0
      s1=s1.split(" ")
      s2=s2.split(" ")
      while i <=len(s1)-1 and j <=len(s2)-1:
          if s1[i] not in sentenceHas:
              sentenceHas[s1[i]]=1
          else:
              sentenceHas[s1[i]] +=1
          if s2[j] not in sentenceHas:
              sentenceHas[s2[j]] = 1
          else:
              sentenceHas[s2[j]] += 1
          i+=1
          j+=1
      while i <=len(s1)-1:
          if s1[i] not in sentenceHas:
              sentenceHas[s1[i]]=1
          else:
              sentenceHas[s1[i]] +=1
          i+=1
      while j <=len(s2)-1:
          if s2[j] not in sentenceHas:
              sentenceHas[s2[j]] = 1
          else:
              sentenceHas[s2[j]] += 1
          j+=1
      res=[]
      for key,val in sentenceHas.items():
          if val==1:
              res.append(key)
      return res
        