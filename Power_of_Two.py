class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a=float('inf')
        for i in range(0,100):
            if pow(2,i)==n:
                return True
       
        return False 
