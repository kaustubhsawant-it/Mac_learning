'''
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        x = len(merged_array)
        y = int((x-1)/2)
        if not (len(merged_array)%2==0):
            median = merged_array[y]
        else:
            median = (merged_array[y]+merged_array[y+1])/2
        return median


Sol = Solution()
nums1 = [1,3]
nums2 = [2,4]
result = Sol.findMedianSortedArrays(nums1,nums2)
print(result)