"""
Solution Summary:
- Initialize two pointers and move them from opposite ends
- The first pointer starts at the beginning of the string and moves toward the middle,
   while the second poiter starts at the end and moves toward the middle
- Compare the elements at each position to detect a nonmatching pair
- If both pointers reach the middle of the string without encountering a nonmatching pair,
   the string is a palindrome. 

Time Complexity
- The time complexity is O(n)

Space Complexity
- The space complexity is O(1)

"""


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

# Driver code
def main():
    test_cases = ["RACECAR", "ABBA", "TART"]
    i = 1
    for s in test_cases:
        print("Test Case #", i)
        print(is_palindrome(s))
        print("-" * 100, end="\n\n")
        i = i + 1

if __name__ == '__main__':
    main()
