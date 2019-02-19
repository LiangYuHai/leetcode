class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory=[-1]*len(nums)
        return self.rob2(nums,len(nums)-1,memory)
    def rob2(self,nums,i,memory):
        if i<0:
            return 0
        if memory[i]!=-1:
            return memory[i]
        else:
            res=max(nums[i]+self.rob2(nums,i-2,memory),self.rob2(nums,i-1,memory))
            memory[i]=res
            return res
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev2 = 0
        prev1 = 0
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(nums[i] + prev2, prev1)
            prev2 = temp
        return prev1

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        memory = list()
        memory.append(0)
        memory.append(nums[0])
        for i in range(1, len(nums)):
            memory.append(max(nums[i] + memory[i - 1], memory[i]))
        return memory[-1]

