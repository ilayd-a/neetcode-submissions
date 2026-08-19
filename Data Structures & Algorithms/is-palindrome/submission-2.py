class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha=""
        for i in range(len(s)):
            if s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuwvxyz0123456789":
                alpha+=s[i]
        print(alpha)
        for i in range(len(alpha)//2):
            if alpha[i]==alpha[len(alpha)-i-1]:
                continue
            elif ord(alpha[i])< 97 and ord(alpha[i])> 64 and (ord(alpha[i])+32) == ord(alpha[len(alpha)-i-1]):
                continue
            elif ord(alpha[i])>96 and (ord(alpha[i])-32) == ord(alpha[len(alpha)-i-1]):
                continue
            else:
                return False
        return True
        