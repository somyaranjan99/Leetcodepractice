class Solution:
    def countVowelSubstrings(self, s: str) -> int: 
      count = 0
      l = []
      b = ["a","e","i","o","u"]
      for i in range(len(s)+1):
          for j in range(i):
              a = s[j:i]
              if "a" in a and "e" in a and "i" in a and "o" in a and "u" in a:
                  l.append(a)
      for i in l:
          c1 = 0
          for j in i:
              if j not in b:
                  c1+=1
                  break
          if c1==0:
              count+=1
              
      return (count)

        