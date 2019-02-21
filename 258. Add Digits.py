class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        Sum=num
        while True:
            Sum=sum([int(i) for i in str(Sum)])
            if Sum<10:
                return Sum

class Solution(object):
    def addDigits(self, num):
        return num if num == 0 else num % 9 or 9
