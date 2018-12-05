# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_len = 9999
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for word in strs:
            if word == "":
                return ""
            if len(word) < min_len:
                min_len = len(word)
        for j in range(min_len):
            letter = []
            for word in strs:
                letter.append(word[j])
            if len(list(set(letter))) != 1:
                return strs[0][0:j]
        return strs[0][0:min_len]