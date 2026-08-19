class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        cnt = 0
        left=0
        right=0
        mx= 0
        while right<len(s) and left<=right:
            if s[right] not in hm:
                hm[s[right]] = 1
                right+=1
                cnt +=1
            else:
                while s[right] in hm:
                    hm.pop(s[left])
                    cnt-=1
                    left+=1
            if cnt>mx:
                mx = cnt
        return mx
            