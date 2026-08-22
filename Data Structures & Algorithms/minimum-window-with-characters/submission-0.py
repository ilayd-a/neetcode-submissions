class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tcount = {}
        for char in t:
            tcount[char] = tcount.get(char, 0) + 1

        scount = {}
        need = len(tcount)
        have = 0

        result_start = 0
        result_length = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in tcount:
                scount[char] = scount.get(char, 0) + 1

                if scount[char] == tcount[char]:
                    have += 1

            # Current window contains everything required
            while have == need:
                window_length = right - left + 1

                if window_length < result_length:
                    result_start = left
                    result_length = window_length

                left_char = s[left]

                if left_char in tcount:
                    scount[left_char] -= 1

                    if scount[left_char] < tcount[left_char]:
                        have -= 1

                left += 1

        if result_length == float("inf"):
            return ""

        return s[result_start:result_start + result_length]