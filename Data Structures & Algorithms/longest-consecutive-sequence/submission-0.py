class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        nums = sorted(nums)
        mx = 0
        for i in nums:
            if (i-1) in hm:
                hm[i] = hm[i-1]+1
            else:
                hm[i]=1
            if hm[i]>mx:
                mx = hm[i]
        return mx