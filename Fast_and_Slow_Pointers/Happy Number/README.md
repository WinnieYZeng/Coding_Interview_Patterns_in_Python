# Statement 
 Write an algorithm to determine if anumber n is a happy number
 We use the following process to check if a given number is a happy number:
 - starting with the given number n, replace the number with the sum of the squares of its digits.
 - Repeat the process until:
    - The number equals 1, which will depict that the given number n is a happy number 
    - It enters a cycle, which will depict thatthe given number n is not a happy number 
 
 Return TRUE if n is a happy number, and FALSE if not

# Solution 
 - Initialise a variable slow with the input number and fast with the sum of the squared input number's digits
 - If fast is not 1and also not equla to slow, increment slow by one iteration and fast by two iterations. Essentially, set slow to Sum of Squared Digits (slow) and fast to Sum of Squared digits (Sum of squared Digits (fast))
 - If fast converges to 1, return TRUE, otherwise return FALSE

