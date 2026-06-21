class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            length  = 1
            current = num

            while current + 1 in nums:
                length += 1
                current += 1
            
            count  =  max(count, length)

        return count


            
        