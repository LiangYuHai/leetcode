#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        origin = x
        rev = 0
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        while (x != 0):
            temp = int(float(x) / 10)
            pop = x - temp * 10
            x = temp
            rev = rev * 10 + pop
        if rev == origin:
            return True
        else:
            return False