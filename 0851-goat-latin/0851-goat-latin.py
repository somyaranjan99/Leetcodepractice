class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U'];
        spltSen=sentence.split(' ')
        ans=[]
        for ind,stn in enumerate(spltSen):
            res=''
            aAdd = ['a'] * (ind + 1)
            if stn.startswith(tuple(vowels)):
                res = stn+'ma'+"".join(aAdd)
            else:
                if len(stn) <= 1:
                    res= stn+'ma'+"".join(aAdd)
                else:
                    st1=stn[0]
                    res = stn[1:]+st1+'ma' + "".join(aAdd)
            ans.append(res)
        return (' '.join(ans))
        