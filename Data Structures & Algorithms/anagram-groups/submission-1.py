class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in range(len(strs)):
            if str(sorted(strs[i])) in ans:
                ans[str(sorted(strs[i]))].append(strs[i])
            else:
                ans[str(sorted(strs[i]))] = [strs[i]]
        return list(ans.values())