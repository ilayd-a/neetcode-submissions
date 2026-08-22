class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                numbers.append(int(i))
            else:
                no2 = numbers.pop()
                no1 = numbers.pop()
                if i=='+':
                    numbers.append(int(no1)+int(no2))
                elif i =='-':
                    numbers.append(int(no1)-int(no2))
                elif i=='/':
                    numbers.append(int(int(no1)/int(no2)))
                else:
                    numbers.append(int(no1)*int(no2))
        return int(numbers[-1])