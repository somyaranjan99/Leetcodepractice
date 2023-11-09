class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
      for i in range(2, n-1):
            bit_form = ''
            num = n
            while num:
                rem = num % i
                num = num // i
                bit_form += str(rem)
            if bit_form != bit_form[::-1]:
                return False
      return True
        