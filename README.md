# Coding-Challenges
Different Coding Questions on Data Structure and Algorithm concepts
1. Array Interesection : 
    1. Problem: Given two arrays of variable lengths, return the items present in both in arrays.
    2. Solution: By changing the lists into sets, the built-in intersection operation can be used on the data.
    3. Time Complexity: O(1) 
    
2. Binary Tree In-order Traversal :
    1. Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using in-order Traversal
    2. Solution 1: Using an iterative function.
    3. Solution 2: Using a recursive function.
    4. Time Complexity: O(N+M) N is number of Nodes, M is number of Edges
  
3. Binary Tree Post-order Traversal :
    1. Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using post-order Traversal
    2. Solution 1: Using an iterative function.
    3. Solution 2: Using a recursive function.
    4. Time Complexity: O(N+M) N is number of Nodes, M is number of Edges
    
4. Binary Tree Pre-order Traversal :
    1. Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using pre-order Traversal
    2. Solution 1: Using an iterative function.
    3. Solution 2: Using a recursive function.
    4. Time Complexity: O(N+M) N is number of Nodes, M is number of Edges
      
5. Circular Queue Design :
    Problem: Create a circular queue class that takes an int, creates a circular queue of size int and has the following functions:
      1. Enqueue - Adds an item to the back of the queue. If queue is full, return false. [Time Complexity - O(1)]
      2. Dequeue - Removes the item at the front of the queue. If the queue is empty, return false. [Time Complexity - O(1)]
      3. Front - Returns the item at the front of the queue. If the queue is empty, return false. [Time Complexity - O(1)]
      4. Rear - Returns the item at the back of the queue. If the queue is empty, return false. [Time Complexity - O(1)]
      5. isEmpty - Returns True if queue is empty, false otherwise. [Time Complexity - O(1)]
      6. isFull - Returns True if the queue is full, false otherwise. [Time Complexity - O(1)]
      
6. Find Duplicates :
    1. Problem: Given a list, find the elements that occur twice in the list. Case insensitive
    2. Solution: Using two for loops and sliding over each element
    3. Time Complexity: O(n^2)
      
7. Lonely Number :
    1. Problem: Given a list of elements, find the element that only occurs once.
    2. Solution: Using the difference operation on two sets
    3. Time Complexity: O(n)
     
8. Moving average from Data Stream :
    1. Problem: Given a window size, return the sum of numbers in the window. If the window is full, remove the oldest item and add the new one
    2. Solution: Using Circular Queues
    3. Time Complexity: O(1)
      
9. Number of Islands :
    1. Problem: Given a grid of 0's and 1's where 0 represents water and 1 represents land, find the number of islands (1's surrounded by 0's upwards, rightwards, leftwards and downwards).
    2. Solution: Using Breadth First Search 
    3. Time Complexity: O((NM)^2) N=number of rows , M=number of columns
      
10. Reverse a String :
    1. Problem: Given a string, reverse it 
    2. Solution: Using pointers
    3. Time Complexity: O(n)
     
11. Validate Palindrome :
    1. Problem: Given a string, check if it is the same when read forwards and backwards while ignoring whitespaces and case sensitivity
    2. Solution: Using Pointers
    3. Time Complexity: O(n)

12. Insert Delete GetRandom O(1)-with Duplicates
    1. Problem: Create a data structure with the following functions:
	-Insert: Add an element to the DS in constaant time, Insert(a)
	-Delete: Delete an element from the DS in constant time, Delete(a)
	-GetRandom: Get Random element from the DS in constant time, GetRandom()
    2. Solution: Using a dictionary, a List, and a pointer
    3. Time Complexity: O(1)

13. Word Search II
    1. Problem: Given a list of words and a 2D array of characters, return all words in the list that can be formed from the 2D array by going in the 4-cardinal directions excluding the previous character
    2. Solution: Store all Words in a Trie and search the Trie with the characters using a DFS technique
    3. Time Complexity: O(2^n)