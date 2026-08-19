class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            if nums[i] > 0:
                break
            left = i+1
            right = len(nums)-1
            while left<right:
                if (nums[left]+nums[right])==(-1*nums[i]):
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left<len(nums) and nums[left]==nums[left-1]:
                        left+=1
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif (nums[left]+nums[right])>(-1*nums[i]):
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                else:
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                
                
        return ans