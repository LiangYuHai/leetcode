# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        i=-1
        while s[i]==' ':
            if i-1<-len(s):
                return 0
            i-=1
        j=i
        while s[i]!=' ':
            if i-1<-len(s):
                return j-i+1
            i-=1
        return j-i

class  Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(" ")[-1])
