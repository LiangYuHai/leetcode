class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(pow(x,0.5))
# Binary search
def mySqrt(self, x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid
        else:
            l = mid + 1