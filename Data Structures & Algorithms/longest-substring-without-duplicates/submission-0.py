class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lp = 0
        max_len = 0

        for rp in range(len(s)):
            while s[rp] in seen:
                seen.remove(s[lp])
                lp += 1

            seen.add(s[rp])
            max_len = max(max_len, rp - lp + 1)

        return max_len