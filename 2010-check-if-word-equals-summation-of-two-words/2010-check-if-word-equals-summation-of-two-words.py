class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        count=0
        d={}
        for i in range(97,123):
            d[chr(i)]=count
            count +=1
        k=0
        j=0
        t=0
        first =''
        secW=''
        target=''
        while k < len(firstWord) and j < len(secondWord) and t < len(targetWord):
            first += str(d[firstWord[k]])
            secW += str(d[secondWord[j]])
            target += str(d[targetWord[t]])
            k +=1
            j +=1
            t +=1
        while k < len(firstWord):
            first += str(d[firstWord[k]])
            k += 1
        while j < len(secondWord):
            secW += str(d[secondWord[j]])
            j +=1
        while t < len(targetWord):
            target += str(d[targetWord[t]])
            t +=1
        if int(first)+int(secW) == int(target):
            return True
        return False
        