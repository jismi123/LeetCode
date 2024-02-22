class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique=[]
        for x in nums:
            if x not in unique:
                unique.append(x)
        unique.sort()
        m=len(unique)
        if m == 3:
            return(unique[0])
        elif m>3:
            return(unique[m-3])
        else:
            return(unique[m-1])
    
    
