class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #        s=bin(n)[2:]
        #        c=0
        #        for i in s:
        #            if i=='1':
        #                c+=1
        #        return c

        #        c=0
        #        while n:
        #            n&=n-1
        #            c+=1
        #        return c

        return bin(n).count('1')