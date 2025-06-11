'''
1. Two Sum

Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        nums.sort()
        if(len(nums)<2):
            return ans
        else:
            p1 = 0
            x = len(nums)
            y=0
            while x>=y:
                
                p2 = p1+1
                print(f'{p1} ,{p2}, {x}, {nums[p1]+nums[p2]}')
                if(nums[p1]+nums[p2]==target):
                    ans.append(p1)
                    ans.append(p2)
                    
                else:
                    p2+=1
                y=y+1
                
            return ans
        



Sol = Solution()
test_case_1 = [2,7,11,15]
test_case_2 = [3,2,4]
test_case_3 = [3,3]
result = Sol.twoSum(test_case_1,target = 13)
print(result)