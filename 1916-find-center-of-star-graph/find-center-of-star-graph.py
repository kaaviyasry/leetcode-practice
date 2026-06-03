class Solution(object):
    def findCenter(self, edges):
        for i in edges[0]:
            if i in edges[1]:
                return i
        
        