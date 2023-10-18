class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        for i in range(len(spaces)):
            spaces[i] += i
        
        for i in spaces:
            s = s[:i] + ' ' + s[i:]
        
        return s
