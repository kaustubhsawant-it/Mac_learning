'''
1342. Number of Steps to Reduce a Number to Zero

Hint
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12
 
Constraints:
0 <= num <= 106
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if(num != 0 ):
            dummy = num
            steps = 0
            while dummy>0:
                z = "Even" if dummy%2==0 else "Odd"
                if (z=="Even"):
                    dummy = dummy/2
                    steps+=1
                else:
                    dummy = dummy-1
                    steps+=1
            return steps
        else:
            return num
    



Sol = Solution()
num1 = 14
num2 = 8
num3 = 123
result = Sol.numberOfSteps(num3)
print(result)