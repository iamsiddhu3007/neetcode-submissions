class Solution:
    def createDict(self, mystr:str) -> dict:
        mydict = {}
        for s in mystr:
            if s in mydict:
                mydict[s]+=1
            else:
                mydict[s] = 1
        return mydict


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        elif self.createDict(s) != self.createDict(t):
            return False
        else:
            return True
        