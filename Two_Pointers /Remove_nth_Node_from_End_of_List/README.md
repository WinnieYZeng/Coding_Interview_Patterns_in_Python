# Statement 
 Given a singly linkedl list, remove the nth node from the end of the list and return its head. 

 # Solution
 - Set two pointers, right and left, at the head of the linked list 
 - Move the right pointer n steps forward
 - Move both the right and left pointers forward until the right pointer reaches the last node. At this point, the left pointer will be pointing to the node behind the nth last node. 
 - Relink the left node to the node next to left's next node 
 - Return the head of the linked list 

 
