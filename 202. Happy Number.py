# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo=set()
        s=0
        while n!=1:
            s=sum([int(i) ** 2 for i in str(n)])
            if s in memo:
                return False
            else:
                memo.add(s)
            n=s
        return True


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)
            if slow == fast:
                break
        if slow == fast == 1:
            return True
        else:
            return False

    def digitSquareSum(self, n):
        Sum = 0
        while n != 0:
            Sum += (n % 10) ** 2
            n /= 10
        return Sum