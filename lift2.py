class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

            # Continue matching target
            if freq[target_idx] > 0:
class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd-frequency character
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Build the left half
        half = []

        for i in range(26):
            half.extend([chr(i + ord('a'))] * (count[i] // 2))

        def buildPalindrome(arr):
            left = "".join(arr)
            return left + middle + left[::-1]

        # Smallest palindrome
        candidate = buildPalindrome(half)

        if candidate > target:
            return candidate

        # Find next lexicographical permutation of half
        i = len(half) - 2

        while i >= 0 and half[i] >= half[i + 1]:
            i -= 1

        # No next permutation exists
        if i < 0:
            return ""

        # Find smallest character greater than half[i]
        j = len(half) - 1

        while half[j] <= half[i]:
            j -= 1

        # Swap
        half[i], half[j] = half[j], half[i]

        # Reverse the remaining suffix
        half[i + 1:] = reversed(half[i + 1:])

        candidate = buildPalindrome(half)

        if candidate > target:
            return candidate

        return ""
