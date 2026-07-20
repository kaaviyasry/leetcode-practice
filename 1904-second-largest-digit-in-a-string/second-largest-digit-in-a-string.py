class Solution:
    def secondHighest(self, s: str) -> int:
        st=list(s)
        ans=[]
        for i in range(len(st)):
            if st[i].isdigit():
                ans.append(int(st[i]))
        ans=list(set(ans))
        ans.sort()
        if len(ans)<2:
            return -1
        return ans[-2]
        