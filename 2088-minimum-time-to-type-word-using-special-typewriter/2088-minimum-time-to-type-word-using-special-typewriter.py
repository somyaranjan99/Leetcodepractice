class Solution:
    def minTimeToType(self, word: str) -> int:
      count=0
      start=0
      for st in word:
        current= ord(st)-ord('a')
        count += min(abs(start-current),abs(start-26-current),abs(start+26-current))
        start=current
      return count+len(word)

        