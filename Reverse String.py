class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ch=list(s)
        for i in range(0,len(ch),2*k):
            ch[i:i+k]=reversed(ch[i:i+k])
        return ''.join(ch)
