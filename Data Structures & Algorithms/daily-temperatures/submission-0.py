class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append(i)
            elif temperatures[stack[-1]]<temperatures[i]:
                while(len(stack)!=0 and temperatures[stack[-1]]<temperatures[i]):
                    ans[stack[-1]] = i- stack[-1]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        return ans
