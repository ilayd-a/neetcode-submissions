class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        hm = dict(sorted(hm.items(), key = lambda item: item[1]))
        ans = list(hm.keys())
        return ans[-k:]
