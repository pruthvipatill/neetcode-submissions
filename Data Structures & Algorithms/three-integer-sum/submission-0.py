class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numss = sorted(nums)
        output = []
        for i in range(len(nums)):
            if i > 0 and numss[i] == numss[i-1]:
                    continue
            left = 1+i
            right = len(numss)-1

        
            while left < right:
                
                total = numss[left]+numss[right] + numss[i]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                elif total == 0:
                    output.append([numss[left],numss[right],numss[i]])
                    left+= 1
                    right-= 1

                    while left < right and numss[left]==numss[left -1]:
                        left+=1
                    while left < right and numss[right] == numss[right+1]:
                        right -=1
                
                
        return output  
                
                
                
                

                





        