class Solution:
    def reverseWords(self, s: str) -> str:
        
        new=s.split()
        list1=[]
        l=len(new)
        for i in range(l):
            list1.append(new[i][::-1])
        p=' '.join(list1)    
        return(p)
