class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = {}

        # for num in nums:
        #     seen[num]= seen.get(num,0)+ 1

        # seen_sort = dict(sorted(seen.items()))

        # for keys in seen_sort:
    
        #     if seen_sort[keys] == seen_sort[keys]+ 1:
        #         count = count + 1 
            
        # return count

        for i in range(len(nums)):
            current = nums[i]
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            count = max(count,length)

        return count

        
        
        