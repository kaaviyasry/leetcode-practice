class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for ch in words:
            if ch.startswith(pref):
                count+=1
        return count

        