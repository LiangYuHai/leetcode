#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        num = 0
        prev = ""

        for rs in s:
            if (rs in d):
                num += d[rs]

            if (len(prev) > 0):
                if (d[prev] == d[rs]):
                    continue
                else:
                    if (d[prev] < d[rs]):
                        num -= (2 * d[prev])

            prev = rs

        return num

    def romanToInt2(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i, letter in enumerate(s):
            if letter == 'I':
                if i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    a -= 1
                    continue
                a += 1
            if letter == 'V':
                a += 5
            if letter == 'X':
                if i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    a -= 10
                    continue
                a += 10
            if letter == 'L':
                a += 50
            if letter == 'C':
                if i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    a -= 100
                    continue
                a += 100
            if letter == 'D':
                a += 500
            if letter == 'M':
                a += 1000
        return a