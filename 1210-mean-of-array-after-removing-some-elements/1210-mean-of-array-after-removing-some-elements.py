class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        lengthNums=len(arr)
        start=int(0.05*lengthNums)
        end =lengthNums-start
        new_length=len(arr[start:end])
        sumN=sum(arr[start:end])
        return sumN/new_length
        