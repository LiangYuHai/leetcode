import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = re.sub('[^a-zA-Z0-9]+', '', s).lower()
        return s == s[::-1]

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s=''.join(s.split()).lower()
        return s==s[::-1]