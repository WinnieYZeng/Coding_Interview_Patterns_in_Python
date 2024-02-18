# Coding_Interview_Patterns_in_Python
 Educative Course -> Grokking Coding Interview Patterns in Python
 Prepare coding interview in python for myself 

# Two Pointers
### Real-World Problems 
#### Memory management
 Two pointers are vital in memory allocation and deallocation. The memory pool is initialized with two pointers: the start pointer, pointing to the beginning of the available memory block, and the end pointer, indicating the end of the block. When a process or data structure requests memory allocation, the start pointer is moved forward, designating a new memory block for allocation. Conversely, when memory is released (deallocated), the start pointer is shifted backward, marking the deallocated memory as available for future allocations.

#### Product Suggestions
 While shopping online, when customers view their cart and the current total doesn’t qualify for free shipping, we want to show them pairs of products that can be bought together to make the total amount equal to the amount required to be eligible for free delivery. Two pointers can be used to suggest the pairs that add up to the required cost for free shipping.


# Fast and Slow Pointers
### Overview
 Similar to the two pointers pattern, the 'fast and slow pointers' pattern uses two pointers to traverse an iterable data structure at different speeds. It’s usually used to identify distinguishable features of directional data structures, such as a linked list or an array.

 The key idea is that the pointers start at the same location, but they move forward at different speeds. If there is a cycle, the two are bound to meet at some point in the traversal. To understand the concept, think of two runners on a track. While they start from the same point, they have different running speeds. If the race track is a circle, the faster runner will overtake the slower one after completing a lap. On the other hand, if the track is straight, the faster runner will end the race before the slower one, hence never meeting on the track again. The fast and slow pointers pattern uses the same intuition.

### Real-world problems
#### Symlink Verification
 Fast and slow pointers can be used in a symlink verification utility in an operating system. A symbolic link, or symlink, is simply a shortcut to another file. Essentially, it’s a file that points to another file. Symlinks can easily create loops or cycles where shortcuts point to each other. To avoid such occurrences, a symlink verification utility can be used. Similar to a linked list, fast and slow pointers can detect a loop in the symlinks by moving along the connected files or directories at different speeds.

#### Compiling an object-oriented program
 Usually, programs are not contained in a single file. Particularly, for large applications, modules can be divided into different files for better maintenance. Dependency relationships are then defined to specify the order of compilation for these files. However, sometimes, there might be cyclic dependencies that can lead to an error. Fast and slow pointers can be used to identify and remove these cycles for seamless compilation and execution of the program.