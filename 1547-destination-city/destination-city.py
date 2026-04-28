class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start={p[0] for p in paths}
        dest={p[1] for p in paths}
        return (dest-start).pop()
    
        