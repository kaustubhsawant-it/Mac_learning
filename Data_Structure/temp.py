'''
1295. Find Numbers with Even Number of Digits


Hint
Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 105
'''

class Solution:
    def findNumbers(self, nums: list[int]) -> int:        
        digits=[]
        lb = 0
        ub = len(nums)
        Count=0
        while lb<ub:
            num = nums[lb]
            while num > 0:
                num , digit = divmod(num,10)
                digits.append(digit)
                print(digits[::-1])
            if(len(digits)%2==0):
                Count+=1
                digits.clear()
            else:
                digits.clear()
            lb+=1
        return Count

Sol = Solution()
test_case_1= [12,345,2,6,7896]
test_case_2 =  [555,901,482,1771]
test_case_3 = [55,33,23]
result = Sol.findNumbers(test_case_3)
print(result)