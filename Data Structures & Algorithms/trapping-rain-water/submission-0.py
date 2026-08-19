class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]]
        postfix = [height[-1]]
        ans = 0
        for i in range(1, len(height)):
            if height[i]>prefix[-1]:
                prefix.append(height[i])
            else:
                prefix.append(prefix[-1])
        for i in reversed(range(len(height)-1)):
            if height[i]>postfix[-1]:
                postfix.append(height[i])
            else: 
                postfix.append(postfix[-1])
        
        for i in range(len(height)):
            ans += min(prefix[i], postfix[len(height)-i-1]) - height[i]
        return ans