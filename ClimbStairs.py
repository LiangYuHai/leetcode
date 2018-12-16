class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        b=2
        c=0
        if n==1:return a
        if n==2:return b
        if n>2:
            for i in range(3,n+1):
                c=a+b
                a=b
                b=c
        return c

class BruteForce(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs_(0,n)
    def climbStairs_(self, i, n):
        if i>n:
            return 0
        if i==n:
            return 1
        return self.climbStairs_(i+1,n)+self.climbStairs_(i+2,n)

bf=BruteForce()
print(bf.climbStairs(35))