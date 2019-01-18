# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
#
# Input: 1
# Output: "A"
# Example 2:
#
# Input: 28
# Output: "AB"
# Example 3:
#
# Input: 701
# Output: "ZY"
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Str=''
        b=n
        i=0
        while True:
            a=(b-1)%26
            b=(b-1)//26
            if b==0:
                return A[a]+Str
            else:
                Str=A[a]+Str
        return Str


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'

        }
        a = n
        s = ''
        while a > 0:
            if a % 26:
                s = s + d[a % 26]
                a = int(a / 26)
            else:
                s = s + 'Z'
                a = int(a / 26 - 1)

        return s[::-1]


a = Solution()
print(a.convertToTitle(7))


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n: return ''
        if n%26: return (self.convertToTitle(n/26) + chr(64+n%26))
        else: return (self.convertToTitle(n/26-1) + 'Z')

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=0: return ''
        if n%26!=0: return (self.convertToTitle(n/26) + chr(64+n%26))
        else: return (self.convertToTitle(n/26-1) + 'Z')