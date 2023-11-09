class Solution:
    def isHappy(self, num: int) -> bool:
      mapHas={}
      num=str(num)
      while int(num) > 1:
          sum=0
          for i in range(len(str(num))):
              sum +=int(num[i])*int(num[i])

          if sum not in mapHas:
              mapHas[sum] = 1
              num = str(sum)
          else:
              num=-1
              break;
      if num ==-1:
        return False
      else:
        return True
        