class Solution:
    def Rev(self,s:List[str] )->bool:
        l=0
        r=len(s)-1
        while r<l:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s

call=Solution()
print(call.Rev('my name '))