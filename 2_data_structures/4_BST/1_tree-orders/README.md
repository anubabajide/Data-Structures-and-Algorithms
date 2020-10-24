# Binary Tree Traversals

## Description 
In this problem you will implement in-order, pre-order and post-order traversals of a binary tree.

## Details
**Task**<br>
You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.

**Input format**<br> 
The first line contains the number of vertices 𝑛. The vertices of the tree are numbered from 0 to 𝑛 − 1. Vertex 0 is the root.<br>
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains three integers 𝑘𝑒𝑦𝑖
, 𝑙𝑒𝑓𝑡<sub>𝑖</sub> and 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> — 𝑘𝑒𝑦<sub>𝑖</sub> is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡<sub>𝑖</sub> is the index of the left child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have left or right child (or both), the corresponding 𝑙𝑒𝑓 𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.

**Output format:**<br> 
Print three lines. The first line should contain the keys of the vertices in the in-order traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree.

**Constraints:**<br>
1 ≤ 𝑛 ≤ 10<sup>5</sup><br>
0 ≤ 𝑘𝑒𝑦<sub>𝑖</sub> ≤ 10<sup>9</sup><br>
−1 ≤ 𝑙𝑒𝑓𝑡<sub>𝑖</sub><br>
𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub> ≤ 𝑛 − 1.<br> 
It is guaranteed that the input
represents a valid binary tree. In particular, if 𝑙𝑒𝑓𝑡<sub>𝑖</sub> ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓𝑡<sub>𝑖</sub> ̸= 𝑟𝑖𝑔ℎ𝑡<sub>𝑖</sub>. Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex.

## Samples.
Sample 1.

    Input:
        5
        4 1 2
        2 3 4
        5 -1 -1
        1 -1 -1
        3 -1 -1
    Output:
        1 2 3 4 5
        4 2 1 3 5
        1 3 2 5 4
    
        4
       / \
      2   5
     / \
    1   3

Sample 2.

    Input:
        10
        0 7 2
        10 -1 -1
        20 -1 6
        30 8 9
        40 3 -1
        50 -1 -1
        60 1 -1
        70 5 4
        80 -1 -1
        90 -1 -1
    Output:
        50 70 80 30 90 40 0 20 10 60
        0 70 50 40 30 80 90 20 60 10
        50 80 90 30 40 70 10 60 20 0
        
                0
               / \
             70   20
            /  \    \
           50  40   60
               /    /
             30    10
            /  \
           80  90
