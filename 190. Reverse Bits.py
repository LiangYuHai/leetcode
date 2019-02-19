class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r=bin(n)[::-1][:-2]
        r+='0'*(32-len(r))
        return int(r,2)