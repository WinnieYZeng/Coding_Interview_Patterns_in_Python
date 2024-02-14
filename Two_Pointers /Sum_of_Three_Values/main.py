"""
Solution Summary:
- Sort the array in ascending order. To find a triplet whose sum is equal to the target value,
  loop through the entire array. In each iteration:
    - store the current array element and setup two pointers(low the high)
        the low pointer is set to the current loop's index + 1
        the high pointer is set to the last index of the array
    - calculate the sum of array elements pointed to by the current loop's index and the low and high pointers
    - if the sum is equal to target, return TRUE
    - if the sum is less than target, move the low pointer forward
    - if the sum is greater than target, move the high pointer backward

- Repeat until the loop has processed the entir array. If, after processing the entire array, we don't find any triplet 
  that matches our requirement, we return FALSE

"""

def find_sum_of_three(nums, target):
    # sort the input list 
    nums.sort()

    # fix one integer at a time and find the other two 
    for i in range(0, len(nums)-2):
        # initialize the two poiners
        low, high = i + 1, len(nums) - 1

        # traverse the list to find the triplet whose sum equals the target
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]
            
            # the sum of the triplet equals the target
            if triplet == target:
                return True 
            
            # the sum of the triplet is less than target, so move the low pointer forward
            elif triplet < target:
                low += 1
            
            # the sum of the triplet is higher than target, so move the higher pointer backward
            else:
                high -= 1
    
    # no such triplet found whose sum equals the given target
    return False


# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()