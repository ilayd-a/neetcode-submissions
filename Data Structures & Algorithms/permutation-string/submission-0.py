class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count ={}
        s2count = {}
        if len(s2)<len(s1):
            return False
        for i in s1:
            s1count[i] = s1count.get(i, 0) + 1
        for i in range(len(s1)):
            s2count[s2[i]] = s2count.get(s2[i], 0) + 1
        if s2count == s1count:
            return True
        left=0
        right = len(s1)-1
        while right<(len(s2)-1):
            if s2count[s2[left]]>1:
                s2count[s2[left]]-=1
                left+=1
            else:
                s2count.pop(s2[left])
                left+=1
            if s2[right+1] in s2count:
                s2count[s2[right+1]]+=1
                right+=1
            else:
                s2count[s2[right+1]]=1
                right+=1
            if s1count==s2count:
                return True
        return False