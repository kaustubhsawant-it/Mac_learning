'''
1480. Running Sum of 1d Array
Hint
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        temp = 0
        lb = 0
        ub = len(nums)
        if(ub>0):
            while(lb<ub):
                temp = temp+nums[lb]
                ans.append(temp)
                lb+=1
            return ans
    
Sol = Solution()
test_case_1=[1,2,3,4]
test_case_2=[1,1,1,1,1]
test_case_3 = [3,1,2,10,1]
result = Sol.runningSum(test_case_3)
print(result)