class Solution:
    def isPalindrome(self, s: str) -> bool:

      final_str= ''.join(letter for letter in s if letter.isalnum())
      final_str=final_str.lower()
      i=0
      j=len(final_str)-1
      while i < j:
          if final_str[i] !=final_str[j]:
              return False
          else:
              i += 1
              j -= 1

      return True
        