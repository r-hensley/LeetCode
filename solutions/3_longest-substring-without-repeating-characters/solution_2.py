from typing import Optional


class Solution:
    """Given a string s, find the length of the longest substring without repeating characters."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The most basic brute-force solution as a preliminary attempt. Later attempts will improve on the method greatly.
        :param s: A string
        :return: Length of the longest substring
        """
        character_bits: list[Optional[int]] = [None] * 128

        # Store the length of the maximum string at any point
        current_max_length = 0

        # Define a substring window by "left" and "right" variables
        left = 0  # Start left index at 0, will move to the right when a duplicate character is found
        # Then for the right index, walk over the entire string
        for right in range(len(s)):
            current_character = s[right]
            current_character_bit = ord(current_character)

            # Check if this character is activated in the bitmap already
            last_character_instance_index: int = character_bits[current_character_bit]
            if last_character_instance_index is not None:
                # Stored in the location of this character should be the index location in the string of the last
                # instance of the character. If it is inside the window (greater than "left"), then move left past it
                if left <= last_character_instance_index:
                    left = last_character_instance_index + 1  # move left border of window past this character

            # If the new string after moving the right border is larger than current max string length, update it
            current_substring_length = right - left + 1
            if current_substring_length > current_max_length:
                current_max_length = current_substring_length

            # Update character_bits with position of current character for if it is encountered as a duplicate later
            character_bits[current_character_bit] = right

        return current_max_length


if __name__ == "__main__":
    test_cases = [('dvdf', 3), ('aaaaaaaabcdefffffabcddeeeeeee', 6), (' ', 1), ("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ('a', 1)]
    s = Solution()
    for test in test_cases:
        res = s.lengthOfLongestSubstring(test[0])
        ans = test[1]
        assert res == ans, f"'{test[0]}': {res=}, {ans=}"


# Runtime: 57 ms, faster than 95.02% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 13.62% of Python3 online submissions for Longest Substring Without Repeating Characters.
# I prefer easy to understand code than super compact code

# https://leetcode.com/submissions/detail/718568592/
