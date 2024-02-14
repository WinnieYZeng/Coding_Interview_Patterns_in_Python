# Statement
 Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

 Note: A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.

# Solution 
 - Initialize two pointers at the beginning and end of the string. 
 - Check whether or not the current pair of characters is identical. 
 - If they are not identical, return FALSE, Otherwise, move both pointers by one index toward the middle. 
 - Keep traversing them toward the middle until they meet. 
 - If we reach the middle of the string without finding a mismatch, return TRUE.

 