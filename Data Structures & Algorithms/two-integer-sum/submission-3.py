class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        nums = sorted(nums)
        j=0
        i=0
        while i<len(nums) and j<len(nums):
            print("i= ", i, "nums[i] = ", nums[i])
            print("j= ", j, "nums[len(nums)-1-j] = ", nums[len(nums)-1-j])
            if (nums[i]+nums[len(nums)-1-j])==target:
                ans = [dic[nums[i]].pop(), dic[nums[len(nums)-1-j]].pop()]
                return sorted(ans)
            elif (nums[i]+nums[len(nums)-1-j])>target:
                j+=1
            else:
                i+=1