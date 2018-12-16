# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums3[i] < nums2[j]:
                nums1[k] = nums3[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        if i == m:
            nums1[k:m + n] = nums2[j:]
        if j == n:
            nums1[k:m + n] = nums3[i:]

    # nums1[m:m+n]=nums2[:]
    # nums1[:m+n]=sorted(nums1[:m+n])

    #     j=0
    #     for i in range(m,m+n):
    #         nums1[i]=nums2[j]
    #         j+=1
    #     nums1=nums1[:m+n]
    #     self.quicksort(nums1)
    # def quicksort(self,nums1):
    #     smaller=[]
    #     larger=[]
    #     if len(nums1)<=1:return nums1
    #     else:
    #         p=nums1.pop()
    #         for i in nums1:
    #             if i>p: larger.append(i)
    #             else: smaller.append(i)
    #     return self.quicksort(smaller)+[p]+self.quicksort(larger)