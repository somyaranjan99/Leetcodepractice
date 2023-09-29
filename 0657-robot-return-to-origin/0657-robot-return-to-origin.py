class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for s in moves:
            if s=='R':
                x +=1
            elif s=='L':
                x -=1
            elif s=='U':
                y +=1
            else:
                y -=1
        if x==0 and y==0:
            return True
        else:
            return False


