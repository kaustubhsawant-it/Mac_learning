'''
448
'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        seen=[]
        for x in range(0,len(nums)):
            print(x," ",nums[x])
            if nums[x] not in seen:
                seen.append(nums[x])
            
        return seen


set=[1,1]
Sol = Solution()
result = Sol.findDisappearedNumbers(set)
print(result)