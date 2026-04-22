        for right in range(len(s)):
            # If duplicate found, shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character
            char_set.add(s[right])

            # Update max length
            max_length = max(max_length, right - left + 1)

        max_length =0
        left = 0
        char_set = set()
    def lengthOfLongestSubstring(self, s):
class Solution(object):
