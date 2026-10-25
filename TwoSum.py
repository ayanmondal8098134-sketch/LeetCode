class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for i in range(0,len(nums)):
            c = target-nums[i]

            if c in s:
                return [s[c], i]
            s[nums[i]]= i

            
        