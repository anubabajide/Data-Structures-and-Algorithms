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

14. Check In - Check Out
    1. Problem: Given a subway scenario with users that own cards, design a system that performs three functions:
	-Swipe In(UserID, Location, Time): A user checks in the subway at a time and location
	-Swipe Out(UserID, Location, Time): A user checks out the subway at a time and location
	-Get Average(FromLocation, ToLocation): Returns the average duration of a Trip
    2. Solution: Use two dictionaries to store customer info and Trip info
    3. Time Complexity: O(1) for all functions

15. Anagram Checker
    1. Problem: Given two strings, check if they are anagrams
    2. Solution: Using hash tables (Dictionaries)
    3. Time Complexity: O(N) ; N=length of shorter word 

16. Binary Tree: Level Order Traversal
    1. Problem: Given a Binary Tree Node,  returns a List of Items in the Tree using in-order Traversal
    2. Solution : Using a Breadth First Search in an iterative function.
    3. Time Complexity: O(N) N is number of Nodes, M is number of Edges

17. Binary Tree Mirror
    1. Problem: Given a Binary Tree, get a mirror image
    2. Solution: Using BFS to traverse all nodes
    3. Time Complexity: O(N) N is number of Nodes

18. Candy Crush 1D
    1. Problem: Given a string of letters, like the candy crush game, delete any strings that are connected in threes and above
    2. Solution: Using a stack and a variable to store the last ejected 
    3. Time Complexity: O(N) N is length of the string

19. Decode String
    1. Problem: Given an encoded string (3[a]) return the decoded string (aaa).
    2. Solution: Using a stack and manually built alphabet and number checkers
    3. Time Complexity: O(N) N is the length of teh string

20. Fibonacci Sequence
    1. Problem: Write a piece of code to create a Fibonacci sequence 
    2. Solution 1: Using Recursion
    3. Solution 2: Using Iteration
    4. Time Complexity: O(N) N is the length of the sequence

21. Insert, Delete, GetRandom O(1)
    1. Problem: Create a data structure with the following functions:
    -Insert: Add an element to the DS in constaant time, Insert(a)
    -Delete: Delete an element from the DS in constant time, Delete(a)
    -GetRandom: Get Random element from the DS in constant time, GetRandom()
    Note: Only unique elements in the data structure
    2. Solution: Using a set
    3. Time Complexity: O(1)

22. Two City Scheduling:
    1. Problem: Given a list of tuples of two integers (cost of city A, cost of city B), return the minimum sum such that not more than half of each city is present in the sum.
    2. Solution: Sorting according to differences 
    3. Time Complexity: O(nlogn)