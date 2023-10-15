class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        width=0
        line=1
        res=[]
        for c in s:
            cwidth = widths[ord(c)-ord('a')]
            if cwidth + width >100:
                line+=1
                width =0
            width +=cwidth
        res.append(line)
        res.append(width)
        return res
        

        