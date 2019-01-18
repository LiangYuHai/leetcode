# iven an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1=0
        index2=len(numbers)-1
        while index1<index2:
            if numbers[index1]+numbers[index2]>target:
                index2-=1
            elif numbers[index1]+numbers[index2]<target:
                index1+=1
            else:
                return [index1+1,index2+1]