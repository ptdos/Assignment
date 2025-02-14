# Assignment

Assignment on Array

Task 1: Pascal's triangle

Write a function that does the following task.

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5

Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

        1

       1 1

      1 2 1

     1 3 3 1

    1 4 6 4 1

Constraints:

1 <= numRows <= 30

Task 2: Maximum Gap

Write a function that does the following task.

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]

Output: 3

Explanation: The array's sorted form is [1,3,6,9]; either (3,6) or (6,9) has a maximum difference of 3.

Example 2:

Input: nums = [10]

Output: 0

Explanation: The array contains less than 2 elements, therefore return 0.

 

Constraints:

1 <= nums.length <= 10^5

0 <= nums[i] <= 10^9
