'''
5. Longest Palindromic Substring
Medium

Hint
Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd length palindrome
            len1 = self.expand_from_center(s, i, i)
            # Even length palindrome
            len2 = self.expand_from_center(s, i, i + 1)

            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end+1]

    def expand_from_center(self, s, left, right):
        # Expand as long as characters match and we're in bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Substring length = right - left - 1
        return right - left - 1

Sol = Solution()
print(Sol.longestPalindrome("babad"))
print(Sol.longestPalindrome("cbbd"))
print(Sol.longestPalindrome("dwvvlmokkdtnbrpnueyamqwrvrcwpwiaglvoizmsfuxzgvkvsexgwxwoygayznjlswucmoehugrkjkduwtdrguaqtqwdvrekxgphbitvxmpazkceodsyjzuvjfvgjbtiawrpcwomeiwgoelilfylydsdgawybjjmbgfhkndnvqdryncglaxmzndsoziqqmrwticjomsyatisjduifwfzjkgpdpneurlylzgrdlixhosmmwhaqgpxhmjqxsasfnqnppyufxwpukaruvlnfetymzqwzfklpwdwwrupvrttxdkgjbrzwuvwkkjiynnoemfzrjaepvejvxqkvhqtegtiwtbwlneqzryjzzjyrzqenlwbtwitgetqhvkqxvjevpeajrzfmeonnyijkkwvuwzrbjgkdxttrvpurwwdwplkfzwqzmytefnlvurakupwxfuyppnqnfsasxqjmhxpgqahwmmsohxildrgzlylruenpdpgkjzfwfiudjsitaysmojcitwrmqqizosdnzmxalgcnyrdqvndnkhfgbmjjbywagdsdylyflileogwiemowcprwaitbjgvfjvuzjysdoeckzapmxvtibhpgxkervdwqtqaugrdtwudkjkrguheomcuwsljnzyagyowxwgxesvkvgzxufsmziovlgaiwpwcrvrwqmayeunprbntdkkomlvvwd"))
print(Sol.longestPalindrome("ac"))
print(Sol.longestPalindrome("bb"))