'''
3423. Maximum Difference Between Adjacent Elements in a Circular Array
Easy

Hint
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.


Example 1:
Input: nums = [1,2,4]
Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

 

Constraints:

2 <= nums.length <= 100
-100 <= nums[i] <= 100
'''
class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        lb = 1
        ub = len(nums)-1
        SP = nums[ub] - nums[lb-1]
        NSP = nums[lb-1]- nums[ub]
        dummy = 0
        while lb<=ub:
            great = nums[lb-1]-nums[lb]
            if dummy<great:
                dummy = great 
            #print(f'{nums[lb-1]} {nums[lb]} {great} {dummy}')
            lb+=1
        z =SP if (nums[ub]>nums[(lb-1)] and (dummy<SP or dummy<NSP)) else NSP
        dummy = z
        return dummy