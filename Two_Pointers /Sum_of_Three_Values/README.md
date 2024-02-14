# Statement
 Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

# Solution
 - Sort the input array in ascending order
 - Iterate over the entire sorted array to find th etriplet whose sum is equal to the target
 - In each itreation, make a triplet by storing the current array element and the otehr two elements using two pointers (low and high), and calculate their sum. 
 - Adjust the calculated sum value, until it becomes equal to the target value, by conditionally moving the pointers, low and high 
 - Return TRUE if the required sum is found. Otherwise, return FALSE

