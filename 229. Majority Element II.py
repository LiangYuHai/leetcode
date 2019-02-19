# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
# Input: [3,2,3]
# Output: [3]
# Example 2:
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Dict=Counter(nums)
        return [elment for elment,count in Dict.items() if count>len(nums)/3]
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [n for n in set(nums) if nums.count(n) > len(nums) / 3] #O(n ^ 2)


from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Vote Algorithnm
        count1 = count2 = 0
        candidate1 = candidate2 = 0
        candidates = []
        for element in nums:
            if element == candidate1:
                count1 += 1
            elif element == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = element
                count1 += 1
            elif count2 == 0:
                candidate2 = element
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1

        if nums.count(candidate1) > len(nums) // 3:
            candidates.append(candidate1)
        if nums.count(candidate2) > len(nums) // 3:
            candidates.append(candidate2)
        return list(set(candidates))