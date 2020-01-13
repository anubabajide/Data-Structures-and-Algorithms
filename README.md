# Coding-Challenges
Different Coding Questions on Data Structure and Algorithm concepts
1. Array Interesection : 
    Problem: Given two arrays of variable lengths, return the items present in both in arrays.
    Solution: By changing the lists into sets, the built-in intersection operation can be used on the data.
        Time Complexity: O(1)
    
2. Binary Tree In-order Traversal :
    Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using in-order Traversal
    Solution 1: Using a iterative function.
    Solution 2: Using an recursive function.
        Time Complexity: O(N+M) N is number of Nodes, M is number of Edges
  
3. Binary Tree Post-order Traversal :
    Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using post-order Traversal
    Solution 1: Using a iterative function.
    Solution 2: Using an recursive function.
        Time Complexity: O(N+M) N is number of Nodes, M is number of Edges
    
4. Binary Tree Pre-order Traversal :
    Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using pre-order Traversal
    Solution 1: Using a iterative function.
    Solution 2: Using an recursive function.
        Time Complexity: O(N+M) N is number of Nodes, M is number of Edges
      
5. Circular Queue Design :
    Problem: Create a circular queue class that takes an int, creates a circular queue of size int and has the following functions:
      1. Enqueue - Adds an item to the back of the queue. If queue is full, return false
            Time Complexity - O(1)
      2. Dequeue - Removes the item at the front of the queue. If the queue is empty, return false  
            Time Complexity - O(1)
      3. Front - Returns the item at the front of the queue. If the queue is empty, return false
            Time Complexity - O(1)
      4. Rear - Returns the item at the back of the queue. If the queue is empty, return false
            Time Complexity - O(1)
      5. isEmpty - Returns True if queue is empty, false otherwise
            Time Complexity - O(1)
      6. isFull - Returns True if the queue is full, false otherwise
            Time Complexity - O(1)
      
6. Find Duplicates :
    Problem: Given a list, find the elements that occur twice in the list. Case insensitive
    Solution: Using two for loops and sliding over each element
        Time Complexity: O(n^2)
      
7. Lonely Number :
    Problem: Given a list of elements, find the element that only occurs once.
    Solution: Using the difference operation on two sets
        Time Complexity: O(n)
     
8. Moving average from Data Stream :
    Problem: Given a window size, return the sum of numbers in the window. If the window is full, remove the oldest item and add the new one
    Solution: Using Circular Queues
       Time Complexity: O(1)
      
9. Number of Islands :
    Problem: Given a grid of 0's and 1's where 0 represents water and 1 represents land, find the number of islands (1's surrounded by 0's upwards, rightwards, leftwards and downwards).
    Solution: Using Breadth First Search 
        Time Complexity: O((NM)^2) N=number of rows , M=number of columns
      
10. Reverse a String :
    Problem: Given a string, reverse it 
    Solution: Using pointers
        Time Complexity: O(n)
     
11. Validate Palindrome :
    Problem: Given a string, check if it is the same when read forwards and backwards while ignoring whitespaces and case sensitivity
    Solution: Using Pointers
        Time Complexity: O(n)
