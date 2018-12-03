#Given a 32-bit signed integer, reverse digits of an integer.#
class Solution(object):
    def reverse(self,x):
        """

        :param x:int
        :return:int
        """
        OVERFLOW_POS=pow(2,31)-1
        OVERFLOW_NEG=float(-pow(2,31))
        rev=0
        while x!=0:
            temp=int(float(x)/10)
            pop=x-temp*10
            x=temp
            if rev > OVERFLOW_POS/10 or (rev==OVERFLOW_POS/10 and pop>7):return 0
            if rev < OVERFLOW_NEG/10 or (rev==OVERFLOW_NEG/10 and pop<-8):return 0
            rev=rev*10+pop
        return rev

