class Solution:
    """Given a string s, find the length of the longest substring without repeating characters."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The most basic brute-force solution as a preliminary attempt. Later attempts will improve on the method greatly.
        :param s: A string
        :return: Length of the longest substring
        """
        building_strings = []
        to_remove = []
        max_length = 0
        for starting_character in s:
            # Attempt to add the new character to any of the other building strings
            for idx, start in enumerate(building_strings):
                # If the string is already in the substring, check if it's the new longest, then delete from list
                if starting_character in start:
                    if len(start) > max_length:
                        max_length = len(start)
                    to_remove.append(idx)

                else:
                    building_strings[idx] += starting_character

            for idx in sorted(to_remove, reverse=True):
                del(building_strings[idx])
            to_remove = []

            building_strings.append(starting_character)

        for string in building_strings:
            new_len = len(string)
            if new_len > max_length:
                max_length = new_len

        return max_length


if __name__ == "__main__":
    test_cases = [('dvdf', 3), ('aaaaaaaabcdefffffabcddeeeeeee', 6), (' ', 1), ("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ('a', 1)]
    s = Solution()
    for test in test_cases:
        res = s.lengthOfLongestSubstring(test[0])
        ans = test[1]
        assert res == ans, f"'{test[0]}': {res=}, {ans=}"


# Runtime: 591 ms, faster than 13.15% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 13.66% of Python3 online submissions for Longest Substring Without Repeating Characters.