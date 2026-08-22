class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        if len(s)<2:
            return False
        for i in s:
            if i in "({[":
                opens.append(i)
            else:
                if len(opens)==0:
                    return False
                close = opens.pop()
                if i ==')' and close!='(':
                    return False
                elif i == ']' and close!='[':
                    return False
                elif i == '}' and close!='{':
                    return False
        if len(opens)!=0:
            return False
        return True
        