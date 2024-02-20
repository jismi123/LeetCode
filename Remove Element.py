class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        s=0
        for i in range(l):
            if nums[i]!=val:
                nums[s]=nums[i]
                s=s+1
        return s
          
