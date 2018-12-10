# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if a[-1] == "1" and b[-1] == "1":
            if len(a) > 1 and len(b) > 1:
                return self.addBinary(self.addBinary(a[:-1], "1"), b[:-1]) + "0"
            elif len(a) == 1 and len(b) > 1:
                return self.addBinary("1", b[:-1]) + "0"
            elif len(b) == 1 and len(a) > 1:
                return self.addBinary(a[:-1], "1") + "0"
            else:
                return "10"
        elif a[-1] == "0" and b[-1] == "0":
            if len(a) > 1 and len(b) > 1:
                return self.addBinary(a[:-1], b[:-1]) + "0"
            elif len(a) == 1 and len(b) > 1:
                return self.addBinary("0", b[:-1]) + "0"
            elif len(b) == 1 and len(a) > 1:
                return self.addBinary(a[:-1], "0") + "0"
            else:
                return "0"
        else:
            if len(a) > 1 and len(b) > 1:
                return self.addBinary(a[:-1], b[:-1]) + "1"
            elif len(a) == 1 and len(b) > 1:
                return self.addBinary("0", b[:-1]) + "1"
            elif len(b) == 1 and len(a) > 1:
                return self.addBinary(a[:-1], "0") + "1"
            else:
                return "1"

class Solution:
    def addBinary(self, a, b):
        return bin(eval('0b' + a) + eval('0b' + b))[2:]