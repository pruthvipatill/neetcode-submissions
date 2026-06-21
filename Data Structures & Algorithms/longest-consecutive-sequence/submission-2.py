class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = {}


        for i in range(len(nums)):
            current = nums[i]
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            count = max(count,length)

        return count

        
        
        