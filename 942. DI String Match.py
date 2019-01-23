# Given
# a
# string
# S
# that
# only
# contains
# "I"(increase) or "D"(decrease), let
# N = S.length.
#
# Return
# any
# permutation
# A
# of[0, 1, ..., N]
# such
# that
# for all i = 0, ..., N-1:
#
# If
# S[i] == "I", then
# A[i] < A[i + 1]
# If
# S[i] == "D", then
# A[i] > A[i + 1]
#
# Example
# 1:
#
# Input: "IDID"
# Output: [0, 4, 1, 3, 2]
# Example
# 2:
#
# Input: "III"
# Output: [0, 1, 2, 3]
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low,high=0,len(S)
        l=list()
        for i in S:
            if i=='I':
                l.append(low)
                low+=1
            if i=='D':
                l.append(high)
                high-=1
        l.append(low)
        return l