class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = (nums[0],0)
        maxis = []
        for i in range(k):
            if maxi[0]<nums[i]:
                maxi = (nums[i],1)
            elif maxi == nums[i]:
                maxi = (nums[i], maxi[1]+1)
        maxis.append(maxi[0])
        right = k
        left=0
        while right<len(nums):
            if maxi[0] == nums[left]:
                if maxi[1]>1 and maxi[0]>nums[right]:
                    maxi = (nums[right-k], maxi[1]-1)
                else:
                    maxi = (max(nums[left+1:right+1]), 1)
                maxis.append(maxi[0])
            else:
                print(maxi[0])
                print(nums[right])
                if nums[right]> maxi[0]:
                    maxi = (nums[right],1)
                    print(maxi)
                maxis.append(maxi[0])
            left+=1
            right+=1
        return maxis
                    
