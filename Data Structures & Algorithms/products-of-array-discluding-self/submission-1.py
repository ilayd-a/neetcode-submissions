class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        presum = [1]
        postsum = [1]
        ans=[]
        for i in range(1, len(nums)):
            presum.append(nums[i-1]*presum[i-1])
            postsum.append(nums[len(nums)-i]*postsum[-1])
        for i in range(len(nums)):
            ans.append(presum[i]*postsum[len(postsum)-1-i])
        return ans

