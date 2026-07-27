class Solution:
    def isValid(self, s: str) -> bool:
        mapPar = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        i = 0
        while i < len(s):
            if s[i] in mapPar.values():
                stack.append(s[i])
                i+=1
            elif s[i] in mapPar:
                if stack and stack[-1]==mapPar[s[i]]:
                    stack.pop()
                    i += 1
                else:
                    return False
        return len(stack)==0


        