class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        mx = 0
        while right>left:
            if heights[left]<heights[right]:
                if heights[left]*(right-left) > mx:
                    mx = heights[left]*(right-left)
                left +=1
            else:
                if heights[right]*(right-left) > mx:
                    mx = heights[right]*(right-left)
                right -=1
        return mx